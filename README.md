# Assignment Task Tracker API

A backend web service built with FastAPI for managing tasks, authentication, and project tracking.
Developed for ITCC14 Web Services Final Project.

## Team Members
- Mychal Redoblado (@Ka1ma) (MychalXU)
- Kyle Gabriel T. Galanida (KGG-Student)
- Karlos Semilla (@Ykarlossemilla)
- Jhemar Visande (@JhemarVisande)

## Project Overview

### Problem Statement
Teams and individuals often struggle to track their daily tasks effectively. This API aims to provide a lightweight system to manage tasks, monitor progress, and maintain accountability.

### Goals
- Implement a secure authentication system using JWT
- Provide CRUD operations for task management
- Ensure a simple and reliable backend for future frontend integration

## API Documentation

### Authentication Endpoints

#### Register User
```
POST /api/auth/register
Content-Type: application/json

{
  "email": "mychal.redoblado@example.com",
  "username": "mychalredoblado",
  "password": "password"
}
```

#### Login User
```
POST /api/auth/login
Content-Type: application/json

{
  "email": "mychal.redoblado@example.com",
  "password": "password"
}
```

Response:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### Task Endpoints

All task endpoints require authentication. Include the JWT token in the Authorization header:
```
Authorization: Bearer <your_jwt_token>
```

#### Create Task
```
POST /api/tasks/
Content-Type: application/json

{
  "title": "Complete ITCC14 Final Project",
  "description": "Finish the Assignment Task Tracker API with all team members",
  "completed": false,
  "due_date": "2024-12-31"
}
```

#### List Tasks
```
GET /api/tasks/
```

Response:
```json
{
  "tasks": [
    {
      "id": "task_id",
      "title": "Task Title",
      "description": "Task description",
      "completed": false,
      "due_date": "2024-12-31",
      "owner_email": "user@example.com",
      "created_at": "2024-11-15T10:00:00"
    }
  ]
}
```

#### Get Task Details
```
GET /api/tasks/{task_id}
```

#### Update Task
```
PUT /api/tasks/{task_id}
Content-Type: application/json

{
  "title": "Complete ITCC14 Final Project - Updated",
  "completed": true
}
```

#### Delete Task
```
DELETE /api/tasks/{task_id}
```

## Setup Instructions

### Backend Setup

1. Clone the repository:
```bash
git clone https://github.com/Ka1ma/Assignment-Task-Tracker-API.git
cd Assignment-Task-Tracker-API
```

2. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install backend dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory:
```
MONGODB_URL=your_mongodb_connection_string
DATABASE_NAME=tasktracker
SECRET_KEY=your_secret_key_here
```

5. Run the backend API:
```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

The API will be available at `http://127.0.0.1:8000`

### Frontend Setup

1. Install frontend dependencies:
```bash
cd frontend
pip install -r requirements.txt
```

2. Run the Streamlit frontend:
```bash
cd frontend
streamlit run app.py
```

The frontend will be available at `http://localhost:8501`

## Application Features

### Backend API Features

- **Authentication**: Secure JWT-based authentication system
- **Task Management**: Complete CRUD operations for tasks
- **API Documentation**: Interactive Swagger UI for testing endpoints
- **MongoDB Integration**: Scalable database solution

### Frontend Features

- **User Authentication**: Registration and login forms with JWT token storage
- **Task Dashboard**: View all tasks with status indicators
- **Task Management**: Create, edit, update status, and delete tasks
- **Responsive Design**: Clean Streamlit UI components
- **Session Management**: Secure token storage and logout functionality

## API Documentation with Swagger

When the backend server is running, visit the Swagger UI for interactive API documentation:

- Swagger UI: http://127.0.0.1:8000/docs

You can test all API endpoints directly from the browser using the Swagger interface.

## Testing the Application

### Using the Streamlit Frontend

The easiest way to test the application is through the Streamlit frontend, which provides a complete user interface for all functionality:

1. Register a new account
2. Login with your credentials
3. Create, view, update, and delete tasks
4. Test error handling with invalid inputs
5. Verify session management by logging out and back in

### Using Postman (for API Testing)

We've included a comprehensive Postman collection for easy API testing.

#### Import the Postman Collection

1. Open Postman
2. Click "Import" button
3. Select the file: `Assignment_Task_Tracker_API.postman_collection.json`
4. The collection will be imported with all endpoints pre-configured

#### Collection Features

- **Automatic Token Management**: Login endpoint automatically saves the JWT token
- **Automatic Task ID Capture**: Create task endpoint saves the task ID for subsequent requests
- **Pre-configured Examples**: All requests include example data using team member names
- **Environment Variables**: Uses collection variables for base_url, access_token, and task_id

#### Testing Workflow

1. **Register a User**: Run the "Register User" request
2. **Login**: Run the "Login User" request (token is automatically saved)
3. **Create Task**: Run the "Create Task" request (task ID is automatically saved)
4. **List Tasks**: View all your tasks
5. **Get Task Details**: View a specific task using the saved task_id
6. **Update Task**: Modify a task using the saved task_id
7. **Delete Task**: Remove a task using the saved task_id

#### Collection Variables

- `base_url`: http://127.0.0.1:8000 (change if using different host/port)
- `access_token`: Automatically populated after login
- `task_id`: Automatically populated after creating a task

#### Manual Testing Endpoints

If you prefer manual testing, here are the endpoints:

**Authentication:**
- POST /api/auth/register
- POST /api/auth/login

**Task Management (requires Bearer token):**
- POST /api/tasks/
- GET /api/tasks/
- GET /api/tasks/{task_id}
- PUT /api/tasks/{task_id}
- DELETE /api/tasks/{task_id}

## Testing

Run the test suite:
```bash
pytest tests/test_api.py -v
```

## Project Milestones

### Milestone 1 (Nov Week 1): Project Setup and API Design
- Updated README.md with project overview and problem statement
- Created FastAPI project structure and virtual environment
- Added initial routes and data models

### Milestone 2 (Nov Week 2): Authentication and Database Integration
- Working register and login endpoints
- MongoDB connection established
- Token-based authentication implemented

### Milestone 3 (Nov Week 3): Task CRUD Operations
- CRUD endpoints for tasks
- Middleware for authentication
- Test cases for each route

### Milestone 4 (Nov Week 4): Testing and Local Deployment
- Passing tests
- Local API deployment completed
- Swagger documentation added

### Milestone 5 (Dec Week 1): Final Presentation and Documentation
- Presentation slides
- API documentation
- Summary of lessons learned

## Frontend

The project now includes a Streamlit-based frontend for a complete user experience.

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:
```bash
streamlit run app.py
```

The frontend will be available at `http://localhost:8501`

### Connecting Frontend to API

- Ensure the FastAPI backend is running locally at `http://localhost:8000` (see Setup Instructions above).
- The frontend automatically connects to the backend endpoints for authentication and task management.
- Register or login through the frontend to access the task dashboard.

### Frontend Features

- **User Registration**: Create a new account.
- **User Login**: Authenticate and receive a JWT token stored in session.
- **Task Dashboard**: View, create, update, and delete tasks.
- **Task Status Change**: Update task completion status via the update form.
- **Logout**: Clear session and return to login.

## Repository
https://github.com/Ka1ma/Assignment-Task-Tracker-API
