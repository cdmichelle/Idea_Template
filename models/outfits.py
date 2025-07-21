from backend.app import db

class ClosetItem(db.Model):
    __tablename__ = 'closet_items'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False, default=1)  # For now, static user_id
    filename = db.Column(db.String(120), nullable=False)
    category = db.Column(db.String(50))
    color = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
