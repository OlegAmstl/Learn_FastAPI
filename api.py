from fastapi import FastAPI

from model import Todo

from todo import todo_router

app = FastAPI()

todo_list = []


@todo_router.post('/todo')
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {'message': 'Todo added successfully'}


@todo_router.get("/todo")
async def retrieve() -> dict:
    return {'todos': todo_list}


app.include_router(todo_router)
