from app.main import db
from app.main.model.user import UserModel


def save_new_user(data):
    user = UserModel.query.filter_by(email=data['email']).first()
    if user:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409
    else:
        new_user = UserModel(
            email=data['email'],
            username=data['username'],
            password=data['password'],
            role_id=data['role_id']
        )
        try:
            save_changes(new_user)
            return generate_token(new_user)
        except:
            error_object = {
                'status': 'fail',
                'message': 'Interval server error'

            }
            return error_object, 500


def generate_token(user):
    try:
        # generate the auth token
        auth_token = user.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def get_all_users():
    return UserModel.query.all()


def get_a_user(_id):
    return UserModel.query.filter_by(id=_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
