# Configuration settings for the application

# MongoDB Atlas connection
MONGO_URL = "mongodb+srv://mychalredoblado_db_user:Assignment123@cluster0.krci2u0.mongodb.net/?appName=Cluster0"
DATABASE_NAME = "tasktracker"
SECRET_KEY = "your_secret_key_here"

# JWT settings
ACCESS_TOKEN_EXPIRE_MINUTES = 30
JWT_SECRET_KEY = SECRET_KEY
JWT_ALGORITHM = "HS256"

class Settings:
    ACCESS_TOKEN_EXPIRE_MINUTES: int = ACCESS_TOKEN_EXPIRE_MINUTES
    JWT_SECRET_KEY: str = JWT_SECRET_KEY
    JWT_ALGORITHM: str = JWT_ALGORITHM

settings = Settings()
