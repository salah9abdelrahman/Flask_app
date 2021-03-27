from flask import request
from flask_restplus import Resource
from ..util.dto import UserDto
from ..service.user_service import save_new_user, get_all_users_paginated, get_a_user
from app.main.util.decorator import login_required, admin_token_required

api = UserDto.api


@api.route('')
class UserList(Resource):
    @api.doc('list_of__users')
    @admin_token_required
    def get(self):
        offset = request.args.get('offset')
        if offset:
            try:
                offset = int(offset)
            except:
                return {'message': 'bad request'}, 400

        return [user.json() for user in get_all_users_paginated(offset).items]


@api.route('/<id>')
@api.param('id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @admin_token_required
    def get(self, id):
        """get a user given its identifier"""
        user = get_a_user(id)
        if user:
            return user.json()
        else:
            api.abort(404)
