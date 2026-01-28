import sys
import pytest
import allure
import os
from playwright.sync_api import sync_playwright
from pathlib import Path
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
env_path = ROOT / '.env'

# Cargar .env
load_dotenv(dotenv_path=env_path, override=True)

# Agregar paths
SRC = ROOT / 'src'
SUPPORT = ROOT / 'support'

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))
if str(SUPPORT) not in sys.path:
    sys.path.insert(0, str(SUPPORT))


def pytest_configure(config):
    """Hook que se ejecuta antes de cualquier test"""
    load_dotenv(dotenv_path=env_path, override=True)


def pytest_configure_node(node):
    """Hook específico para workers de pytest-xdist"""
    load_dotenv(dotenv_path=env_path, override=True)


@pytest.fixture(scope="session", autouse=True)
def load_environment():
    """Carga las variables de entorno"""
    load_dotenv(dotenv_path=env_path, override=True)

    # Agregar información al reporte de Allure
    # allure.environment(
    #     BASE_URL=os.getenv('BASE_URL'),
    #     ENVIRONMENT=os.getenv('ENVIRONMENT', 'dev'),
    #     BROWSER='Chromium',
    #     PYTHON_VERSION=sys.version.split()[0]
    # )

    yield


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        #browser = p.chromium.launch(headless=False) # Levanta el navegador en local
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    yield page

    # Capturar screenshot en caso de fallo
    if hasattr(page, '_playwright_page'):
        try:
            screenshot = page.screenshot()
            allure.attach(
                screenshot,
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )
        except:
            pass

    context.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook para capturar screenshots en fallos"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # Agregar metadata del fallo
        allure.attach(
            str(call.excinfo),
            name="Error Details",
            attachment_type=allure.attachment_type.TEXT
        )


pytest_plugins = ['tests.step_defs.test_login_steps']