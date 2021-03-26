from flask_restplus import Namespace, fields
from ..model.card import CardModel


class UserDto:
    api = Namespace('users', description='user related operations')
    user = api.model('users', {
        'id': fields.String(required=False, description='user id identifier'),
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'role_id': fields.Integer(required=True, description='user role id'),
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password'),
    })


class RoleDto:
    api = Namespace('roles', description='role for users related operations')
    role = api.model('roles', {
        'id': fields.Integer(required=False, description='role id'),
        'role': fields.String(required=True, description='role name'),
    })


class CommentDto:
    api = Namespace('comments', description='comment related operations')
    comment = api.model('comments', {
        'id': fields.Integer(required=False, description='comment id'),
        'text': fields.String(required=True, description='comment text'),
        'parent_comment_id': fields.Integer(required=False, description='comment text', default=None),
        'user_id': fields.Integer(required=True, description='comment user id'),
        'card_id': fields.Integer(required=True, description='comment card id'),
    })


class CardDto:
    api = Namespace('cards', description='card list related operations')
    card_list = api.model('cards', {
        'id': fields.Integer(required=False, description='list id'),
        'title': fields.String(required=True, description='card title'),
    })


class CardListDto:
    api = Namespace('card_lists', description='card list related operations')
    card_list = api.model('card_lists', {
        'id': fields.Integer(required=False, description='list id'),
        'title': fields.String(required=True, description='card title'),
        # 'cards': fields.Nested(model=CardDto.card_list, required=False, description='card title')
    })
