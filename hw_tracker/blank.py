from db import get_db

db = get_db()
user = db.execute(
    'SELECT * FROM user'
).fetchone()
