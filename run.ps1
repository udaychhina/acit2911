$env:FLASK_APP = "hw_tracker"
$env:FLASK_ENV = "development"
#Run this on first time run
#flask init-db
flask run

#email nofitication
#python hw_tracker/email_alert.py