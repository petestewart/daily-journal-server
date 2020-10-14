CREATE TABLE `JournalEntries` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `concept` TEXT NOT NULL,
  `entry` TEXT NOT NULL,
  `date` INTEGER NOT NULL,
  `moodId` INTEGER
);

CREATE TABLE `Moods` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `label` TEXT NOT NULL,
  FOREIGN KEY(`id`) REFERENCES `JournalEntries`(`moodId`)
);

INSERT INTO `Moods` VALUES (null, "Surviving");
INSERT INTO `Moods` VALUES (null, "Balanced");
INSERT INTO `Moods` VALUES (null, "Angry");
INSERT INTO `Moods` VALUES (null, "Joyful");


INSERT INTO `JournalEntries` VALUES (null, "1235", "123", 1598458543321, 1);
INSERT INTO `JournalEntries` VALUES (null, "Happy", "It's a beatiful day", 1598458548239, 2);
INSERT INTO `JournalEntries` VALUES (null, "Sneezy", "Hello World", 1598458559152, 1);
INSERT INTO `JournalEntries` VALUES (null, "Angry", "Whatever", 1598557358781, 3);
INSERT INTO `JournalEntries` VALUES (null, "Funny", "Knock Knock", 1598557373697, 4);






SELECT * FROM `JournalEntries`;