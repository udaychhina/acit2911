DROP TABLE IF EXISTS [user];
DROP TABLE IF EXISTS hw;
CREATE TABLE [user] (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    [password] TEXT NOT NULL
);
CREATE TABLE hw (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_id INTEGER NOT NULL,
    course TEXT NOT NULL,
    [name] TEXT NOT NULL,
    typehw TEXT NOT NULL,
    [desc] TEXT NOT NULL,
    duedate TEXT NOT NULL,
    completed BOOLEAN NOT NULL,
    FOREIGN KEY (author_id) REFERENCES user(id)
);
CREATE TABLE email_list (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_id INTEGER NOT NULL,
    [email_address] TEXT NOT NULL,
    FOREIGN KEY (author_id) REFERENCES user(id)
);