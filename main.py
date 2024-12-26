from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app=FastAPI(title='Created API',version='0.1.5')

@app.get('/blog')   # query parameter
def index(limit,published:bool):
    if published:
        return {'data':f'{limit} published blog list of database'}
    else:
         return {'data':f'{limit} blog list of database'}
    
@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blog'}

@app.get('/blog/{id}')
def show(id:int):          #path operation function
    return {'data':id}

@app.get('/blog/{id}/comments')
def comments(id):          #with parameters
    return {'data':{'1','2'}}


class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]


@app.post('/blog')
def created_blog(blog:Blog):
    return{'data':f'Blog is created title as {blog.title}'}





