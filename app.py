from flask import Flask

app = Flask(__name__)

stores=[
    {"name": "My Stores",
     "item":[{
         "name": "Chairs",
         "price": 45.00
     }]
    }
]

@app.get("/store")
def get_stores():
    return{"stores": stores}