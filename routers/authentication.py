from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from .. import schemas,database,models
from .. hashing import Hash
from .Token import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router=APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Credential")
    
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Incorrect password")
    
    # generate jwt token and return it
    # return  create_access_token(data={"email": user.email,'password':user.password})
    
    access_token=create_access_token(data={'email':user.email})
    return {'access_token':access_token,'token_type':'bearer'}
   








