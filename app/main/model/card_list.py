from app.main import db


class CardListModel(db.Model):
    __tablename__ = 'card_list'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    cards = db.relationship('CardModel', backref='card_list', lazy='dynamic')

    def __repr__(self):
        return f"<CardList title:'{self.title}', id:'{self.id}'>"

    def json(self):
        return {
            'id': self.id,
            'title': self.title,
            'cards': [card.json() for card in self.cards.all()],
            'users': [user.json() for user in self.users.all()]
        }
