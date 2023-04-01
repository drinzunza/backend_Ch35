from flask import Flask
import json
from about import me
from data import mock_data

app = Flask(__name__) # create a instance of Flask class

###################################################
##### WEB SERVER ##########
###################################################
@app.get("/")
def home():
    return "Hello World from a flask server"


@app.get("/test")
def test():
    return "This is a test page"




###################################################
############ API SERVER ###########################
###################################################

@app.get("/api/version")
def version():
    return json.dumps("1.0")


@app.get("/api/about")
def about():
    return json.dumps(me)


# get /api/developer/name
# return the full name of the developer plus the email
# eg. Sergio Inzunza -- sinzunza@sdgku.edu
@app.get("/api/developer/name")
def dev_name():
    name = me["name"]
    last = me["last_name"]
    email = me["email"]
    response = f"{name} {last} -- {email}"
    return json.dumps(response)

    # return json.dumps(f"{me["name"]} {me["last_name"]} -- {me["email"]}")


@app.get("/api/catalog")
def get_catalog():
    return json.dumps(mock_data)


# get /api/products/count
# return the number of products in the catalog
@app.get("/api/products/count")
def products_count():
    count = len(mock_data)
    return json.dumps(count)




# get /api/products/total
# return the sum of all prices in the catalog
@app.get("/api/products/total")
def sum_prices():
    total = 0
    for product in mock_data:
        price = product["price"]
        total =  total + price

    print(total) # show the result on the terminal
    return json.dumps(total)



@app.get("/api/categories")
def categories():
    cats = []
    for prod in mock_data:
        category = prod["category"]

        # if category does not exist inside the list
        if category not in cats:
            cats.append(category)

    return json.dumps(cats)




@app.get("/api/catalog/<category>")
def products_by_category(category):
    results = []
    for prod in mock_data:
        if prod["category"].lower() == category.lower():
            results.append(prod)

    return json.dumps(results)



# should return all the produces whose price is lower than price var
@app.get("/api/products/lower/<price>")
def products_lower_price(price):
    fixed_price = float(price)
    results = []
    for prod in mock_data:
        if prod["price"] < fixed_price:
            results.append(prod)

    return json.dumps(results)



# /api/products/greater/<price>
# prices greater OR EQUAL
@app.get("/api/products/greater/<price>")
def products_greater_price(price):
    fixed_price = float(price)
    results = []
    for prod in mock_data:
        if prod["price"] >= fixed_price:
            results.append(prod)

    return json.dumps(results)



# /api/products/search/<term>
# search must be case insensitive
@app.get('/api/products/search/<term>')
def search_products(term):
    results = []
    for prod in mock_data:
        if term.lower() in prod["title"].lower():
            results.append(prod)

    return json.dumps(results)



# start the server
app.run(debug=True)