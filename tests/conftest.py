import pytest
from sqlalchemy.orm import scoped_session, sessionmaker
from app import create_app
from app.core.database import db as _db
from app.core.config import TestConfig

@pytest.fixture(scope='session')
def app():
    # Cria uma instância do app
    app = create_app()
    # Configura o app para usar a configuração de teste
    app.config.from_object(TestConfig)
    # Cria as tabelas no banco de dados
    with app.app_context():
        _db.create_all()
    return app

@pytest.fixture(scope='session')
def db(app):
    return _db

@pytest.fixture(scope='function')
def client(app):
    return app.test_client()

@pytest.fixture(scope='function')
def session(db, app):
    with app.app_context():
        # Conecta ao banco de dados
        connection = db.engine.connect()
        # Inicia uma transação
        transaction = connection.begin()
        # Define as opções de conexão
        options = dict(bind=connection, binds={})
        # Cria uma sessão escopada
        Session = scoped_session(sessionmaker(bind=connection))

        # Atribui no db.session
        db.session = Session

        # Fornece para testes
        yield Session

        # Após os testes, faz rollback
        transaction.rollback()
        # Fecha a conexão
        connection.close()
        # Remove a sessão
        Session.remove()