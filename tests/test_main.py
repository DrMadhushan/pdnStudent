"""Test Module."""
import pytest
from httpx import AsyncClient

from main import app

# client = TestClient(app)


@pytest.mark.anyio
async def test_path_doesnt_exist():
    """_summary."""
    async with AsyncClient(app=app, base_url="http://test") as a_c:
        response = await a_c.get("/randomPath")
    # response = client.get("/randomPath")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}


@pytest.mark.anyio
async def test_root():
    """_summary."""
    async with AsyncClient(app=app, base_url="http://test") as a_c:
        response = await a_c.get("/")
    # response = await client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "No Functionality"}


@pytest.mark.anyio
async def test_get_students():
    """_summary."""
    async with AsyncClient(app=app, base_url="http://test") as a_c:
        response = await a_c.get("/students")
    # response = await client.get("/students")
    assert response.status_code == 200
    assert response.json()[0]["name"] == "Ruwan"


@pytest.mark.anyio
async def test_get_student_info():
    """_summary."""
    async with AsyncClient(app=app, base_url="http://test") as a_c:
        response = await a_c.get("/student/view/E17064")
    # response = await client.get("/student/view/E17194")
    # status = response.status_code
    assert response.status_code == 200
    assert response.json()["name"] == "Dushintha"


@pytest.mark.anyio
async def test_update_student_info():
    """_summary."""
    async with AsyncClient(app=app, base_url="http://test") as a_c:
        test_user_before = await a_c.get("/student/view/E17194")
        response = await a_c.put(
            "/student/edit/E17194", data={"new_name": "New User Name"}
        )
        test_user_after = await a_c.get("/student/view/E17194")

    async with AsyncClient(app=app, base_url="http://test") as a_c:
        await a_c.put(
            "/student/edit/E17194",
            data={"new_name": test_user_before.json()["new_name"]},
        )

    assert response.status_code == 200
    assert test_user_after.json()["new_name"] == "New User Name"


@pytest.mark.anyio
async def test_get_all_profile_update_requests():
    """_summary."""
    async with AsyncClient(app=app, base_url="http://test") as a_c:
        response = await a_c.get("/controls/admin/profile_updates")

    assert response.status_code == 200
    assert response.json()[0]["roll_no"] == "E17194"
