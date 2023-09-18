from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from flask import Flask
from flask_restful import Api, request
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)


SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger.json'  # Our API url (can of course be a local resource)
api = Api(app)
# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)
app.register_blueprint(swaggerui_blueprint)

fake_database = {'users': [
    {
        "id": 1,  # тут тип данных - число
        "name": "Anna",  # тут строка
        "nick": "Anny42",  # и тут
        "balance": 15300  # а тут float
    },

    {
        "id": 2,  # у второго пользователя
        "name": "Dima",  # такие же
        "nick": "dimon2319",  # типы
        "balance": 160.23  # данных
    }
    , {
        "id": 3,  # у третьего
        "name": "Vladimir",  # юзера
        "nick": "Vova777",  # мы специально сделаем
        "balance": "25000"  # нестандартный тип данных в его балансе
    },
    {
        "id": 4,
        "name": "Maria",
        "nick": "Mary",
        "balance": 0
    }
], }


@app.route('/hello', methods=['GET'])
def get_hello():
    return 'Hello user'


@app.route('/get_info_by_user_id/{id:int}', methods=['GET'])
def get_info_about_user(id: int=-1):
    return fake_database['users'][id - 1]


@app.route('/get_user_balance_by_id/{id:int}', methods=['GET'])
def get_user_balance(id: int=-1):
    return fake_database['users'][id - 1]['balance']


@app.route('/get_name/{name}', methods=['GET'])
def get_name(name):
    for i in fake_database['users']:
        if i['name'] == name:
            return i


@app.route('/get_names', methods=['GET'])
def get_names():
    count = 0
    result = []
    try:
        for i in fake_database['users']:
            result.append(f"number - {count}: {i['name']}")
            count += 1
        return result
    except:
        return {404: 'Not Found'}

@app.route('/get_total_balance',methods=['GET'])
def get_total_balance():
    total_balance: float = 0.0
    for user in fake_database['users']:
        total_balance += user['balance']
    return total_balance


@app.route('/gets', methods=['GET'])
def gets(skip: int = 0, limit: int = 0):
    return fake_database['users'][skip:skip + limit]


@app.route('/deluser/{user_id}', methods=['DELETE'])
def deluser(user_id: int=-1):
    for index, u in enumerate(fake_database[
                                  'users']):  # так как в нашей бд юзеры хранятся в списке, нам нужно найти их индексы внутри этого списка
        if u['id'] == user_id:
            del fake_database['users'][index]
        return fake_database['users']




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
#