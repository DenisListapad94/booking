# import pytest
#
# @pytest.fixture
# def some_fixture_1():
#     lst = [1, 2, 3]
#     return lst
#
# @pytest.fixture
# def some_fixture_2(some_fixture_1):
#     return some_fixture_1.append(4)
import pytest
from fastapi import Depends
from src.database import get_sync_session, sync_engine
from src.core.models import Base
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture(scope="session")
def create_client():
    client = TestClient(app)

@pytest.fixture(scope="session")
def create_session():
    session = get_sync_session()


@pytest.fixture(scope="session")
def create_db():
    Base.metadata.create_all(sync_engine)
    yield
    Base.metadata.drop_all(sync_engine)




