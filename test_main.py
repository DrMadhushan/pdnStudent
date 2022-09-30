from time import sleep
from urllib import response
from fastapi.testclient import TestClient
from main import app
import ast
from httpx import AsyncClient
import asyncio
import pytest

client = TestClient(app)
# pytest_plugins = ('pytest_asyncio',)

def test_pathDoesntExist():
    response = client.get("/randomPath")
    assert response.status_code == 404
    assert response.json() == { "detail": "Not Found" }

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == { "message": "No Functionality" }

def test_getStudents():
    response = client.get("/students")
    assert response.status_code == 200
    assert response.json()[0]["name"] == "Ruwan"

def test_getStudentInfo():
    r1 = client.get("/students/E17194")
    r2 = client.get("/Engineering/students/E17194")
    r3 = client.get("/Engineering/Computer Engineering/students/E17194")
    # sleep(1)
    # print(r1)
    # print(r2)
    # print(r3)
    # await asyncio.sleep(0.5)
    # async with AsyncClient(app=app, base_url="http://test") as ac:
    #     # response = await ac.get("/")
    #     r1 = await ac.get("/students/E17194")
    #     await asyncio.sleep(0.5)
        
    # assert response.status_code == 200

    assert r1.status_code == 200 

    # assert r1.json()["faculty"] == r2.json()["faculty"] == r3.json()["faculty"] == "Engineering"
    # assert r1.json()["department"] == r2.json()["department"] == r3.json()["department"] == "Computer Engineering" 


