from app.main import db
from app.main.model.role import RoleModel


def save_new_role(data):
    role = RoleModel.query.filter_by(role=data['role']).first()
    if role:
        response_object = {
            'status': 'fail',
            'message': f'role {data["role"]} already exists..',
        }
        return response_object, 409
    else:
        new_role = RoleModel(
            role=data['role'],
        )
        save_changes(new_role)
        response_object = {
            'status': 'success',
            'message': 'Successfully created.'
        }
        return response_object, 201


def get_all_roles():
    return RoleModel.query.all()


def get_a_user(_id):
    return RoleModel.query.filter_by(id=_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
