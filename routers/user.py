from fastapi import APIRouter,Depends,HTTPException,status
from blog.hashing import Hash
from .. import database,schemas,models
from sqlalchemy.orm import Session

router=APIRouter(tags=['Users'])
get_db=database.get_db




@router.post('/user',response_model=schemas.ShowUser)
def create_user(request:schemas.User,db:Session=Depends(get_db)):

    hashPassword=Hash.decrypt(request.password)
    new_user=models.User(name=request.name,email=request.email,password=hashPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/user/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id {id} not available")
    db.commit()
    return user















