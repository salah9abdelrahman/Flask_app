from app.main import db

"""
 self referential relation https://docs.sqlalchemy.org/en/14/orm/self_referential.html
"""


class CommentModel(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(255), nullable=False)

    parent_comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    card_id = db.Column(db.Integer, db.ForeignKey('card.id'), nullable=False)

    parent = db.relationship('CommentModel', remote_side=[id])
