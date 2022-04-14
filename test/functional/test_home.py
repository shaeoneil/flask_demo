def test_index_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WEHN the '/' route is requested (GET)
    THEN check that the response is valid
    """
    with app.test_client() as test_client:
        res = test_client.get('/')
        assert res.status_code == 200
        assert b"Mike&#39;s Friends" in res.data # &#39; was used in place of '
        assert b"My List of Friends" in res.data
        assert b"My Friends" in res.data

def test_mike_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WEHN the '/mike' route is requested (GET)
    THEN check that the response is valid
    """
    with app.test_client() as test_client:
        res = test_client.get('/mike')
        assert res.status_code == 200
        assert b"Hello Mike!!" in res.data

def test_add_friend_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WEHN the '/add_friend' route is requested (GET)
    THEN check that the user is redirected to the home page
    """
    with app.test_client() as test_client:
        res = test_client.get('/add_friend')
        assert res.status_code == 302
        assert res.headers["Location"] == "/" # where are you redirecting the user


def test_add_friend_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WEHN the '/add_friend' route is requested (POST)
    THEN check that the user is redirected to the home page
    """
    with app.test_client() as test_client:
        new_friend = {"fname":"amy", "lname":"colbert"}
        res = test_client.post('/add_friend', data=new_friend)
        assert res.status_code == 302 # Found
 