import functools
from flask import request
from app.main.service.auth_service import Auth


def login_required(func):
    @functools.wraps(func)
    def wrapper_login_required(*args, **kwargs):
        data, status = Auth.get_logged_in_user(request)
        token = data.get('data')

        if not token:
            return data, status
        return func(*args, **kwargs)

    return wrapper_login_required


def admin_token_required(func):
    @functools.wraps(func)
    def decorated(*args, **kwargs):
        data, status = Auth.get_logged_in_user(request)
        token = data.get('data')
        print(token)
        if not token:
            return data, status

        admin = token.get('role')
        print(admin)
        if admin.lower() != 'admin':
            response_object = {
                'status': 'fail',
                'message': 'admin token required'
            }
            return response_object, 401
        return func(*args, **kwargs)

    return decorated
