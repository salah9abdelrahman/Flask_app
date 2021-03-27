from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.role_controller import api as role_ns
from .main.controller.card_list_controller import api as card_list_ns
from .main.controller.comment_controller import api as comment_list_ns
from .main.controller.card_controller import api as card_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Irithm task',
          version='1.0',
          description='flask api docs'
          )

api.add_namespace(user_ns, path='/users')
api.add_namespace(auth_ns)
api.add_namespace(role_ns)
api.add_namespace(card_list_ns)
api.add_namespace(card_ns, path='/cards')
api.add_namespace(comment_list_ns, path='/comments')
