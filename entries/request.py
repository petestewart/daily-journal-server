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