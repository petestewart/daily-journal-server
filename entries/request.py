import sqlite3
import json
from models import Entry, Mood

def get_all_entries():
  with sqlite3.connect("./dailyjournal.db") as conn:

    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()

    db_cursor.execute("""
    SELECT
      j.id,
      j.concept,
      j.entry,
      j.date,
      j.moodId,
      m.label,
      m.id mood_id
    FROM JournalEntries j
    LEFT JOIN Moods m ON j.moodId = m.id
    """)

    entries = []

    dataset = db_cursor.fetchall()

    for row in dataset:

      entry = Entry(row['id'], row['concept'], row['entry'], row['date'], row['moodId'])

      mood = Mood(row['mood_id'], row['label'])

      entry.mood = mood.__dict__

      entries.append(entry.__dict__)

  return json.dumps(entries)

def get_single_entry(id):
  with sqlite3.connect("./dailyjournal.db") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()

  db_cursor.execute("""
  SELECT
    j.id,
    j.concept,
    j.entry,
    j.date,
    j.moodId,
    m.label,
    m.id mood_id
  FROM JournalEntries j
  LEFT JOIN Moods m ON j.moodId = m.id
  WHERE j.id = ?
  """, ( id, ))

  data = db_cursor.fetchone()

  entry = Entry(data['id'], data['concept'], data['entry'], data['date'], data['moodId'])

  mood = Mood(data['mood_id'], data['label'])

  entry.mood = mood.__dict__

  return json.dumps(entry.__dict__)

def delete_entry(id):
  with sqlite3.connect("./dailyjournal.db") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()

    db_cursor.execute("""
    DELETE FROM JournalEntries
    WHERE id = ?
    """, (id, ))

def create_entry(new_entry):
  with sqlite3.connect("./dailyjournal.db") as conn:

    db_cursor = conn.cursor()

    db_cursor.execute("""
    INSERT INTO JournalEntries
      ( id, concept, entry, date, moodId )
    VALUES
      ( Null, ?, ?, ?, ?)
    """, (new_entry['concept'], new_entry['entry'], new_entry['date'], new_entry['moodId']))

def update_entry(id, updated_entry):
  with sqlite3.connect("./dailyjournal.db") as conn:

    db_cursor = conn.cursor()

    db_cursor.execute("""
    UPDATE JournalEntries
      SET
        concept = ?,
        entry = ?,
        date = ?,
        moodId = ?
      WHERE id = ?
    """, (updated_entry['concept'], updated_entry['entry'], updated_entry['date'], updated_entry['moodId'], id))

    rows_affected = db_cursor.rowcount

  if rows_affected == 0:
    return False
  else:
    return True