# pdnStudent
A private API for student profile management

<div style="display: flex; flex-flow: row wrap; justify-content: center; ">
<img style="padding-right:5px; padding-bottom:5px" alt="GitHub Pipenv locked dependency version" src="https://img.shields.io/github/pipenv/locked/dependency-version/DrMadhushan/pdnStudent/fastapi"> 
<img style="padding-right:5px; padding-bottom:5px" alt="GitHub Pipenv locked dependency version" src="https://img.shields.io/github/pipenv/locked/dependency-version/DrMadhushan/pdnStudent/uvicorn?color=blue&logoColor=blue"> 
<img style="padding-right:5px; padding-bottom:5px" alt="GitHub Pipenv locked dependency version" src="https://img.shields.io/github/pipenv/locked/dependency-version/DrMadhushan/pdnStudent/pymongo?color=g&logoColor=blue">

<img style="padding-right:5px; padding-bottom:5px" alt="GitHub Pipenv locked dependency version" src="https://img.shields.io/github/pipenv/locked/dependency-version/DrMadhushan/pdnStudent/python-multipart"> 
<img style="padding-right:5px; padding-bottom:5px" alt="GitHub Pipenv locked dependency version" src="https://img.shields.io/github/pipenv/locked/dependency-version/DrMadhushan/pdnStudent/pyjwt?color=blue&logoColor=blue"> 
<img style="padding-right:5px; padding-bottom:5px" alt="GitHub Pipenv locked dependency version" src="https://img.shields.io/github/pipenv/locked/dependency-version/DrMadhushan/pdnStudent/passlib?color=g&logoColor=blue">
</div>
<div style="display: flex; flex-flow: row wrap; justify-content: center;">
<img alt="GitHub Pipenv locked dependency version" src="https://img.shields.io/github/pipenv/locked/dependency-version/DrMadhushan/pdnStudent/dev/pytest?color=g&logoColor=blue">
</div>
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

