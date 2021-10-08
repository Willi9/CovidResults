# The username and password are incorrect for safety reasons
# This file shows how I inserted to MongoDB
from pymongo import MongoClient
import pandas as pd

username = 'admin'
password = '*************'

# Connecting to my Mongo data base
client = MongoClient(
    "mongodb+srv://%s:%s@covidanalysisproject.rehjp.mongodb.net/covidDB?retryWrites=true&w=majority"
    % (username, password))

# Getting the data base and collections that I will read into
db = client.covidDB
collection = db.RacialData

# Using pandas I am going to read the CSV data into a data frame
df = pd.read_csv('CRDT Data - CRDT.csv')   # loading csv file

# Converting the data frame into a dictionary that I can upload to the Database
data = df.to_dict('records')

# Uploading the data into my database
collection.insert_many(data)



