import os
from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture(scope="session", autouse=True)
def setup_application() -> Generator[None, None, None]:
    fastapi_app = app
    yield fastapi_app


@pytest.fixture(scope="module")
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="session", autouse=True)
def override_settings() -> None:
    os.environ["ENV"] = "test"
