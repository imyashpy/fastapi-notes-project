from pydantic import BaseModel

class NoteCreate(BaseModel):
    title: str
    content: str
    category: str = "General"

class NoteUpdate(BaseModel):
    title: str
    content: str
    category: str
