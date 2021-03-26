from flask import request
from flask_restplus import Resource
from ..util.dto import RoleDto
from ..service.role_service import save_new_role, get_a_user, get_all_roles

api = RoleDto.api
_role = RoleDto.role


@api.route('/')
class Role(Resource):
    """add role"""

    @api.response(201, 'Role successfully created.')
    @api.doc('create a new role')
    @api.expect(_role, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_role(data=data)
