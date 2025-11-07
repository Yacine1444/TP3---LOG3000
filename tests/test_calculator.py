"""
Flask Calculator – Test Module
------------------------------
This module tests:
- the calculator functions (backend)
- the Flask route behavior (integration)
- the structure and visibility of the HTML interface (frontend)
"""

import pytest
from app import app, calculate
from operators import add, subtract, multiply, divide
from bs4 import BeautifulSoup


# ==============================================================
# UNIT TESTS – BACKEND (calculation functions)
# ==============================================================

def test_add():
    """Tests the add() function: simple addition."""
    assert add(2, 3) == 5


def test_subtract():
    """Tests the subtract() function: standard subtraction."""
    assert subtract(5, 2) == 3


def test_multiply():
    """Tests the multiply() function: standard multiplication."""
    assert multiply(2, 3) == 6


def test_divide():
    """Tests the divide() function: standard division."""
    assert divide(5, 2) == 2.5


def test_divide_by_zero():
    """Ensures that division by zero raises an error."""
    with pytest.raises(ZeroDivisionError):
        _ = divide(5, 0)


# ==============================================================
# BACKEND TESTS – calculate() function
# ==============================================================

def test_calculate_addition():
    """Tests calculate() with a valid addition expression."""
    assert calculate("3+4") == 7


def test_calculate_invalid_format():
    """Tests detection of invalid expressions."""
    with pytest.raises(ValueError):
        calculate("+5")


def test_calculate_non_numeric():
    """Tests detection of non-numeric characters."""
    with pytest.raises(ValueError):
        calculate("a+b")


# ==============================================================
# INTEGRATION TESTS – Flask routes
# ==============================================================

@pytest.fixture
def client():
    """Creates a Flask test client to simulate HTTP requests."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_route_get(client):
    """Tests GET request: the home page should load correctly with the title."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Flask Calculator" in response.data


def test_home_route_post_valid(client):
    """Tests POST request with a valid expression."""
    response = client.post("/", data={"display": "2+3"})
    assert response.status_code == 200
    assert b"5" in response.data


def test_home_route_post_invalid(client):
    """Tests POST request with an invalid expression."""
    response = client.post("/", data={"display": "3++2"})
    assert b"Error" in response.data


# ==============================================================
# FRONTEND TESTS – HTML structure (using BeautifulSoup)
# ==============================================================

def test_html_has_title(client):
    """Checks that the page contains the title 'Flask Calculator'."""
    response = client.get('/')
    assert b"Flask Calculator" in response.data


def test_html_buttons_present(client):
    """Checks that all buttons (0–9 and operators) are visible in the HTML page."""
    response = client.get('/')
    soup = BeautifulSoup(response.data, 'html.parser')
    buttons = [b.text.strip() for b in soup.find_all('button')]
    expected_buttons = {'0','1','2','3','4','5','6','7','8','9','+','-','*','/','=','C'}
    missing = expected_buttons - set(buttons)
    assert not missing, f"Missing or mislabeled buttons: {missing}"


def test_html_has_display_field(client):
    """Checks that the display input field is present and readonly."""
    response = client.get('/')
    soup = BeautifulSoup(response.data, 'html.parser')
    display = soup.find('input', {'id': 'display'})
    assert display is not None
    assert display.has_attr('readonly')
