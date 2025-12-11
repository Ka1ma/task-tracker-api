from motor.motor_asyncio import AsyncIOMotorClient
from app.config import MONGO_URL, DATABASE_NAME
import ssl

# Create SSL context
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# Initialize MongoDB client with proper SSL configuration
client = AsyncIOMotorClient(
    MONGO_URL,
    tls=True,
    tlsAllowInvalidCertificates=True,
    serverSelectionTimeoutMS=5000,
    connectTimeoutMS=5000,
    socketTimeoutMS=5000
)
db = client[DATABASE_NAME]
