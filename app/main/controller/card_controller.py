from flask import request
from flask_restplus import Resource, reqparse
from ..util.dto import CardDto
from ..service.card_service import save_new_card, edit_a_card, get_a_card, \
    get_all_cards_ordered_by_main_comments_num_paginated, delete_card

from app.main.util.decorator import login_required

api = CardDto.api


@api.route('')
class Cards(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title',
                        type=str,
                        required=True,
                        help='This field is required')
    parser.add_argument('description',
                        type=str,
                        required=False,
                        )
    parser.add_argument('card_list_id',
                        type=int,
                        required=True,
                        )

    @api.doc('list_of__cards')
    def get(self):
        """List all  cards"""
        offset = request.args.get('offset')
        if offset:
            try:
                offset = int(offset)
            except:
                return {'message': 'bad request'}, 400
        return [card.json() for card in get_all_cards_ordered_by_main_comments_num_paginated(offset).items]

    @api.response(201, 'Card successfully created.')
    @api.doc('create a card')
    @login_required
    def post(self):
        """Creates a new card """
        data = Cards.parser.parse_args()

        return save_new_card(data=data)


@api.route('/<int:id>')
@api.param('id', 'The card list identifier')
class Card(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title',
                        type=str,
                        required=True,
                        help='This field is required')
    parser.add_argument('description',
                        type=str,
                        required=False,
                        )

    @api.doc('get a card list')
    def get(self, id):
        """get a card given its identifier"""
        card = get_a_card(id)
        if card:
            print(card)
            return card.json(), 200
        else:
            return {'status': 'fail', 'message': 'card does not exist'}, 404

    @api.response(200, 'Card successfully updated.')
    @api.doc('update a new card')
    @login_required
    def put(self, id):
        data = Card.parser.parse_args()
        return edit_a_card(id, data=data)

    @api.response(200, 'Card  successfully deleted.')
    @api.doc('delete a card')
    @login_required
    def delete(self, id):
        card = get_a_card(id)
        if not card:
            response_object = {
                'status': 'fail',
                'message': 'Card  not exists.',
            }
            return response_object, 400
        delete_card(card)
        return {'status': 'success', 'message': 'Card  successfully deleted. '}, 200
