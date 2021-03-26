from flask import request
from flask_restplus import Resource
from ..util.dto import CommentDto
from ..service.comment_service import save_new_comment, save_changes, get_a_comment, get_all_comments
from app.main.util.decorator import login_required, admin_token_required

api = CommentDto.api
_comment = CommentDto.comment


@api.route('/')
class CommentList(Resource):
    @api.doc('list_of__comments')
    @api.marshal_list_with(_comment, envelope='data')
    def get(self):
        """List all  comments"""
        return get_all_comments()

    @api.response(201, 'Card successfully created.')
    @api.doc('create a new user')
    @api.expect(_comment, validate=True)
    def post(self):
        """Creates a new comment """
        data = request.json
        return save_new_comment(data=data)


@api.route('/<comment_id>')
@api.param('comment_id', 'The comment identifier')
@api.response(404, 'comment not found.')
class Comment(Resource):
    @api.doc('get a comment')
    @api.marshal_with(_comment)
    def get(self, comment_id):
        """get a comment given its identifier"""
        comment = get_a_comment(comment_id)
        if comment:
            print(comment)
            return comment
        else:
            api.abort(404)
