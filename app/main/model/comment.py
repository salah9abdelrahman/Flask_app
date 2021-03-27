from sqlalchemy.orm import backref

from app.main import db

"""
 self referential relation https://docs.sqlalchemy.org/en/14/orm/self_referential.html
"""


class CommentModel(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(255), nullable=False)

    parent_comment_id = db.Column(db.Integer, db.ForeignKey('comment.id', ondelete='CASCADE'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    card_id = db.Column(db.Integer, db.ForeignKey('card.id'), nullable=False)
    created_date = db.Column(db.DateTime)

    replies = db.relationship('CommentModel', cascade='all',
                              backref=backref('Parent', remote_side=[id]))

    def json(self):
        return {
            'id': self.id,
            'text': self.text,
            'created_date': str(self.created_date),
            'parent_comment_id': self.parent_comment_id,
            'card_id': self.card_id,
            'replies': [replay.json() for replay in self.replies]
        }
