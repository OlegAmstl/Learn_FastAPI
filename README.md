# Learn_FastAPI

```commandline
poetry init
```
Запускаем виртуальное окружение
```commandline
poetry shell
```
## Установка FastAPI
```commandline
poetry add fastapi
```
Так же понадобится установить uvicorn - это модуль для запуска приложений.
```commandline
poetry add uvicorn
```

Запуск приложения с помощью uvicorn
```commandline
uvicorn api:app --port 8080 --reload
```

Роутинг осуществляется с помощью класса APIRouter
```commandline
from fastapi import APIRouter
```
Запуск приложения с помощью uvicorn
```commandline
uvicorn api:app --port 8080 --reload
```
Роутинг осуществляется с помощью класса APIRouter
```commandline
from fastapi import APIRouter
```


## Установка и работа с Jinja2
```commandline
poetry add jinja2
```
```commandline
mkdir tamplates
touch base.html
```
```commandline
from fastapi.templating import Jinja2Templates
```