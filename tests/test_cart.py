import json
from flask import url_for
from app.models.user import User
from app.models.product import Product
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

def create_test_product():
    product_data = {
        'name': 'Test Product',
        'description': 'This is a test product.',
        'image': 'https://example.com/product.jpg',
        'price': 100.0
    }
    product = Product(**product_data)
    return product

def get_access_token(client, email, password):
    response = client.post(
        url_for('api.loginresource'),
        json={'email': email, 'password': password}
    )
    data = response.get_json()
    return data['access_token']

def test_add_item_to_cart(client, session):
    user = create_test_user()
    product = create_test_product()
    session.add(product)
    session.commit()

    access_token = get_access_token(client, user.email, 'testpassword')
    headers = {'Authorization': f'Bearer {access_token}'}

    response = client.post(
        url_for('api.cartresource'),
        json={'product_id': product.id, 'quantity': 2},
        headers=headers
    )
    assert response.status_code == 201
    data = response.get_json()
    assert data['product_id'] == product.id
    assert data['quantity'] == 2

def test_get_cart(client, session):
    user = create_test_user()
    product = create_test_product()
    session.add(product)
    session.commit()

    access_token = get_access_token(client, user.email, 'testpassword')
    headers = {'Authorization': f'Bearer {access_token}'}

    client.post(
        url_for('api.cartresource'),
        json={'product_id': product.id, 'quantity': 2},
        headers=headers
    )

    response = client.get(url_for('api.cartresource'), headers=headers)
    assert response.status_code == 200
    data = response.get_json()
    assert len(data['items']) == 1
    assert data['items'][0]['product_id'] == product.id
    assert data['items'][0]['quantity'] == 2
    assert data['total_value'] == product.price * 2

def test_remove_item_from_cart(client, session):
    user = create_test_user()
    product = create_test_product()
    session.add(product)
    session.commit()

    access_token = get_access_token(client, user.email, 'testpassword')
    headers = {'Authorization': f'Bearer {access_token}'}

    client.post(
        url_for('api.cartresource'),
        json={'product_id': product.id, 'quantity': 2},
        headers=headers
    )

    response = client.delete(
        url_for('api.cartresource'),
        json={'product_id': product.id},
        headers=headers
    )
    assert response.status_code == 204

    response = client.get(url_for('api.cartresource'), headers=headers)
    data = response.get_json()
    assert len(data['items']) == 0
    assert data['total_value'] == 0.0