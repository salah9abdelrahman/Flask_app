from sqlalchemy import func

from app.main import db
from app.main.config import PAGINATION_NUMBER
from app.main.model.card import CardModel
from app.main.model.comment import CommentModel
from app.main.service.auth_service import Auth
from app.main.service.card_list_service import get_a_card_list_by_id
from flask import request


def save_new_card(data):
    logged_user_id = Auth.get_logged_in_user_id(request)
    card_list = get_a_card_list_by_id(data['card_list_id'])
    if not card_list:
        return {'status': 'fail', 'message': 'card list does not exists'}, 400
    new_card = CardModel(
        title=data['title'],
        description=data['description'],
        user_id=logged_user_id,
        card_list_id=data['card_list_id']
    )
    try:
        _save_changes(new_card)
        return new_card.json(), 201
    except:
        error_object = {
            'status': 'fail',
            'message': 'Interval server error'

        }
        return error_object, 500


def edit_a_card(_id, data):
    card = get_a_card(_id)
    if not card:
        response_object = {
            'status': 'fail',
            'message': 'Card not exists.',
        }
        return response_object, 404
    else:

        card.title = data['title']
        card.description = data['description']
        _save_changes(card)
        return card.json(), 200


def delete_card(card):
    db.session.delete(card)
    db.session.commit()


def get_all_cards_ordered_by_main_comments_num_paginated(page=1):
    return CardModel.query.outerjoin(CommentModel
                                     ).filter(CommentModel.parent_comment_id == None
                                              ).group_by(CardModel.id
                                                         ).order_by(func.count(CardModel.comments).desc()
                                                                    ).paginate(page,
                                                                               PAGINATION_NUMBER,
                                                                               error_out=False)




def get_a_card(_id):
    return CardModel.query.filter_by(id=_id).first()


def _save_changes(data):
    db.session.add(data)
    db.session.commit()
