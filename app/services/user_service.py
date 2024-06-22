from ..models.user import User
from ..core.database import db
from werkzeug.security import generate_password_hash, check_password_hash

def get_all_users():
    return User.query.all()

def get_user_by_id(user_id):
    return db.session.get(User, user_id)

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def create_user(data):
    data['password'] = generate_password_hash(data['password'])
    new_user = User(**data)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def update_user(user, data):
    if 'password' in data:
        data['password'] = generate_password_hash(data['password'])
    for key, value in data.items():
        setattr(user, key, value)
    db.session.commit()
    return user

def delete_user(user):
    db.session.delete(user)
    db.session.commit()

def check_password(user, password):
    return check_password_hash(user.password, password)