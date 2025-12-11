import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def test_connection():
    try:
        client = AsyncIOMotorClient(
            'mongodb+srv://mychalredoblado_db_user:Assignment123@cluster0.krci2u0.mongodb.net/?appName=Cluster0',
            tls=True,
            tlsAllowInvalidCertificates=True,
            serverSelectionTimeoutMS=5000
        )
        await client.admin.command('ping')
        print("✓ MongoDB connection successful")
        
        # Test database access
        db = client["tasktracker"]
        collections = await db.list_collection_names()
        print(f"✓ Available collections: {collections}")
        
        client.close()
    except Exception as e:
        print(f"✗ MongoDB connection failed: {e}")

if __name__ == "__main__":
    asyncio.run(test_connection())
