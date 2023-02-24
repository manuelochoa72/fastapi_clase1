from fastapi import FastAPI
from pydantic import BaseModel

applicacion=FastAPI()

class Persona(BaseModel):
    nombre:str
    edad:int

fakedata= {
    "1":{
        "nombre":"Adan",
        "edad":35
    },
    "2":{
        "nombre":"Eduardo",
        "edad":25
    },
    "3":{
        "nombre":"Maria",
        "edad":31
    }
}

@applicacion.get("/")
def index():
    return{
        "mensaje": "Hola como estas"
    }


@applicacion.get ("/persona")
def get_nombre_edad():
    return fakedata


@applicacion.get("/persona/{id}")
def get_nombre_edad(id: str):
    return fakedata[id]

@applicacion.post("/insert/persona")
def insert_persona(persona:Persona):
    last_id=0
    for id in fakedata.keys():
        last_id=id 

    fakedata[str(int(last_id)+1)]=persona