import datetime

from app.main import db
from app.main.config import PAGINATION_NUMBER
from app.main.model.comment import CommentModel
from app.main.service.auth_service import Auth
from flask import request

from app.main.service.card_service import get_a_card


def save_new_comment(data):
    logged_user_id = Auth.get_logged_in_user_id(request)
    card = get_a_card(data['card_id'])
    if not card:
        return {'status': 'fail', 'message': 'card  does not exists'}, 400
    new_comment = CommentModel(
        text=data['text'],
        parent_comment_id=data['parent_comment_id'],
        user_id=logged_user_id,
        card_id=data['card_id'],
        created_date=datetime.datetime.utcnow()
    )
    try:
        _save_changes(new_comment)
        return new_comment.json(), 201
    except:
        error_object = {
            'status': 'fail',
            'message': 'Interval server error'

        }
        return error_object, 500


def get_all_comments_paginated(page=1):
    return CommentModel.query.paginate(page, PAGINATION_NUMBER, error_out=False)


def get_a_comment(_id):
    return CommentModel.query.filter_by(id=_id).first()


def edit_a_comment(_id, data):
    comment = get_a_comment(_id)
    if not comment:
        response_object = {
            'status': 'fail',
            'message': 'Comment not exists.',
        }
        return response_object, 404
    else:

        comment.text = data['text']
        _save_changes(comment)
        return comment.json(), 200


def delete_comment(comment):
    db.session.delete(comment)
    db.session.commit()


def _save_changes(data):
    db.session.add(data)
    db.session.commit()
