  
# test_hello.py
from app import app
def test_hello():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == '<h1>Prueba de Python en Docker!</h1>'
