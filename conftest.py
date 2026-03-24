
import pytest
from playwright.sync_api import Page
from pages.application import Application
from api.obj_api import ObjectsApi

@pytest.fixture(scope="function")
def app(page: Page) -> Application:
    return Application(page)

@pytest.fixture
def obj_api(playwright):

    context = playwright.request.new_context(
        base_url="http://127.0.0.1:8000 ")
    yield ObjectsApi(context)
    context.dispose()