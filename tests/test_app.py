def test_app(app, client):
    resp = client.get('/')
    assert '!' in resp.get_data(as_text=True)