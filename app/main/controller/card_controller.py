from flask_restplus import Resource, reqparse
from ..util.dto import CardListDto
from ..service.card_list_service import save_new_card_list, get_a_card_list_by_id, get_all_lists, edit_a_card_list, \
    assign_member, delete_card_list

from app.main.util.decorator import login_required, admin_token_required

api = CardListDto.api
_card_list = CardListDto.card_list


@api.route('/')
class CardLists(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title',
                        type=str,
                        required=True,
                        help='This field is required')

    @api.doc('list_of__cards')
    def get(self):
        """List all  lists"""
        return [card_list.json() for card_list in get_all_lists()]

    @api.response(201, 'Card successfully created.')
    @api.doc('create a new user')
    def post(self):
        """Creates a new User """
        data = CardLists.parser.parse_args()
        print('nani')
        print(data)
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
        """get a user given its identifier"""
        card_list = get_a_card_list_by_id(id)
        if card_list:
            print(card_list)
            return card_list.json(), 200
        else:
            api.abort(404)

    @api.response(200, 'Card successfully updated.')
    @api.doc('update a new user')
    def put(self, id):
        data = CardList.parser.parse_args()
        return edit_a_card_list(id, data=data)

    @api.response(200, 'Card list successfully deleted.')
    @api.doc('delete a card')
    def delete(self, id):
        card_list = get_a_card_list_by_id(id)
        if not card_list:
            response_object = {
                'status': 'fail',
                'message': 'Card list not exists.',
            }
            return response_object, 400
        delete_card_list(card_list=card_list)
        return {'status': 'success', 'message': 'Card list successfully deleted. '}, 200


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
