from crud import create_note, get_all_notes, update_note, delete_note
from models import NoteCreate, NoteUpdate
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "server is running"}



@app.get("/notes")
async def all_notes():
    return get_all_notes()



@app.post("/note")
async def add_note(note: NoteCreate):
    note_id = create_note(note.title, note.content, note.category)
    return {
        "response": "note created successfully",
        "note": {
            "id": note_id,
            "title": note.title,
            "content": note.content,
            "category": note.category
        }
    }

#update route
@app.put("/note/{note_id}")
async def update_existing_note(note_id: int, note: NoteUpdate):
    result = update_note(note_id, note.title, note.content, note.category)

    if result == 0:
        return {"error": "Note not found"}

    return {"message": "Note updated successfully"}


#delete route
@app.delete("/note/{note_id}")
async def delete_existing_note(note_id: int):
    result = delete_note(note_id)

    if result == 0:
        return {"error": "Note not found"}

    return {"message": "Note deleted successfully"}

