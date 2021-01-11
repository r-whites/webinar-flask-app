def test_app(app, client):
    resp = client.get('/')
    assert '!' in resp