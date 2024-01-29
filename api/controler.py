from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_production():
    return {"get": "Teste"}