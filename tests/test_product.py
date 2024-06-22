import json
from flask import url_for
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

def create_test_product(session):
    product_data = {
        'name': 'Test Product',
        'description': 'This is a test product.',
        'image': 'https://example.com/product.jpg',
        'price': 100.0
    }
    product = Product(**product_data)
    session.add(product)
    session.commit()
    return product

def get_access_token(client, email, password):
    response = client.post(
        url_for('api.loginresource'),
        json={'email': email, 'password': password}
    )
    data = response.get_json()
    return data['access_token']

def test_add_product(client, session):
    user = create_test_user()
    session.commit()

    access_token = get_access_token(client, user.email, 'testpassword')
    headers = {'Authorization': f'Bearer {access_token}'}

    product_data = {
        'name': 'New Product',
        'description': 'This is a new product.',
        'image': 'https://example.com/newproduct.jpg',
        'price': 150.0
    }
    response = client.post(
        url_for('api.productlistresource'),
        json=product_data,
        headers=headers
    )
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == product_data['name']
    assert data['price'] == product_data['price']

def test_get_product(client, session):
    user = create_test_user()
    session.commit()

    access_token = get_access_token(client, user.email, 'testpassword')
    headers = {'Authorization': f'Bearer {access_token}'}

    product = create_test_product(session)

    response = client.get(url_for('api.productresource', id=product.id), headers=headers)
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == product.name
    assert data['description'] == product.description