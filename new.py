from flask import Flask, request, jsonify

app = Flask(__name__)

PRODUCTS = [
     {'itemNo': '1', 'Item': 'Milk', 'Price': '$30'},
     {'itemNo': '2', 'Item': 'Cheese', 'Price': '$50'}
    ]

@app.route('/')
def home(): 
    return 'Heloo'

@app.route('/products', methods=['GET'])
def get_all():
    return jsonify({'items': PRODUCTS})


@app.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
       each_item = [item for item in PRODUCTS if (item['itemNo'] == product_id)]    
       return jsonify({'item': each_item})

@app.route('/products/<product_id>', methods=['PUT'])
def update_items(product_id):
    update = [item for item in PRODUCTS if (item['itemNo'] == product_id)]

    if 'Item' in request.json:
        update[0]['Item'] = request.json['Item']

    if 'Price' in request.json:
        update[0]['Price'] = request.json['Price']
    return jsonify({'item': update[0]})

@app.route('/products', methods=['POST'])
def create_item():

    data = {
        'itemNo': request.json['itemNo'],
        'Item': request.json['Item'],
        'Price': request.json['Price']
        }
    PRODUCTS.append(data)
    return jsonify(data)

@app.route('/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    del_item = [item for item in PRODUCTS if (item['itemNo'] == product_id)]

    if len(del_item) == 0:
        abort(404)

    PRODUCTS.remove(del_item[0])
    return jsonify({'response': 'Delete Successful'})

if __name__ == '__main__':
    app.run(debug=True)

