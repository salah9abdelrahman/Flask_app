import datetime

from app.main import db, flask_bcrypt
import jwt
from app.main.model.blacklist import BlacklistToken
from ..config import key

# many to many table between users and card lists
user_card_list = db.Table('user_card_list',
                          db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
                          db.Column('card_list_id', db.Integer, db.ForeignKey('card_list.id'), primary_key=True),
                          )


class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(100))

    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)

    card_lists = db.relationship('CardListModel', secondary=user_card_list, backref=db.backref('users', lazy='dynamic'))
    cards = db.relationship('CardModel', backref='user', lazy='dynamic')
    comments = db.relationship('CommentModel', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def json(self):
        return {
            'id': self.id,
            'email': self.email,
            'username': self.username
        }

    @staticmethod
    def encode_auth_token(user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                key,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, key, algorithms='HS256')
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please log in again.'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    def __repr__(self):
        return f"<User name:'{self.username}', id:'{self.id}', role: {self.role}>"
