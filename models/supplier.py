from database.db_connection import db
from datetime import datetime

class Supplier:
    """Supplier Model"""
    
    def __init__(self, supplier_code, supplier_name, email=None, phone=None, address=None, city=None, country=None, tax_id=None):
        self.id = None
        self.supplier_code = supplier_code
        self.supplier_name = supplier_name
        self.email = email
        self.phone = phone
        self.address = address
        self.city = city
        self.country = country
        self.tax_id = tax_id
    
    def save(self):
        """Save supplier to database"""
        query = """
            INSERT INTO suppliers (supplier_code, supplier_name, email, phone, address, city, country, tax_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.id = db.execute_update(query, (
            self.supplier_code, self.supplier_name, self.email, self.phone,
            self.address, self.city, self.country, self.tax_id
        ))
        return self.id
    
    def update(self):
        """Update supplier in database"""
        query = """
            UPDATE suppliers 
            SET supplier_name=?, email=?, phone=?, address=?, city=?, country=?, tax_id=?, updated_at=?
            WHERE id=?
        """
        db.execute_update(query, (
            self.supplier_name, self.email, self.phone, self.address,
            self.city, self.country, self.tax_id, datetime.now(), self.id
        ))
    
    @staticmethod
    def get_by_id(supplier_id):
        """Get supplier by ID"""
        query = "SELECT * FROM suppliers WHERE id=?"
        result = db.execute_query(query, (supplier_id,))
        if result:
            row = result[0]
            supplier = Supplier(row['supplier_code'], row['supplier_name'], row['email'], row['phone'],
                              row['address'], row['city'], row['country'], row['tax_id'])
            supplier.id = row['id']
            return supplier
        return None
    
    @staticmethod
    def get_all():
        """Get all suppliers"""
        query = "SELECT * FROM suppliers ORDER BY supplier_name"
        return db.execute_query(query)
    
    @staticmethod
    def delete(supplier_id):
        """Delete supplier"""
        query = "DELETE FROM suppliers WHERE id=?"
        db.execute_update(query, (supplier_id,))
