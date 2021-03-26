import unittest
import datetime

from app.main import db
from app.main.model.role import RoleModel
from app.main.model.user import UserModel
from app.test.base import BaseTestCase


class TestUserModel(BaseTestCase):

    def test_encode_auth_token(self):
        role = RoleModel(role='Member')
        user = UserModel(
            username='test',
            email='test@test.com',
            password='test',
            role_id=1
        )
        db.session.add(role)
        db.session.add(user)
        db.session.commit()
        auth_token = UserModel.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))

    def test_decode_auth_token(self):
        role = RoleModel(role='Member')
        user = UserModel(
            username='test',
            email='test@test.com',
            password='test',
            role_id=1
        )
        db.session.add(role)
        db.session.add(user)
        db.session.commit()
        auth_token = UserModel.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertTrue(UserModel.decode_auth_token(auth_token.decode("utf-8")) == 1)


if __name__ == '__main__':
    unittest.main()
