from database.db_connection import db
from datetime import datetime

class Account:
    """Chart of Accounts Model"""
    
    def __init__(self, account_code, account_name, account_type, description=None):
        self.id = None
        self.account_code = account_code
        self.account_name = account_name
        self.account_type = account_type  # Asset, Liability, Equity, Revenue, Expense
        self.description = description
    
    def save(self):
        """Save account to database"""
        query = """
            INSERT INTO accounts (account_code, account_name, account_type, description)
            VALUES (?, ?, ?, ?)
        """
        self.id = db.execute_update(query, (self.account_code, self.account_name, self.account_type, self.description))
        return self.id
    
    def update(self):
        """Update account in database"""
        query = """
            UPDATE accounts 
            SET account_name=?, account_type=?, description=?, updated_at=?
            WHERE id=?
        """
        db.execute_update(query, (self.account_name, self.account_type, self.description, datetime.now(), self.id))
    
    @staticmethod
    def get_by_id(account_id):
        """Get account by ID"""
        query = "SELECT * FROM accounts WHERE id=?"
        result = db.execute_query(query, (account_id,))
        if result:
            row = result[0]
            account = Account(row['account_code'], row['account_name'], row['account_type'], row['description'])
            account.id = row['id']
            return account
        return None
    
    @staticmethod
    def get_all():
        """Get all accounts"""
        query = "SELECT * FROM accounts ORDER BY account_code"
        return db.execute_query(query)
    
    @staticmethod
    def get_by_type(account_type):
        """Get accounts by type"""
        query = "SELECT * FROM accounts WHERE account_type=? ORDER BY account_code"
        return db.execute_query(query, (account_type,))
    
    @staticmethod
    def delete(account_id):
        """Delete account"""
        query = "DELETE FROM accounts WHERE id=?"
        db.execute_update(query, (account_id,))
