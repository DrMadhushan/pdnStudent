from fastapi.testclient import TestClient
from main import app
import pytest
from httpx import AsyncClient

# client = TestClient(app)

@pytest.mark.anyio
async def test_pathDoesntExist():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/randomPath")
    # response = client.get("/randomPath")
    assert response.status_code == 404
    assert response.json() == { "detail": "Not Found" }

@pytest.mark.anyio
async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    # response = await client.get("/")
    assert response.status_code == 200
    assert response.json() == { "message": "No Functionality" }

@pytest.mark.anyio
async def test_getStudents():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/students")
    # response = await client.get("/students")
    assert response.status_code == 200
    assert response.json()[0]["name"] == "Ruwan"

@pytest.mark.anyio
async def test_getStudentInfo():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/student/view/E17064")
    # response = await client.get("/student/view/E17194")
    status = response.status_code
    assert response.status_code == 200
    assert response.json()["name"] == "Dushintha"

@pytest.mark.anyio
async def test_updateStudentInfo():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        test_user_before = await ac.get("/student/view/E17194")
        response = await ac.put("/student/edit/E17194", data={'new_name': "New User Name"})
        test_user_after = await ac.get("/student/view/E17194")
    
    async with AsyncClient(app=app, base_url="http://test") as ac:
        await ac.put("/student/edit/E17194", data={'new_name': test_user_before.json()["new_name"]})
    
    assert response.status_code == 200
    assert test_user_after.json()["new_name"] == "New User Name"

@pytest.mark.anyio
async def test_getAllProfileUpdateRequests():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/controls/admin/profile_updates")
    
    assert response.status_code == 200
    assert response.json()[0]["roll_no"] == "E17194"