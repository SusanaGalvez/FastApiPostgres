from fastapi import FastAPI,Response
from starlette.status import HTTP_200_OK,HTTP_201_CREATED,HTTP_204_NO_CONTENT
from model.user_connection import UserConnection
from schema.user_schena import UserSchema

app= FastAPI()
conn= UserConnection()

@app.get("/",status_code=HTTP_200_OK)
def get_all():
    # Este mensajito lo puso primero antes de hacer nada para ver que el servidor iba bién
    #return "Hi , I an FastAPI"
    return conn.read_all()
    '''
    items = []
    #Con este FOR nos sale en consola linea por linea los datos y le damos formato
    for data in conn.read_all():
        dictionary = {}
        dictionary["id"]=data[0]
        dictionary["name"]=data[1]
        dictionary["phone"]=data[2]
        items.append(dictionary)
        return items
        #print(data)
    '''


@app.get("/api/user/{id}",status_code=HTTP_200_OK)
def get_one(id:str):
    dictionary= {}
    data = conn.read_one(id)
    dictionary["id"] = data[0]
    dictionary["name"] = data[1]
    dictionary["phone"] = data[2]
    return dictionary


@app.post("/api/insert",status_code=HTTP_201_CREATED)
def insert(user_data:UserSchema):
    #Se manda en formato de diccionario de python
    data=user_data.dict()
    #Para quitar el dato id
    data.pop("id")
    print(data)
    #Metodo de la conexión para escribir
    conn.write(data)
    return Response(status_code=HTTP_201_CREATED)


@app.put("/api/update/{id}",status_code=HTTP_204_NO_CONTENT)
def update(user_data:UserSchema,id:str):
    # Se manda en formato de diccionario de python
    data = user_data.dict()
    data["id"] =id
    conn.update(data)
    #print(data)
    return Response(status_code=HTTP_204_NO_CONTENT)



@app.delete("/api/delete/{id}",status_code=HTTP_204_NO_CONTENT)
def delete(id:str):
    conn.delete(id)
    return Response(status_code=HTTP_204_NO_CONTENT)