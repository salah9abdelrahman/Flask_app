from app.main import db


class RoleModel(db.Model):
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(255))

    users = db.relationship('UserModel', backref='role', lazy='dynamic')

    def __repr__(self):
        return self.role
