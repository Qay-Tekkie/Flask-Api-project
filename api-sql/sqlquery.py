from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    db = sqlite3.connect('posts.db')
    cursor = db.cursor()
    # cursor.execute('CREATE TABLE products(id: INTEGER PRIMARY KEY, item: TEXT NOT NULL, price: TEXT NOT NULL)')
   

    cursor.execute('SELECT * FROM products')
    data = cursor.fetchall()
    db.close()

    return jsonify(data)

@app.route('/create', methods=['POST'])
def create():
    db = sqlite3.connect('posts.db')
    cursor = db.cursor()

    item = request.args.get('item')
    price = request.args.get('price')
    cursor.execute('INSERT INTO products(item, price) VALUES("%s", "%s")' %  (item, price))
    db.commit()

    db.close()
    return 'added succesfully'

@app.route('/update/<_id>', methods=['PUT'])
def update(_id):
    db = sqlite3.connect('posts.db')
    cursor = db.cursor()

    item = request.args.get('item')
    price = request.args.get('price')

    cursor.execute('UPDATE products SET item="%s", price="%s" WHERE id=%s' % (item, price, _id))
    db.commit()

    db.close()
    return jsonify(
        '_id: %s, item: %s, price: %s' % (_id, item, price)
    )


@app.route('/delete/<_id>', methods=['DELETE'])
def delete(_id):
    db = sqlite3.connect('posts.db')
    cursor = db.cursor()

    cursor.execute('DELETE FROM products WHERE id=%s' %  _id)
    db.commit()

    db.close()
    return 'deleted _id: %s' % _id

if __name__ == '__main__':
    app.run(debug=True)
