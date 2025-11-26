#!/usr/bin/env python
# coding: utf-8


# In[6]:


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from FastAPI!"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}!"}

@app.post("/sum")
def sum_numbers(a: int, b: int):
    return {"result": a + b}


