from app import db

class Rental(db.Model):
    # __tablename__ = 'rentals'
    id = db.Column(db.Integer, primary_key=True)
    due_date = db.Column(db.Date, nullable=False)
    available_inventory = db.Column(db.Integer, default=0, nullable=False)

    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    customer = db.relationship("Customer", back_populates="videos")
    video_id = db.Column(db.Integer, db.ForeignKey('video.id'))
    video = db.relationship("Video", back_populates="customers")

