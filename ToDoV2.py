# importing the libraries
from fastapi import FastAPI, HTTPException
from typing import List, Optional
from pydantic import BaseModel

# defining our api
api = FastAPI()

class TodoBase(BaseModel):
    todo_name: str
    todo_description: str

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    todo_id: int

class TodoUpdate(BaseModel):
    todo_name: Optional[str]
    todo_description: Optional[str]



# pseudo data
all_todos = [
    Todo(todo_id=1, todo_name='Sports', todo_description='Go to the gym'),
    Todo(todo_id=2, todo_name='Read', todo_description='Read 10 pages'),
    Todo(todo_id=3, todo_name='Shop', todo_description='Buy a PS5'),
    Todo(todo_id=4, todo_name='Study', todo_description='Study about AI'),
    Todo(todo_id=5, todo_name='Gaming', todo_description='Play Resident Evil 4')
]

#-------------------------------------------------------------------------------

# GET endpoints

# path parameter 
@api.get('/todo/{todo_id}', response_model=Todo)
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            return todo
        
    raise HTTPException(status_code=404, detail="Todo not found")

# @api.get('/todo')
# def get_all_todos():
#     return all_todos

# query parameter
# example: http://127.0.0.1:8000/todo?first_n=2
@api.get('/todo', response_model=List[Todo])
def get_todos(first_n: Optional[int] = None):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos
    
#-------------------------------------------------------------------------------

# POST endpoint

# we use /docs for POST for FastAPI
@api.post('/todo', response_model=Todo)
def create_todo(todo: TodoCreate):
    new_todo_id = max(todo.todo_id for todo in all_todos) + 1

    new_todo = Todo(
        todo_id=new_todo_id, 
        todo_name=todo.todo_name, 
        todo_description=todo.todo_description)
    
    all_todos.append(new_todo)

    return new_todo

#-------------------------------------------------------------------------------

# PUT endpoint

@api.put('/todo/{todo_id}', response_model=Todo)
def update_todo(todo_id: int, updated_todo: TodoUpdate):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            if updated_todo.todo_name is not None:
                todo.todo_name = updated_todo.todo_name
            if updated_todo.todo_description is not None:
                todo.todo_description = updated_todo.todo_description
            return todo
        
    raise HTTPException(status_code=404, detail="Todo not found")

#-------------------------------------------------------------------------------

# DELETE endpoint

@api.delete('/todo/{todo_id}', response_model=Todo)
def delete_todo(todo_id: int):
    for index, todo in enumerate(all_todos):
        if todo.todo_id == todo_id:
            deleted_todo = all_todos.pop(index)
            return deleted_todo
    
    raise HTTPException(status_code=404, detail="Todo not found")