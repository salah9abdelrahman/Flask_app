from app.main import db
from app.main.model.comment import CommentModel
from app.main.service.auth_service import Auth
from flask import request


def save_new_comment(data):
    logged_user_id = Auth.get_logged_in_user_id(request)
    new_comment = CommentModel(
        text=data['text'],
        parent_comment_id=data['text'],
        user_id=logged_user_id,
        card_id=data['card_id']
    )
    try:
        save_changes(new_comment)
        return new_comment, 201
    except:
        error_object = {
            'status': 'fail',
            'message': 'Interval server error'

        }
        return error_object, 500


def get_all_comments():
    return CommentModel.query.all()


def get_a_comment(_id):
    return CommentModel.query.filter_by(id=_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
