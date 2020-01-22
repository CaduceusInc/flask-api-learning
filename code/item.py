import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True, help="This field cannot be left blank"
                        )

@jwt_required
def get(self, name):
    item = self.find_by_name(name)
    if item:
        return item
    return {'message': 'Item not found'}, 404

@classmethod
def find_by_name(cls, name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    query = "SELECT * from items WHERE name=?"
    result = cursor.execute(query, (ame,))
    row = result.fetchone()
    connection.close()

    if row:
        return {'item': {'name': row[0], 'price': row[1]}}


def post(self, name):
    if self.find_by_name(name):
        return {'message': "An item with name '{}' already exists.".format(name)}, 400

    data = Item.parser.parse_args()

    item = {'name': name, 'price': data['price']}

    try:
        self.insert(item)
    except:
        return {'message:' "An error occured when trying to insert the item"}, 500

    return item, 201


@classmethod
def insert(cls, name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    query = "INSERT INTO items VALUES (?,?)"
    cursor.execute(query, (item['name'], item['price']))

    connection.commit()
    connection.close()


def delete(self, name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    query = "DELETE FROM items WHERE name=?"
    cursor.execute(query, (name,))

    connection.commit()
    connection.close()

    return {'message': "Item deleted"}


def put(self, name):
    data = 
















