from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import pandas as pd
import pprint as pp
import json

app = FastAPI()

# my_dict = {
#     "id": "123456789",
#     "store": "Brussels",
#     "date": "2020-01-01",
#     "products": [
#         {
#             "id": "123456789",
#             "name": "Banana",
#             "price": 1.5
#         },
#         {
#             "id": "123456789",
#             "name": "Bread",
#             "price": 1.5
#         },
#         {
#             "id": "123456789",
#             "name": "Water",
#             "price": 1.5
#         }
#     ]
# }
@app.get("/")
async def root():
    return {'message':'Hello World'}
@app.post('/data')
async def getPriceandproduct():
    file = open('database.json')
    #return {'message':'Hello World'}
    return json_load(file)

# # def price(dict):
# #     df=pd.DataFrame([dict])
# #     pp.pprint(df)
#     df.describe()
# return price[0]

# @app.post("/data")
# async def data(user_data: my_dict):
#     return {'message': 'Hello World2'}
    # print(user_data)
    # # TODO: send data to the queue
    # # which proportion of the products are Fruits, Bakery or Drinks
    # # average price
    # # average price of the products per store
    # return {"status": "ok"}

# filename = 'database.json'
# with open(filename, 'w') as file_object:
#  json.dump(data, file_object)
#
#  json.load(file_object)

#data(my_dict)
