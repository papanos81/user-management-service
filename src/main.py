from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/")
async def create_users():
    pass





#Get Users

#Create Users

#Modify User

#Delete User (this will be treated separately as we need to consider archivign data for GDPR and certain amount of time)

