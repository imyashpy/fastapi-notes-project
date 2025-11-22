from app.database import get_connection

def create_note(title:str,content:str):
    db = get_connection()
    cursor = db.cursor()
    cursor.execute(
        "insert into notes (title,content) values(%s,%s)",
        (title,content)
    )
    db.commit()
    cursor.close()
    db.close()
    return {"message":"note created!"}

def get_note():
    db = get_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("select * from notes")
    notes = cursor.fetchall()
    cursor.close()
    db.close()
    return notes







