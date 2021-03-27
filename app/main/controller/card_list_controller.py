from flask_restplus import Resource, reqparse
from flask import request
from ..util.dto import CardListDto
from ..service.card_list_service import save_new_card_list, get_a_card_list_by_id, get_all_lists_paginated, \
    edit_a_card_list, assign_member, delete_card_list

from app.main.util.decorator import login_required, admin_token_required

api = CardListDto.api


@api.route('')
class CardLists(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title',
                        type=str,
                        required=True,
                        help='This field is required')

    @api.doc('list_of__card_lists')
    @admin_token_required
    def get(self):
        offset = request.args.get('offset')
        if offset:
            try:
                offset = int(offset)
            except:
                return {'message': 'bad request'}, 400
        """List all  lists"""
        return [card_list.json() for card_list in get_all_lists_paginated(offset).items]

    @api.response(201, 'Card successfully created.')
    @api.doc('create a new card list')
    @admin_token_required
    def post(self):
        """Creates a new card list """
        data = CardLists.parser.parse_args()
        return save_new_card_list(data=data)


@api.route('/<int:id>')
@api.param('id', 'The card list identifier')
class CardList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title',
                        type=str,
                        required=True,
                        help='This field is required')

    @api.doc('get a card list')
    def get(self, id):
        """get a card list given its identifier"""
        card_list = get_a_card_list_by_id(id)
        if card_list:
            print(card_list)
            return card_list.json(), 200
        else:
            return {'status': 'fail', 'message': 'card list does not exist'}, 404

    @api.response(200, 'Card successfully updated.')
    @api.doc('update a new card list')
    @admin_token_required
    def put(self, id):
        data = CardList.parser.parse_args()
        return edit_a_card_list(id, data=data)

    @api.response(200, 'Card list successfully deleted.')
    @api.doc('delete a card')
    @admin_token_required
    def delete(self, id):
        card_list = get_a_card_list_by_id(id)
        if not card_list:
            response_object = {
                'status': 'fail',
                'message': 'Card list not exists.',
            }
            return response_object, 400

        return delete_card_list(card_list=card_list)


@api.route('/<int:id>/member/assign')
class CardListMemberAssignment(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('user_id',
                        type=int,
                        required=True,
                        help='This field is required')

    @api.doc('assign a new user')
    def put(self, id):
        data = CardListMemberAssignment.parser.parse_args()
        return assign_member(card_list_id=id, user_id=data['user_id'], assign=True)


@api.route('/<int:id>/member/un-assign')
class CardListMemberUnAssignment(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('user_id',
                        type=int,
                        required=True,
                        help='This field is required')

    def put(self, id):
        data = CardListMemberAssignment.parser.parse_args()
        return assign_member(card_list_id=id, user_id=data['user_id'], assign=False)
