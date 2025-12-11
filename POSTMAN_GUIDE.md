# Postman Collection Guide for Assignment Task Tracker API

This guide will help you test the Assignment Task Tracker API using the provided Postman collection.

## Team Members
- Mychal Redoblado (@Ka1ma)
- Kyle Gabriel T. Galanida (KGG-Student)
- Karlos Semilla (@Ykarlossemilla)
- Jhemar Visande (@JhemarVisande)

## Prerequisites

1. **Postman Installed**: Download from [postman.com](https://www.postman.com/downloads/)
2. **Backend Server Running**: Ensure the FastAPI server is running on `http://127.0.0.1:8000`
3. **MongoDB Connected**: Verify MongoDB connection is active

## Quick Start

### Step 1: Import the Collection

1. Open Postman
2. Click the **Import** button (top left)
3. Click **Upload Files**
4. Select `Assignment_Task_Tracker_API.postman_collection.json` from the project root
5. Click **Import**

### Step 2: Verify Collection Variables

1. Click on the collection name in the left sidebar
2. Go to the **Variables** tab
3. Verify these variables are set:
   - `base_url`: `http://127.0.0.1:8000`
   - `access_token`: (empty - will be auto-populated)
   - `task_id`: (empty - will be auto-populated)

## Testing Workflow

### 1. Register a New User

**Endpoint**: `POST /api/auth/register`

**Request Body**:
```json
{
  "email": "mychal.redoblado@example.com",
  "username": "mychalredoblado",
  "password": "password123"
}
```

**Expected Response**: `200 OK`
```json
{
  "message": "User registered successfully"
}
```

**Note**: If the user already exists, you'll get a `400 Bad Request` error. Use a different email to register a new user.

### 2. Login

**Endpoint**: `POST /api/auth/login`

**Request Body**:
```json
{
  "email": "mychal.redoblado@example.com",
  "password": "password123"
}
```

**Expected Response**: `200 OK`
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

**Automatic Action**: The collection automatically saves the `access_token` to the collection variable for use in subsequent requests.

### 3. Create a Task

**Endpoint**: `POST /api/tasks/`

**Headers**: 
- `Authorization: Bearer {{access_token}}` (automatically added)

**Request Body**:
```json
{
  "title": "Complete ITCC14 Final Project",
  "description": "Finish the Assignment Task Tracker API with all team members",
  "completed": false,
  "due_date": "2024-12-31"
}
```

**Expected Response**: `200 OK` or `201 Created`
```json
{
  "id": "507f1f77bcf86cd799439011",
  "title": "Complete ITCC14 Final Project",
  "description": "Finish the Assignment Task Tracker API with all team members",
  "completed": false,
  "due_date": "2024-12-31",
  "owner_email": "mychal.redoblado@example.com",
  "created_at": "2024-12-15T10:30:00"
}
```

**Automatic Action**: The collection automatically saves the `task_id` for use in subsequent requests.

### 4. List All Tasks

**Endpoint**: `GET /api/tasks/`

**Headers**: 
- `Authorization: Bearer {{access_token}}` (automatically added)

**Expected Response**: `200 OK`
```json
{
  "tasks": [
    {
      "id": "507f1f77bcf86cd799439011",
      "title": "Complete ITCC14 Final Project",
      "description": "Finish the Assignment Task Tracker API with all team members",
      "completed": false,
      "due_date": "2024-12-31",
      "owner_email": "mychal.redoblado@example.com",
      "created_at": "2024-12-15T10:30:00"
    }
  ]
}
```

### 5. Get Task Details

**Endpoint**: `GET /api/tasks/{{task_id}}`

**Headers**: 
- `Authorization: Bearer {{access_token}}` (automatically added)

**Expected Response**: `200 OK`
```json
{
  "id": "507f1f77bcf86cd799439011",
  "title": "Complete ITCC14 Final Project",
  "description": "Finish the Assignment Task Tracker API with all team members",
  "completed": false,
  "due_date": "2024-12-31",
  "owner_email": "mychal.redoblado@example.com",
  "created_at": "2024-12-15T10:30:00"
}
```

### 6. Update a Task

**Endpoint**: `PUT /api/tasks/{{task_id}}`

**Headers**: 
- `Authorization: Bearer {{access_token}}` (automatically added)

**Request Body**:
```json
{
  "title": "Complete ITCC14 Final Project - Updated",
  "completed": true
}
```

**Expected Response**: `200 OK`
```json
{
  "message": "Task updated successfully"
}
```

### 7. Delete a Task

**Endpoint**: `DELETE /api/tasks/{{task_id}}`

**Headers**: 
- `Authorization: Bearer {{access_token}}` (automatically added)

**Expected Response**: `204 No Content`

## Troubleshooting

### Issue: "Internal Server Error" on Register/Login

**Solution**: 
1. Check if MongoDB is running: `pgrep -fl mongod`
2. Verify MongoDB connection string in `app/config.py`
3. Check backend server logs for detailed error messages

### Issue: "Unauthorized" Error on Task Endpoints

**Solution**:
1. Ensure you've run the Login request first
2. Check that the `access_token` variable is populated (Collection > Variables tab)
3. Verify the token hasn't expired (tokens expire after 30 minutes)

### Issue: "Task not found" Error

**Solution**:
1. Ensure you've created a task first
2. Check that the `task_id` variable is populated (Collection > Variables tab)
3. Verify you're using the correct task ID for your user

### Issue: Cannot Connect to Server

**Solution**:
1. Verify the backend server is running: `curl http://127.0.0.1:8000/`
2. Check if port 8000 is in use: `lsof -ti:8000`
3. Start the server: `uvicorn app.main:app --reload --host 127.0.0.1 --port 8000`

## Testing Different Scenarios

### Test Case 1: Complete User Journey
1. Register → Login → Create Task → List Tasks → Update Task → Delete Task

### Test Case 2: Authentication Errors
1. Try to access task endpoints without logging in (should get 401 Unauthorized)
2. Try to login with wrong password (should get 401 Unauthorized)
3. Try to register with existing email (should get 400 Bad Request)

### Test Case 3: Task Management
1. Create multiple tasks
2. List all tasks
3. Update specific tasks
4. Delete specific tasks
5. Verify tasks are properly filtered by user

### Test Case 4: Data Validation
1. Try to create task with missing required fields
2. Try to create task with invalid date format
3. Try to update task with invalid data

## Advanced Usage

### Using Different Users

To test with multiple users:
1. Change the email in the Register request
2. Run Register → Login sequence
3. Create tasks for this user
4. Verify tasks are isolated per user

### Customizing the Base URL

If your server runs on a different host/port:
1. Click on the collection name
2. Go to Variables tab
3. Change `base_url` to your server address (e.g., `http://localhost:3000`)

### Exporting Test Results

1. Run all requests in sequence
2. Click on the collection name
3. Click "Run" to open Collection Runner
4. Select all requests
5. Click "Run Assignment Task Tracker API"
6. Export results for documentation

## Tips for Effective Testing

1. **Use the Collection Runner**: Test all endpoints in sequence automatically
2. **Check Response Times**: Monitor API performance in the response section
3. **Validate Responses**: Use Postman's Tests tab to add automated validations
4. **Save Examples**: Save successful responses as examples for documentation
5. **Use Environments**: Create separate environments for development, staging, and production

## Support

For issues or questions:
- Check the main README.md for setup instructions
- Review the API documentation at http://127.0.0.1:8000/docs
- Contact team members listed at the top of this guide

## Additional Resources

- [Postman Documentation](https://learning.postman.com/docs/getting-started/introduction/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [MongoDB Documentation](https://docs.mongodb.com/)
