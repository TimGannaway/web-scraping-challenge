from flask import Flask, render_template

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.store_inventory

# Drops collection if available to remove duplicates
db.produce.drop()

# Creates a collection in the database and inserts two documents
db.produce.insert_many(
    [
	{
    	"type": "apples",
    	"cost": .23,
    	"stock": 333
	}
	,
	{
    	"type": "oranges",
    	"cost": .50,
    	"stock": 334
	}
	,
	{
	"type": "beets",
    	"cost": .24,
    	"stock": 335
	}
	,
	{
	"type": "celery",
    	"cost": .44,
    	"stock": 336
	}
	,
	{
	"type": "grapes",
    	"cost": .12,
    	"stock": 337
	}
    ]
)


# Set route
@app.route('/')
def index():
    # Store the entire team collection in a list
    produce = list(db.produce.find())
    print(produce)

    # Return the template with the teams list passed in
    return render_template('index.html', produce=produce)

if __name__ == "__main__":
    app.run(debug=True)










