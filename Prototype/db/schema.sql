CREATE TABLE IF NOT EXISTS decks (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    creation_date TEXT DEFAULT CURRENT_TIMESTAMP,
    parent INTEGER,
    FOREIGN KEY (parent) REFERENCES decks(id)
    UNIQUE (name, parent)
);