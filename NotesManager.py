# ==================================================================
# Imports
# ==================================================================
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional


# ==================================================================
# App Initialization
# ==================================================================
app = FastAPI()


# ==================================================================
# Pydantic Models
# ==================================================================
class NoteBase(BaseModel):
    note_title: str
    note_content: str

class Note(NoteBase):
    note_id: int

class NoteCreate(NoteBase):
    pass

class NoteUpdate(BaseModel):
    note_title: Optional[str]
    note_content: Optional[str]


# ==================================================================
# Pseudo Data (In production, this would be replaced by a database)
# ==================================================================
notes = [
    Note(note_id=1, note_title="Birthday Reminder", note_content="My birthday is on 12th February")
]


# ==================================================================
# Routes
# ==================================================================

# Index
@app.get('/')
def index():
    return "Visit /docs for using this CRUD app"

# Getting a note by note id
@app.get('/note/{note_id}', response_model=Note)
def get_note(note_id: int):
    for note in notes:
        if note.note_id == note_id:
            return note
    raise HTTPException(status_code=404, detail="Note ID NOT Found")

# ------------------------------------------------------------------

# Getting first n notes
@app.get('/note', response_model=List[Note])
def get_first_n_note(first_n: Optional[int] = None):
    if first_n:
        return notes[:first_n]
    else:
        return notes
    
# ------------------------------------------------------------------
    
# Create a Note
@app.post('/note', response_model=Note)
def create_note(note: NoteCreate):
    new_note_id = max((n.note_id for n in notes), default=0) + 1
    new_note = Note(
        note_id=new_note_id,
        note_title=note.note_title,
        note_content=note.note_content
    )
    notes.append(new_note)
    return new_note

# ------------------------------------------------------------------

# Update a Note
@app.patch('/note/{note_id}', response_model=Note)
def update_note(note_id: int, updated_note: NoteUpdate):
    for note in notes:
        if note.note_id == note_id:
            if updated_note.note_title is not None:
                note.note_title = updated_note.note_title
            if updated_note.note_content is not None:
                note.note_content = updated_note.note_content
            return note
    raise HTTPException(status_code=404, detail="Note ID NOT Found")

# ------------------------------------------------------------------

# Delete a Note
@app.delete('/note/{note_id}', response_model=Note)
def delete_note(note_id: int):
    for index, note in enumerate(notes):
        if note.note_id == note_id:
            deleted_note = notes.pop(index)
            return deleted_note
    raise HTTPException(status_code=404, detail="Note ID NOT Found")