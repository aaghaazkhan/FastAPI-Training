# importing the libraries
from fastapi import FastAPI

# defining our api
api = FastAPI()

# pseudo data
all_todos = [
    {'todo_id': 1, 'todo_name': 'sports', 'todo_description': "Go to the gym"},
    {'todo_id': 2, 'todo_name': 'read', 'todo_description': "Read 10 pages"},
    {'todo_id': 3, 'todo_name': 'shop', 'todo_description': "Go to shopping"},
    {'todo_id': 4, 'todo_name': 'study', 'todo_description': "Study for exam"},
    {'todo_id': 5, 'todo_name': 'meditate', 'todo_description': "Meditate 20 minutes"}
]

#--------------------------------------------------------------------------------

# GET endpoints

@api.get('/')
def index():
    return {"message": "Hello World"}

# path parameter 
@api.get('/todo/{todo_id}')
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            return {"result": todo}
    return {"error": "Please enter a valid ID"}

# @api.get('/todo')
# def get_all_todos():
#     return all_todos

# query parameter
# example: http://127.0.0.1:8000/todo?first_n=2
@api.get('/todo')
def get_todos(first_n: int = None):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos
    
#--------------------------------------------------------------------------------
# POST endpoint

# we use /docs for POST for FastAPI
@api.post('/todo')
def create_todo(todo: dict):
    new_todo_id = max(todo['todo_id'] for todo in all_todos) + 1
    new_todo = {
        'todo_id': new_todo_id,
        'todo_name': todo['todo_name'],
        'todo_description': todo['todo_description']
    }
    all_todos.append(new_todo)

    return new_todo

#--------------------------------------------------------------------------------
# PUT endpoint

@api.put('/todo/{todo_id}')
def update_todo(todo_id: int, updated_todo: dict):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            todo['todo_name'] = updated_todo['todo_name']
            todo['todo_description'] = updated_todo['todo_description']
            return todo

    return "Error, Not Found"

#--------------------------------------------------------------------------------

# DELETE endpoint

@api.delete('/todo/{todo_id}')
def delete_todo(todo_id: int):
    for index, todo in enumerate(all_todos):
        if todo['todo_id'] == todo_id:
            deleted_todo = all_todos.pop(index)
            return deleted_todo
    
    return "Error, Not Found"