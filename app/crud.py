from database import get_connection


#making notes
def create_note(title, content, category):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO notes (title, content, category)
        VALUES (%s, %s, %s)
    """
    cursor.execute(query, (title, content, category))
    conn.commit()
    cursor.close()
    conn.close()



#reading notes or fetching
def get_all_notes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()
    cursor.close()
    conn.close()
    return notes


# updating note
def update_note(note_id, title, content, category):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        UPDATE notes
        SET title = %s, content = %s, category = %s
        WHERE id = %s
    """

    cursor.execute(query, (title, content, category, note_id))
    conn.commit()

    affected_rows = cursor.rowcount

    cursor.close()
    conn.close()

    return affected_rows


# deleting note
def delete_note(note_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = "DELETE FROM notes WHERE id = %s"
    cursor.execute(query, (note_id,))
    conn.commit()

    affected_rows = cursor.rowcount

    cursor.close()
    conn.close()

    return affected_rows
