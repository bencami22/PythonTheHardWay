from nose.tools import *
from ex51 import app

app.config['TESTING'] = True
web = app.test_client()

def test_index():
    rv = web.get('/', follow_redirects=True)
    assert_equal(rv.status_code, 404)

    rv = web.get('/hello', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b"Fill out this form", rv.data)

    data = {'name':'Ben', 'greet':'Hola'}
    rv = web.post('/hello', follow_redirects=True, data = data)
    assert_in(b"Ben", rv.data)
    assert_in(b"Hola", rv.data)
