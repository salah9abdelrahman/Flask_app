from flask import request
from flask_restplus import Resource, reqparse
from ..util.dto import CommentDto
from ..service.comment_service import get_a_comment, edit_a_comment, delete_comment, save_new_comment, \
    get_all_comments_paginated

from app.main.util.decorator import login_required, admin_token_required

api = CommentDto.api


@api.route('')
class Comments(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('text',
                        type=str,
                        required=True,
                        help='This field is required')
    parser.add_argument('parent_comment_id',
                        type=int,
                        required=False,
                        )
    parser.add_argument('card_id',
                        type=int,
                        required=True,
                        )

    @api.doc('list_of__comments')
    def get(self):
        """List all  comments"""
        offset = request.args.get('offset')
        if offset:
            try:
                offset = int(offset)
            except:
                return {'message': 'bad request'}, 400
        return [comment.json() for comment in get_all_comments_paginated().items]

    @api.response(201, 'comment successfully created.')
    @api.doc('create a comment')
    @login_required
    def post(self):
        """Creates a new comment """
        data = Comments.parser.parse_args()

        return save_new_comment(data=data)


@api.route('/<int:id>')
@api.param('id', 'The comment  identifier')
class Comment(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('text',
                        type=str,
                        required=True,
                        help='This field is required')

    @api.doc('get a comment')
    def get(self, id):
        """get a comment given its identifier"""
        comment = get_a_comment(id)
        if comment:
            print(comment)
            return comment.json(), 200
        else:
            return {'status': 'fail', 'message': 'comment does not exist'}, 404

    @api.response(200, 'Comment successfully updated.')
    @api.doc('update a new comment')
    @login_required
    def put(self, id):
        data = Comment.parser.parse_args()
        return edit_a_comment(id, data=data)

    @api.response(200, 'Comment  successfully deleted.')
    @api.doc('delete a comment')
    @login_required
    def delete(self, id):
        comment = get_a_comment(id)
        if not comment:
            response_object = {
                'status': 'fail',
                'message': 'comment  not exists.',
            }
            return response_object, 400
        delete_comment(comment)
        return {'status': 'success', 'message': 'comment  successfully deleted. '}, 200
