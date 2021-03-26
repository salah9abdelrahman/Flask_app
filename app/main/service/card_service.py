from app.main import db
from app.main.model.card import CardModel
from app.main.service.auth_service import Auth
from flask import request


def save_new_card(data):
    logged_user_id = Auth.get_logged_in_user_id(request)

    new_card = CardModel(
        title=data['title'],
        description=data['description'],
        user_id=logged_user_id,
        card_list_id=data['card_list_id']
    )
    try:
        save_changes(new_card)
        return new_card, 201
    except:
        error_object = {
            'status': 'fail',
            'message': 'Interval server error'

        }
        return error_object, 500


def get_all_cards():
    return CardModel.query.all()


def get_a_card(_id):
    return CardModel.query.filter_by(id=_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
