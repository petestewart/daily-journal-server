from os import stat

class Journal_Entry():

  def __init__(self, id, concept, entry, date, moodId):
    self.id = id
    self.concept = concept
    self.entry = entry
    self.date = date
    self.moodId = moodId