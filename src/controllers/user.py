from fastapi import Response, HTTPException, APIRouter
from ..model.schemas import UserBase
from ..dao.crud import User
from neomodel import DoesNotExist, db
from datetime import datetime


router  = APIRouter()

@router.get("/user")
async def get_users():
    return User.nodes.all()


@router.get("/user/{id}")
async def get_users(id: str):
    try:
        return User.nodes.get(unique_id=id)
    except DoesNotExist as e:
        print('Ressource does not exist', e)
    
    except Exception as e:
        print('An error occured', e)


@router.post("/user")
async def create_users(user: UserBase):
    try:
        user_data = User(
            username=user.username,
            email = user.email,
            age=user.age,
            created_at=datetime.now()
        ).save()

    except ValueError as e:
        print("An error with the values passed", e) 
    
    except Exception as e:
        print("Excpetion occured", e) 

    return {"user_id": user_data.unique_id}


@router.put("/user")
async def edit_user(user: UserBase):
    try:
        user_to_update = User.nodes.get(unique_id=user.id)
        user_to_update.username = user.username
        user_to_update.email = user.email
        user_to_update.age = user.age
        user_to_update.created_at = user_to_update.created_at
        user_to_update.updated_at = datetime.now()
        user_to_update.save()

    except ValueError as e:
        print("An error with the values passed", e) 
        raise HTTPException(status_code=400, detail=str(e)) from e
    
    except Exception as e:
        print("Excpetion occured", e) 
        raise HTTPException(status_code=400, detail=str(e)) from e
    
    return Response(status_code=201)
