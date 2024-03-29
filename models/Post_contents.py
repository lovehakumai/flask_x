from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from extension import db

class Post_contents(db.Model):
    user_id = db.Column(db.String(300),index=True)
    post_id = db.Column(db.String(300),primary_key=True)
    image_url = db.Column(db.String(300))
    description = db.Column(db.String(150))
    good_no = db.Column(db.Integer)
    post_date = db.Column(db.DateTime, default=datetime.utcnow)

