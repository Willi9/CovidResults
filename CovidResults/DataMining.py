from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt
from pymongo import MongoClient
import pandas as pd

username = 'GUEST'
password = '12345'

# Connecting the Mongo Database
client = MongoClient(
    "mongodb+srv://%s:%s@covidanalysisproject.rehjp.mongodb.net/covidDB?retryWrites=true&w=majority"
    % (username, password))

# Connecting to the database and collection
db = client.covidDB
collection = db.RacialData

# Querying all the data from colorado from 2020-04-12 to 2021-03-7
coloradoQuery = {"State": "CO"}

# Converting the data into a dataframe to work with it easier.
data = pd.DataFrame(list(collection.find(coloradoQuery)))
data.set_index("_id", inplace=True)

# Getting the latest data
summation = data.iloc[0]

# Printing the information for the March 7th, 2021.
pprint(summation)

# Creating the numpy array that we will use for the case numbers pie chart
caseNumbers = np.array([summation["Cases_White"], summation["Cases_Black"], summation["Cases_Latinx"],
                        summation["Cases_Asian"], summation["Cases_AIAN"], summation["Cases_NHPI"],
                        summation["Cases_Multiracial"], summation["Cases_Other"], summation["Cases_Unknown"]])

# Creating the key that will also show the percentages
cases_labels = [
    "White - " + str(round(100 * (summation["Cases_White"] / summation["Cases_Total"]), 2)) + "%",
    "Black - " + str(round(100 * (summation["Cases_Black"] / summation["Cases_Total"]), 2)) + "%",
    "Latinx - " + str(round(100 * (summation["Cases_Latinx"] / summation["Cases_Total"]), 2)) + "%",
    "Asian - " + str(round(100 * (summation["Cases_Asian"] / summation["Cases_Total"]), 2)) + "%",
    "AIAN - " + str(round(100 * (summation["Cases_AIAN"] / summation["Cases_Total"]), 2)) + "%",
    "NHPI - " + str(round(100 * (summation["Cases_NHPI"] / summation["Cases_Total"]), 2)) + "%",
    "Multiracial - " + str(round(100 * (summation["Cases_Multiracial"] / summation["Cases_Total"]), 2)) + "%",
    "Other - " + str(round(100 * (summation["Cases_Other"] / summation["Cases_Total"]), 2)) + "%",
    "Unknown - " + str(round(100 * (summation["Cases_Unknown"] / summation["Cases_Total"]), 2)) + "%"
]

# Creating a numpy array that we will use for the death percentages  pie chart
deathNumbers = np.array([summation["Deaths_White"], summation["Deaths_Black"], summation["Deaths_Latinx"],
                         summation["Deaths_Asian"], summation["Deaths_AIAN"], summation["Deaths_NHPI"],
                         summation["Deaths_Multiracial"], summation["Deaths_Other"], summation["Deaths_Unknown"]])

# Creating the key that will also show the percentages
death_labels = [
    "White - " + str(round(100 * (summation["Deaths_White"] / summation["Deaths_Total"]), 2)) + "%",
    "Black - " + str(round(100 * (summation["Deaths_Black"] / summation["Deaths_Total"]), 2)) + "%",
    "Latinx - " + str(round(100 * (summation["Deaths_Latinx"] / summation["Deaths_Total"]), 2)) + "%",
    "Asian - " + str(round(100 * (summation["Deaths_Asian"] / summation["Deaths_Total"]), 2)) + "%",
    "AIAN - " + str(round(100 * (summation["Deaths_AIAN"] / summation["Deaths_Total"]), 2)) + "%",
    "NHPI - " + str(round(100 * (summation["Deaths_NHPI"] / summation["Deaths_Total"]), 2)) + "%",
    "Multiracial - " + str(round(100 * (summation["Deaths_Multiracial"] / summation["Deaths_Total"]), 2)) + "%",
    "Other - " + str(round(100 * (summation["Deaths_Other"] / summation["Deaths_Total"]), 2)) + "%",
    "Unknown - " + str(round(100 * (summation["Deaths_Unknown"] / summation["Deaths_Total"]), 2)) + "%"
]

# Creating cases numbers pie chart plots
plt.subplot(211)
plt.title("Colorado Covid Case Percentages Numbers by Race March 7, 2021")
plt.pie(caseNumbers)
plt.legend(cases_labels, bbox_to_anchor=(0, 1), loc="upper right", fontsize="small")

# Creating death numbers pie charts
plt.subplot(212)
plt.title("Colorado Covid Death Percentages Numbers by Race March 7, 2021")
plt.pie(deathNumbers)
plt.legend(death_labels, bbox_to_anchor=(.9, 1), loc="upper left", fontsize="small")
plt.show()
