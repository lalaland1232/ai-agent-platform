from fastapi.testclient import TestClient
from main import app
def test_here():
    client = TestClient(app)
    token = client.post("/login",json={"email":"shiv31desaiis@gmail.com","password":"12345678"}).json()["access_token"]
    response=client.get("/agents_by_user",headers={"Authorization":f"Bearer {token}"})
    assert response.status_code==200
    assert response.json()=={}