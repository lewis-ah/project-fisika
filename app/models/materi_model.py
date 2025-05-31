from app import db

class Materi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    judul = db.Column(db.String(100), nullable=False)
    isi = db.Column(db.Text, nullable=False)
