from hw_tracker import create_app
from hw_tracker.db import init_db
db=init_db()
app=create_app()