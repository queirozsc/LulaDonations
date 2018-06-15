import pytest

from setup_classes import Session


@pytest.fixture
def db_session():
    session = Session()
    yield session
    session.close()

@pytest.mark.usefixtures('db_session')
def test_db_acess_save():
    """"Test db save"""
    print('### Running save')


def test_db_acess_delete(db_session):
    """"Test db deletion"""
    print('### Running delete')