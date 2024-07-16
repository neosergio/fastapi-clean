from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)



# Todo: Implement tests with moto
def test_create_todo():
    response = client.post("/api/v1/todos/", json={'title': 'Test Todo', 'description':'This is a test todo'})
    assert response.status_code == 200
    assert response.json()['title'] == "Test Todo"
