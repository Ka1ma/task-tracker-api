# Assignment Task Tracker API

A backend web service built with FastAPI for managing tasks, authentication, and project tracking.  
Developed for ITCC14 Web Services Final Project.

## Team Members
- Mychal Redoblado (@Ka1ma) (MychalXU)
- Kyle Gabriel T. Galanida (KGG-Student)
- Karlos Semilla (@Ykarlossemilla)
- Jhemar Visande (@JhemarVisande)

## Project Milestones

### Milestone 1 (Nov Week 1): Project Setup and API Design
What we'll do:
This week we will finalize the Task Tracker API topic, set up the FastAPI structure, and define the initial models for Users and Tasks.

Deliverables:
- Updated README.md with project overview and problem statement
- Created FastAPI project structure and virtual environment
- Added initial routes and data models

Checklists:
- [x] Define project scope and core features
- [x] Create FastAPI base app
- [x] Add User and Task models
- [x] Commit setup to GitHub

---

### Milestone 2 (Nov Week 2): Authentication and Database Integration
What we'll do:
Implement registration, login, and JWT authentication. Connect MongoDB using Motor.

Deliverables:
- Working register and login endpoints
- MongoDB connection established
- Token-based authentication implemented

Checklists:
- [x] Create auth_routes.py
- [x] Add password hashing and JWT token generation
- [x] Test register/login with pytest
- [x] Push updates to GitHub

---

### Milestone 3 (Nov Week 3): Task CRUD Operations
What we'll do:
Build CRUD endpoints for managing tasks. Secure routes with authentication.

Deliverables:
- CRUD endpoints for tasks
- Middleware for authentication
- Test cases for each route

Checklists:
- [x] Implement POST, GET, PUT, DELETE
- [x] Add authentication middleware
- [x] Write pytest cases
- [x] Commit and push changes

---

### Milestone 4 (Nov Week 4): Testing and Deployment
What we'll do:
Run all tests, prepare documentation, and deploy API to Heroku or similar platform.

Deliverables:
- Passing tests
- Hosted API link
- Final README documentation

Checklists:
- [x] Complete tests
- [x] Deploy API (prepared deployment files)
- [ ] Update README with live link

---

### Milestone 5 (Dec Week 1): Final Presentation and Documentation
What we'll do:
Prepare slides, finalize API documentation, and present the project.

Deliverables:
- Presentation slides
- API documentation
- Summary of lessons learned

Checklists:
- [ ] Finalize slides
- [ ] Present project
- [ ] Archive final version on GitHub

---

## Problem Statement
Teams and individuals often struggle to track their daily tasks effectively.  
This API aims to provide a lightweight system to manage tasks, monitor progress, and maintain accountability.

## Goals
- Implement a secure authentication system using JWT
- Provide CRUD operations for task management
- Ensure a simple and reliable backend for future frontend integration

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login` - Login and get JWT token

### Tasks (Protected)
- `POST /api/tasks/` - Create a new task
- `GET /api/tasks/` - List all tasks for the authenticated user
- `GET /api/tasks/{task_id}` - Get a specific task
- `PUT /api/tasks/{task_id}` - Update a task
- `DELETE /api/tasks/{task_id}` - Delete a task

## Deployment

The API is prepared for deployment on Heroku with the following files:
- `Procfile` - Defines the web process
- `runtime.txt` - Specifies Python version
- `requirements.txt` - Lists all dependencies

To deploy:
1. Create a Heroku account and install Heroku CLI
2. Run `heroku create your-app-name`
3. Set environment variables (e.g., `MONGODB_URL`, `SECRET_KEY`)
4. Run `git push heroku main`
5. The API will be live at `https://your-app-name.herokuapp.com`

Repository: https://github.com/Ka1ma/task-tracker-api
