from fastapi import FastAPI

app = FastAPI()

#Creating developer API with POST method
@app.post("/developers/")
def create_developer(developer: Developer):
    return {"message": "Developer created successfully", developer}