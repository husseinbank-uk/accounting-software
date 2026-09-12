import sqlite3
import os
from pathlib import Path

class DatabaseConnection:
    """Handles all database connections and initialization"""
    
    _instance = None
    _connection = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if self._connection is None:
            self.db_path = os.path.join(str(Path.home()), '.accounting_software', 'accounting.db')
            os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
            self.connect()
            self.initialize_database()
    
    def connect(self):
        """Establish database connection"""
        try:
            self._connection = sqlite3.connect(self.db_path)
            self._connection.row_factory = sqlite3.Row
            self._connection.execute('PRAGMA foreign_keys = ON')
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")
            raise
    
    def get_connection(self):
        """Get the database connection"""
        if self._connection is None:
            self.connect()
        return self._connection
    
    def initialize_database(self):
        """Initialize database tables from schema"""
        schema_path = os.path.join(os.path.dirname(__file__), 'schema.sql')
        try:
            with open(schema_path, 'r') as f:
                schema = f.read()
            cursor = self._connection.cursor()
            cursor.executescript(schema)
            self._connection.commit()
            print("Database initialized successfully")
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")
            raise
    
    def execute_query(self, query, params=None):
        """Execute a SELECT query"""
        cursor = self._connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        return cursor.fetchall()
    
    def execute_update(self, query, params=None):
        """Execute INSERT, UPDATE, or DELETE query"""
        cursor = self._connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        self._connection.commit()
        return cursor.lastrowid
    
    def close(self):
        """Close database connection"""
        if self._connection:
            self._connection.close()
            self._connection = None
    
    def __del__(self):
        self.close()

# Singleton instance
db = DatabaseConnection()
