import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem,
                             QDialog, QLabel, QLineEdit, QComboBox, QMessageBox)
from PyQt5.QtCore import Qt
from database.db_connection import db
from database.chart_of_accounts import seed_chart_of_accounts
from models.account import Account

class AccountDialog(QDialog):
    """Dialog for adding/editing accounts"""
    
    def __init__(self, parent=None, account=None):
        super().__init__(parent)
        self.account = account
        self.init_ui()
        
        if account:
            self.load_account_data()
    
    def init_ui(self):
        """Initialize the dialog UI"""
        self.setWindowTitle("Account" if not self.account else "Edit Account")
        self.setGeometry(100, 100, 500, 300)
        
        layout = QVBoxLayout()
        
        # Account Code
        layout.addWidget(QLabel("Account Code:"))
        self.code_input = QLineEdit()
        self.code_input.setReadOnly(self.account is not None)  # Read-only for editing
        layout.addWidget(self.code_input)
        
        # Account Name (English)
        layout.addWidget(QLabel("Account Name (English):"))
        self.name_input = QLineEdit()
        layout.addWidget(self.name_input)
        
        # Account Type
        layout.addWidget(QLabel("Account Type:"))
        self.type_combo = QComboBox()
        self.type_combo.addItems(["Asset", "Liability", "Equity", "Revenue", "Expense"])
        layout.addWidget(self.type_combo)
        
        # Description
        layout.addWidget(QLabel("Description (Arabic):"))
        self.description_input = QLineEdit()
        layout.addWidget(self.description_input)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        save_btn = QPushButton("Save")
        cancel_btn = QPushButton("Cancel")
        
        save_btn.clicked.connect(self.save_account)
        cancel_btn.clicked.connect(self.reject)
        
        button_layout.addWidget(save_btn)
        button_layout.addWidget(cancel_btn)
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
    
    def load_account_data(self):
        """Load account data into form"""
        if self.account:
            self.code_input.setText(self.account['account_code'])
            self.name_input.setText(self.account['account_name'])
            self.type_combo.setCurrentText(self.account['account_type'])
            self.description_input.setText(self.account['description'] or "")
    
    def save_account(self):
        """Save account to database"""
        code = self.code_input.text().strip()
        name = self.name_input.text().strip()
        acc_type = self.type_combo.currentText()
        description = self.description_input.text().strip()
        
        if not code or not name:
            QMessageBox.warning(self, "Validation Error", "Please fill in all required fields")
            return
        
        try:
            if self.account:
                # Update existing account
                query = """
                    UPDATE accounts 
                    SET account_name=?, account_type=?, description=?
                    WHERE id=?
                """
                db.execute_update(query, (name, acc_type, description, self.account['id']))
                QMessageBox.information(self, "Success", "Account updated successfully")
            else:
                # Create new account
                account = Account(code, name, acc_type, description)
                account.save()
                QMessageBox.information(self, "Success", "Account created successfully")
            
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save account: {str(e)}")


class ChartOfAccountsWidget(QWidget):
    """Widget for managing Chart of Accounts"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.load_accounts()
    
    def init_ui(self):
        """Initialize the UI"""
        layout = QVBoxLayout()
        
        # Title
        title = QLabel("Chart of Accounts")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        add_btn = QPushButton("Add Account")
        seed_btn = QPushButton("Seed Chart of Accounts")
        refresh_btn = QPushButton("Refresh")
        delete_btn = QPushButton("Delete Selected")
        
        add_btn.clicked.connect(self.add_account)
        seed_btn.clicked.connect(self.seed_accounts)
        refresh_btn.clicked.connect(self.load_accounts)
        delete_btn.clicked.connect(self.delete_account)
        
        button_layout.addWidget(add_btn)
        button_layout.addWidget(seed_btn)
        button_layout.addWidget(refresh_btn)
        button_layout.addWidget(delete_btn)
        layout.addLayout(button_layout)
        
        # Accounts Table
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels([
            "Account Code", 
            "Account Name", 
            "Account Type", 
            "Description",
            "ID"
        ])
        self.table.setColumnHidden(4, True)  # Hide ID column
        self.table.cellDoubleClicked.connect(self.edit_account)
        layout.addWidget(self.table)
        
        self.setLayout(layout)
    
    def load_accounts(self):
        """Load accounts from database and display in table"""
        try:
            accounts = Account.get_all()
            self.table.setRowCount(len(accounts))
            
            for row, account in enumerate(accounts):
                self.table.setItem(row, 0, QTableWidgetItem(account['account_code']))
                self.table.setItem(row, 1, QTableWidgetItem(account['account_name']))
                self.table.setItem(row, 2, QTableWidgetItem(account['account_type']))
                self.table.setItem(row, 3, QTableWidgetItem(account['description'] or ""))
                self.table.setItem(row, 4, QTableWidgetItem(str(account['id'])))
            
            self.table.resizeColumnsToContents()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load accounts: {str(e)}")
    
    def add_account(self):
        """Open dialog to add new account"""
        dialog = AccountDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            self.load_accounts()
    
    def edit_account(self, row, column):
        """Edit selected account"""
        account_id = int(self.table.item(row, 4).text())
        account = Account.get_by_id(account_id)
        
        if account:
            # Get full account data
            query = "SELECT * FROM accounts WHERE id=?"
            result = db.execute_query(query, (account_id,))
            if result:
                dialog = AccountDialog(self, result[0])
                if dialog.exec_() == QDialog.Accepted:
                    self.load_accounts()
    
    def delete_account(self):
        """Delete selected account"""
        selected_row = self.table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Selection Error", "Please select an account to delete")
            return
        
        account_id = int(self.table.item(selected_row, 4).text())
        
        reply = QMessageBox.question(self, "Confirm Delete", 
                                     "Are you sure you want to delete this account?",
                                     QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            try:
                Account.delete(account_id)
                QMessageBox.information(self, "Success", "Account deleted successfully")
                self.load_accounts()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to delete account: {str(e)}")
    
    def seed_accounts(self):
        """Seed Chart of Accounts"""
        reply = QMessageBox.question(self, "Confirm Seed", 
                                     "This will add all Iraqi standard accounts. Continue?",
                                     QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            try:
                seed_chart_of_accounts()
                QMessageBox.information(self, "Success", "Chart of Accounts seeded successfully")
                self.load_accounts()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to seed accounts: {str(e)}")


class MainWindow(QMainWindow):
    """Main Application Window"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Accounting Software - Chart of Accounts")
        self.setGeometry(100, 100, 1200, 700)
        
        # Create central widget
        central_widget = ChartOfAccountsWidget()
        self.setCentralWidget(central_widget)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
