import json
from flask import url_for
from app.models.user import User
from app.services.user_service import create_user

def create_test_user():
    user_data = {
        'name': 'testuser',
        'email': 'testuser@example.com',
        'password': 'testpassword',
        'endereco': 'Rua 1, 123',
        'cidade': 'Espirito Santo',
        'cep': '29100000',
        'pais': 'Brasil',
        'telefone': '27999999999',
        'cpf': '12345678900',
    }
    return create_user(user_data)

def get_access_token(client, email, password):
    response = client.post(
        url_for('api.loginresource'),
        json={'email': email, 'password': password}
    )
    data = response.get_json()
    return data['access_token']

def test_add_user(client, session):
    user_data = {
        'name': 'newuser',
        'email': 'newuser@example.com',
        'password': 'newpassword',
        'endereco': 'Rua 2, 456',
        'cidade': 'Rio de Janeiro',
        'cep': '22000000',
        'pais': 'Brasil',
        'telefone': '21999999999',
        'cpf': '09876543210',
    }
    response = client.post(
        url_for('api.registerresource'),
        json=user_data
    )
    assert response.status_code == 201
    data = response.get_json()
    assert 'access_token' in data

def test_get_user(client, session):
    user = create_test_user()
    session.commit()

    access_token = get_access_token(client, user.email, 'testpassword')
    headers = {'Authorization': f'Bearer {access_token}'}

    response = client.get(url_for('api.userresource', id=user.id), headers=headers)
    assert response.status_code == 200
    data = response.get_json()
    assert data['email'] == user.email
    assert data['name'] == user.name