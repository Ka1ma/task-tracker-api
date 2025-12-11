# TODO for Completing Milestone 4

- [x] Fix bug in app/models/task_model.py: Import ObjectId and correct _id queries in update_task and delete_task
- [x] Fix tests/test_api.py: Use AsyncClient for consistent testing with async app
- [x] Run pytest to test register/login endpoints
- [x] Push updates to GitHub
- [x] Update README with API documentation and deployment instructions
- [x] Update README with interactive API docs (Swagger/ReDoc)
- [x] Local deployment completed

# Recent Fixes (Current Session)

- [x] Fixed pytest import issues by creating tests/__init__.py and tests/conftest.py
- [x] Added pytest-asyncio, httpx, and pytest to requirements.txt
- [x] Updated test_api.py to use ASGITransport for httpx AsyncClient compatibility
- [x] Enhanced database.py with improved SSL/TLS configuration for MongoDB Atlas
- [x] Created mock database (tests/test_database.py) to avoid MongoDB connection issues during testing
- [x] Implemented proper ObjectId handling in mock database
- [x] All tests now passing successfully!

# Test Results Summary

**Status**: ALL TESTS PASSING

```
tests/test_api.py::test_register_and_login PASSED [100%]
1 passed, 6 warnings in 1.08s
```

The test successfully validates:
- User registration
- User login with JWT token generation
- Task creation with authentication
- Task listing
- Task retrieval by ID
- Task update
- Task deletion

# Known Warnings (Non-Critical)

- Deprecation warnings for `datetime.utcnow()` (Python 3.13)
- Pydantic V2 deprecation warnings for `.dict()` method (should use `.model_dump()`)

# Next Steps

- [ ] Consider fixing deprecation warnings for future Python/Pydantic compatibility
- [ ] Add more comprehensive test coverage (edge cases, error handling)
- [ ] Prepare final presentation materials for Milestone 5
- [ ] Document lessons learned
- [ ] Consider adding integration tests with actual MongoDB (optional)
