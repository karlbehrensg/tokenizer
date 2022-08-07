from src.utils.tokenizer import Tokenizer

class TestClient:
    body = {"payload": {"data": "hello"}}

    def test_create_token(self, client):
        response = client.post("/api/create", json=self.body)
        assert response.status_code == 201

    def test_no_body_to_create_token(self, client):
        response = client.post("/api/create")
        assert response.status_code == 422

    def test_verify_token(self, client):
        tokenizer = Tokenizer()
        token = tokenizer.create_token(self.body, 30, True)
        body = {"token": token}
        response = client.get("/api/verify", json=body)
        response_body = response.json()
        assert response.status_code == 200
        assert response_body["payload"] == self.body

    def test_invalid_token(self, client):
        body = {"token": "invalidToken"}
        response = client.get("/api/verify", json=body)
        assert response.status_code == 401

    def test_expired_token(self, client):
        tokenizer = Tokenizer()
        token = tokenizer.create_token(self.body, -1, True)
        body = {"token": token}
        response = client.get("/api/verify", json=body)
        assert response.status_code == 401

    def test_no_expire_token(self, client):
        tokenizer = Tokenizer()
        token = tokenizer.create_token(self.body, -1, False)
        body = {"token": token}
        response = client.get("/api/verify", json=body)
        response_body = response.json()
        assert response.status_code == 200
        assert response_body["payload"] == self.body
