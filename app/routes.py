from flask import Flask, jsonify, request 
 
app = Flask('__name__') 
 
products = [{'title': 'matooke', 'price': 'Ugx 15000', 'product_id': 1}, {'title': 'Cassava', 'price': 'Ugx 2000', 'product_id': 2}, {'title': 'Rice', 'price': '200', 'product_id': 3}] 

records = [{'Record1' : 'Benjamin bought matooke on 24 11 2018', 'salesID': 1}, {'Record2' : 'Arafat bought Rice on 02 11 2018', 'salesID': 2}] 

@app.route('/products', methods=['POST']) 
def add_product(): 
    data = request.get_json() 
    title = data.get("title") 
    price = data.get("price") 
    product_id = data.get("product_id") 
 
    if price and title: 
        return jsonify({"message": "product added"}) 
    else: 
        return jsonify({"message": "Product not added"}) 
 
@app.route('/products', methods=['GET'])
def returnAll():
    return jsonify({'products': products})

@app.route('/products/<int:product_id>', methods=['GET'])
def returnOne(product_id):
   product = [product for product in products if product['product_id'] == product_id]
   return jsonify({'product': product[0]})
 
 
@app.route('/sales', methods=['GET'])
def returnAllSales():
    return jsonify({'sales': records})

@app.route('/sales/<int:salesID>', methods=['GET'])
def returnOneSale(salesID):
   sale = [sale for sale in records if sale['salesID'] == salesID]
   return jsonify({'product': sale[0]})
 
@app.route('/sales', methods=['POST'])
def add_sales(): 
    data = request.get_json() 
    sales = data.get("sales") 
    record = data.get("record") 
    salesID = data.get("salesID")         
 
    if sales and record: 
        return jsonify({"message": "This Sales Record has been added"}) 
    else: 
        return jsonify({"message": "Opps..!!! This record has not been added"}) 