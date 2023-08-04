from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return{"message":"Hola, bienvenido a mi API de saludos"}

@app.get("/saludar/{nombre}")
def saludar(nombre:str):
    return{"mensaje":f"Hola {nombre}"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)