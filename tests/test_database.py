"""
Mock database for testing purposes
"""
from typing import Dict, List, Optional
from datetime import datetime
from bson import ObjectId

class MockCollection:
    """Mock MongoDB collection for testing"""
    
    def __init__(self):
        self.data: Dict[str, dict] = {}
        self.counter = 0
    
    async def find_one(self, query: dict) -> Optional[dict]:
        """Find one document matching the query"""
        for doc_id, doc in self.data.items():
            # Handle ObjectId queries
            query_match = {}
            for k, v in query.items():
                if k == "_id" and isinstance(v, ObjectId):
                    query_match[k] = str(v)
                else:
                    query_match[k] = v
            
            # Check if document matches
            match = all(
                (k == "_id" and doc_id == query_match.get(k)) or 
                (k != "_id" and doc.get(k) == query_match.get(k))
                for k in query_match.keys()
            )
            if match:
                return {**doc, "_id": doc_id}
        return None
    
    async def insert_one(self, document: dict):
        """Insert a document"""
        # Generate a valid ObjectId string
        doc_id = str(ObjectId())
        self.data[doc_id] = {**document, "created_at": datetime.utcnow().isoformat()}
        
        class InsertResult:
            def __init__(self, inserted_id):
                self.inserted_id = inserted_id
        
        return InsertResult(doc_id)
    
    def find(self, query: dict = None):
        """Find documents matching the query"""
        results = []
        query = query or {}
        for doc_id, doc in self.data.items():
            if not query or all(doc.get(k) == v for k, v in query.items()):
                results.append({**doc, "_id": doc_id, "id": doc_id})
        return MockCursor(results)
    
    async def update_one(self, query: dict, update: dict):
        """Update one document"""
        for doc_id, doc in self.data.items():
            # Handle ObjectId queries
            query_match = {}
            for k, v in query.items():
                if k == "_id" and isinstance(v, ObjectId):
                    query_match[k] = str(v)
                else:
                    query_match[k] = v
            
            # Check if document matches
            match = all(
                (k == "_id" and doc_id == query_match.get(k)) or 
                (k != "_id" and doc.get(k) == query_match.get(k))
                for k in query_match.keys()
            )
            if match:
                if "$set" in update:
                    self.data[doc_id].update(update["$set"])
                
                class UpdateResult:
                    def __init__(self):
                        self.modified_count = 1
                
                return UpdateResult()
        
        class UpdateResult:
            def __init__(self):
                self.modified_count = 0
        
        return UpdateResult()
    
    async def delete_one(self, query: dict):
        """Delete one document"""
        for doc_id, doc in self.data.items():
            # Handle ObjectId queries
            query_match = {}
            for k, v in query.items():
                if k == "_id" and isinstance(v, ObjectId):
                    query_match[k] = str(v)
                else:
                    query_match[k] = v
            
            # Check if document matches
            match = all(
                (k == "_id" and doc_id == query_match.get(k)) or 
                (k != "_id" and doc.get(k) == query_match.get(k))
                for k in query_match.keys()
            )
            if match:
                del self.data[doc_id]
                
                class DeleteResult:
                    def __init__(self):
                        self.deleted_count = 1
                
                return DeleteResult()
        
        class DeleteResult:
            def __init__(self):
                self.deleted_count = 0
        
        return DeleteResult()
    
    def clear(self):
        """Clear all data"""
        self.data.clear()
        self.counter = 0


class MockCursor:
    """Mock MongoDB cursor"""
    
    def __init__(self, results: List[dict]):
        self.results = results
    
    async def to_list(self, length: Optional[int] = None):
        """Convert cursor to list"""
        if length is None:
            return self.results
        return self.results[:length]


class MockDatabase:
    """Mock MongoDB database for testing"""
    
    def __init__(self):
        self.collections = {}
    
    def __getitem__(self, name: str) -> MockCollection:
        """Get or create a collection"""
        if name not in self.collections:
            self.collections[name] = MockCollection()
        return self.collections[name]
    
    def clear_all(self):
        """Clear all collections"""
        for collection in self.collections.values():
            collection.clear()


# Global mock database instance for tests
mock_db = MockDatabase()
