from flask import request
from flask_restplus import Resource
from ..util.dto import UserDto
from ..service.user_service import save_new_user, get_all_users, get_a_user
from app.main.util.decorator import login_required, admin_token_required

api = UserDto.api
_user = UserDto.user

@api.route('/')
class UserList(Resource):
    @api.doc('list_of__users')
    @api.marshal_list_with(_user, envelope='data')
    @admin_token_required
    def get(self):
        """List all  users"""
        return get_all_users()

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)


@api.route('/<id>')
@api.param('id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, id):
        """get a user given its identifier"""
        user = get_a_user(id)
        if user:
            print(user)
            return user
        else:
            api.abort(404)