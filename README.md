# API REST USERS - Case BridgeHub

## Objetivo

Esse projeto tem como objetivo criar uma API RESTful, onde será possível aplicar as operações CRUD na entidade `User`.

## Pré-Requisitos

- Python 3.9

## Pacotes utilizados

- [Flask](https://flask.palletsprojects.com/en/2.1.x/installation/)
- [Flask-RESTX](https://flask-restx.readthedocs.io/en/latest/)
- [Flask-marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)
- [Flask-sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)

## Instalação da Aplicação

Abra o terminal/Powershell e rode os comandos abaixo:

Clonando o repositório:

```
git clone https://github.com/brunosa91/API-REST-Users
```

Entrando na pasta:

```
cd API-REST-Users

```

Instalando os pacotes:

```
py -3 -m venv ven
```

```
venv\Scripts\activate
```

```
pip install Flask
```

```
pip install flask-restx
```

```
pip install flask-marshmallow
```

```
pip install -U Flask-SQLAlchemy
```

Iniciando o servidor:

```
python app.py
```

---

## Para testar a api use o Swagger através da rota /api/doc/

### Users

- **GET /users**

- **GET /users/ < int : id >**

- **POST /add_users**

- **PUT /edit_user/ < int : id >**

- **DELETE /delete_user/ < int : id >**

  Schema da resposta

  ```

          {
              "nome" : <String>,
              "email": <String>,
              "telefone" : <int>
          }

  ```
