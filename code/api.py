from flask import Flask, request
from flask_restful import Api, Resource
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
api = Api(app)

app.secret_key = 'andres'

jwt = JWT(app, authenticate, identity)

items = []


class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name']==name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name']==name, items), None):
            return {'mesage': f'Item {name} already exist, can\'t be created, duplication is not allowed!'}
            
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201


class ItemList(Resource):
    def get(self):
        return {'Item list': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')


if __name__ == "__main__":
    app.run(port=9897, debug=True) 