# pdnStudent
A private API for student profile management

<img alt="GitHub Pipenv locked dependency version" src="https://img.shields.io/github/pipenv/locked/dependency-version/DrMadhushan/pdnStudent/fastapi"> 
<img alt="GitHub Pipenv locked dependency version" src="https://img.shields.io/github/pipenv/locked/dependency-version/DrMadhushan/pdnStudent/uvicorn?color=blue&logoColor=blue"> 
<img alt="GitHub Pipenv locked dependency version" src="https://img.shields.io/github/pipenv/locked/dependency-version/DrMadhushan/pdnStudent/pymongo?color=g&logoColor=blue">


Create virtual env

    virtualenv fastApiVenv

Activate v.env

    source fastApiVenv/bin/activate

Install packages

    pin install <package name>

["https://realpython.com/fastapi-python-web-apis/](FastAPI, uvicorn[standard], pymongo, motor==2.5.1 )

For asynchronous test

```pytest, httpx, trio, twisted, pytest-asyncio, pytest-trio, anyio, pytest-twisted, pytest-tornasync```

```python-multipart (for Form)```

```pyjwt, passlib```

To run the fast Api programm

    uvicorn main:app --reload

