from fastapi import FastAPI
from app.models import Note
import app.crud as crud

app = FastAPI()

@app.get("/")
def home():
    return {"message":"welcome to YashTech Industries",
            "message2":"Server is running!"}


@app.post("/notes")
def create_note_route(note:Note):
    return crud.create_note(note.title,note.content)

@app.get("/notes")
def show_note():
    return crud.get_note()