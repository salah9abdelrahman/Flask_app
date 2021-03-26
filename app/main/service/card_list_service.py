from app.main import db
from app.main.model.card_list import CardListModel

from app.main.service.user_service import get_a_user


def save_new_card_list(data):
    card_list = get_a_card_list_by_title(data['title'])
    if card_list:
        response_object = {
            'status': 'fail',
            'message': 'Card already exists.',
        }
        return response_object, 400
    else:
        new_card = CardListModel(
            title=data['title'],
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


def get_all_lists():
    return CardListModel.query.all()


def get_a_card_list_by_id(_id):
    return CardListModel.query.filter_by(id=_id).first()


def get_a_card_list_by_title(title):
    return CardListModel.query.filter_by(title=title).first()


def edit_a_card_list(_id, data):
    print(data['title'])
    card_list = get_a_card_list_by_id(_id)
    if not card_list:
        response_object = {
            'status': 'fail',
            'message': 'Card not exists.',
        }
        return response_object, 400
    else:
        card_list_by_title = get_a_card_list_by_title(data['title'])
        if card_list_by_title:
            response_object = {
                'status': 'fail',
                'message': 'Card already exists.',
            }
            return response_object, 400
        else:
            card_list.title = data['title']

            _save_changes(card_list)
        return card_list.json(), 200


def assign_member(card_list_id, user_id, assign):
    card_list = get_a_card_list_by_id(card_list_id)
    if not card_list:
        response_object = {
            'status': 'fail',
            'message': 'card list not exists'
        }
        return response_object, 400
    user = get_a_user(user_id)
    if not user:
        response_object = {
            'status': 'fail',
            'message': 'user not exists'
        }
        return response_object, 400

    if assign:
        card_list.users.append(user)
    else:
        card_list.users.remove(user)
    db.session.commit()
    return card_list.json(), 200


def delete_card_list(card_list):
    db.session.delete(card_list)
    db.session.commit()


def _save_changes(data):
    db.session.add(data)
    db.session.commit()
