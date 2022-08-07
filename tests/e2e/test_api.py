class TestClient:
    def test_create_user(self, client):
        body = {"payload": {"data": "hello"}}
        response = client.post("/create", json=body)
        assert response.status_code == 201
