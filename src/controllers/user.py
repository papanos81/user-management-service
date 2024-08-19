from fastapi import Response, HTTPException, APIRouter, status
from ..model.schemas import UserBase
from ..dao.user_entities import User
from neomodel import DoesNotExist, db
from datetime import datetime


router  = APIRouter()

@router.get("/user", status_code=status.HTTP_200_OK)
async def get_users():
    return User.nodes.all()

@router.get("/user/{username}", status_code=status.HTTP_200_OK)
async def get_users(username: str):
    try:
        return User.nodes.get(username=username)
    
    except DoesNotExist as e:
        print('Ressource does not exist', e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=str(e)) from e
    
    except Exception as e:
        print('An error occured', e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=str(e)) from e

@router.get("/user/{id}", status_code=status.HTTP_200_OK)
async def get_users(id: str):
    try:
        return User.nodes.get(unique_id=id)
    
    except DoesNotExist as e:
        print('Ressource does not exist', e)  
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=str(e)) from e
    except Exception as e:
        print('An error occured', e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=str(e)) from e


@router.post("/user", status_code=status.HTTP_201_CREATED)
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
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=str(e)) from e

    except Exception as e:
        print("Check Excpetion occured", e) 
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=str(e)) from e

    return {"user_id": user_data.unique_id}


@router.put("/user", status_code=status.HTTP_201_CREATED)
async def edit_user(user: UserBase):
    try:
        user_to_update = User.nodes.get(username=user.username)
        user_to_update.username = user.username
        user_to_update.email = user.email
        user_to_update.age = user.age
        user_to_update.created_at = user_to_update.created_at
        user_to_update.updated_at = datetime.now()
        user_to_update.save()

        print(type(user_to_update.updated_at))
    except ValueError as e:
        print("An error with the values passed", e) 
        raise HTTPException(status_code=400, detail=str(e)) from e
    
    except Exception as e:
        print("Excpetion occured", e) 
        raise HTTPException(status_code=400, detail=str(e)) from e  
    return user_to_update

@router.delete("/user/{id}", status_code=status.HTTP_202_ACCEPTED)
async def delete_user_by_id(id: str):
    try:
        user = User.nodes.get(unique_id=id)
        user.delete()
    
    except DoesNotExist as e:
        print('Ressource does not exist', e)
        raise HTTPException(status_code=400, detail=str(e)) from e

    except Exception as e:
        print('An error occured', e)
        raise HTTPException(status_code=400, detail=str(e)) from e
