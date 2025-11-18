from fastapi import APIRouter, Header, HTTPException, status
from app.schemas.task_schema import TaskCreate, TaskUpdate
from app.models.task_model import create_task, get_tasks_by_owner, update_task, delete_task
from app.utils.auth import get_current_user

router = APIRouter(prefix="/api/tasks", tags=["Tasks"])

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_new_task(task: TaskCreate, authorization: str = Header(...)):
    user_email = get_current_user(authorization.split(" ")[1])
    task_data = task.dict()
    task_data["owner_email"] = user_email
    task_id = await create_task(task_data)
    return {"id": task_id, "message": "Task created successfully"}

@router.get("/", status_code=status.HTTP_200_OK)
async def list_my_tasks(authorization: str = Header(...)):
    user_email = get_current_user(authorization.split(" ")[1])
    tasks = await get_tasks_by_owner(user_email)
    if not tasks:
        return {"tasks": [], "message": "No tasks found."}
    return {"tasks": tasks}

@router.get("/{task_id}", status_code=status.HTTP_200_OK)
async def get_my_task(task_id: str, authorization: str = Header(...)):
    user_email = get_current_user(authorization.split(" ")[1])
    tasks = await get_tasks_by_owner(user_email)
    task = next((t for t in tasks if str(t.get("id")) == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found or unauthorized")
    return {"task": task}

@router.put("/{task_id}", status_code=status.HTTP_200_OK)
async def update_my_task(task_id: str, task: TaskUpdate, authorization: str = Header(...)):
    user_email = get_current_user(authorization.split(" ")[1])
    updated = await update_task(task_id, task.dict(exclude_unset=True), user_email)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found or unauthorized")
    return {"message": "Task updated successfully"}

@router.delete("/{task_id}", status_code=status.HTTP_200_OK)
async def delete_my_task(task_id: str, authorization: str = Header(...)):
    user_email = get_current_user(authorization.split(" ")[1])
    deleted = await delete_task(task_id, user_email)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found or unauthorized")
    return {"message": "Task deleted successfully"}
