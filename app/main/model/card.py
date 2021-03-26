from app.main import db


class CardModel(db.Model):
    __tablename__ = 'card'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255))

    card_list_id = db.Column(db.Integer, db.ForeignKey('card_list.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comments = db.relationship('CommentModel', backref='card', lazy='dynamic')

    def json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
        }

