import sys
from pathlib import Path
import pytest
from unittest.mock import patch

# Add the project root directory to the Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Configure pytest-asyncio
pytest_plugins = ('pytest_asyncio',)

@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"

@pytest.fixture(autouse=True)
def mock_database():
    """Mock the database for all tests"""
    from tests.test_database import mock_db
    
    # Clear the mock database before each test
    mock_db.clear_all()
    
    # Patch the database module to use mock_db
    with patch('app.database.db', mock_db):
        with patch('app.models.user_model.users_collection', mock_db["users"]):
            with patch('app.models.task_model.tasks_collection', mock_db["tasks"]):
                yield mock_db
    
    # Clear after test
    mock_db.clear_all()
