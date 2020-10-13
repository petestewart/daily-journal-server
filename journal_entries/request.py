import sqlite3
import json
from models import Journal_Entry

def get_all_entries():
  with sqlite3.connect("./dailyjournal.db") as conn:

    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()

    db_cursor.execute("""
    SELECT
      a.id,
      a.concept,
      a.entry,
      a.date,
      a.moodId
    FROM JournalEntries a
    """)

    entries = []

    dataset = db_cursor.fetchall()

    for row in dataset:

      entry = Journal_Entry(row['id'], row['concept'], row['entry'], row['date'], row['moodId'])

      entries.append(entry.__dict__)

  return json.dumps(entries)

def get_single_entry(id):
  with sqlite3.connect("./dailyjournal.db") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()

  db_cursor.execute("""
  SELECT
    a.id,
    a.concept,
    a.entry,
    a.date,
    a.moodId
  FROM JournalEntries a
  WHERE a.id = ?
  """, ( id, ))

  data = db_cursor.fetchone()

  entry = Journal_Entry(data['id'], data['concept'], data['entry'], data['date'], data['moodId'])

  return json.dumps(entry.__dict__)