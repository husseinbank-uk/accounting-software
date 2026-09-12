from database.db_connection import db

class Reports:
    """Financial Reports Model"""
    
    @staticmethod
    def get_trial_balance(start_date=None, end_date=None):
        """Generate Trial Balance Report"""
        query = """
            SELECT 
                a.account_code,
                a.account_name,
                a.account_type,
                SUM(CASE WHEN jel.debit IS NOT NULL THEN jel.debit ELSE 0 END) as total_debit,
                SUM(CASE WHEN jel.credit IS NOT NULL THEN jel.credit ELSE 0 END) as total_credit
            FROM accounts a
            LEFT JOIN journal_entry_lines jel ON a.id = jel.account_id
            LEFT JOIN journal_entries je ON jel.journal_entry_id = je.id
        """
        
        params = []
        if start_date and end_date:
            query += " WHERE je.entry_date BETWEEN ? AND ?"
            params = [start_date, end_date]
        
        query += """
            GROUP BY a.id, a.account_code, a.account_name, a.account_type
            ORDER BY a.account_code
        """
        
        if params:
            return db.execute_query(query, tuple(params))
        else:
            return db.execute_query(query)
    
    @staticmethod
    def get_income_statement(start_date, end_date):
        """Generate Income Statement Report"""
        query = """
            SELECT 
                a.account_code,
                a.account_name,
                a.account_type,
                SUM(CASE WHEN jel.credit IS NOT NULL THEN jel.credit ELSE 0 END) as revenue,
                SUM(CASE WHEN jel.debit IS NOT NULL THEN jel.debit ELSE 0 END) as expense
            FROM accounts a
            LEFT JOIN journal_entry_lines jel ON a.id = jel.account_id
            LEFT JOIN journal_entries je ON jel.journal_entry_id = je.id
            WHERE (a.account_type = 'Revenue' OR a.account_type = 'Expense')
            AND je.entry_date BETWEEN ? AND ?
            GROUP BY a.id, a.account_code, a.account_name, a.account_type
            ORDER BY a.account_type, a.account_code
        """
        return db.execute_query(query, (start_date, end_date))
    
    @staticmethod
    def get_balance_sheet(as_of_date):
        """Generate Balance Sheet Report"""
        query = """
            SELECT 
                a.account_code,
                a.account_name,
                a.account_type,
                SUM(CASE WHEN jel.debit IS NOT NULL THEN jel.debit ELSE 0 END) - 
                SUM(CASE WHEN jel.credit IS NOT NULL THEN jel.credit ELSE 0 END) as balance
            FROM accounts a
            LEFT JOIN journal_entry_lines jel ON a.id = jel.account_id
            LEFT JOIN journal_entries je ON jel.journal_entry_id = je.id
            WHERE (a.account_type = 'Asset' OR a.account_type = 'Liability' OR a.account_type = 'Equity')
            AND je.entry_date <= ?
            GROUP BY a.id, a.account_code, a.account_name, a.account_type
            ORDER BY a.account_type, a.account_code
        """
        return db.execute_query(query, (as_of_date,))
    
    @staticmethod
    def get_account_ledger(account_id, start_date=None, end_date=None):
        """Get detailed ledger for a specific account"""
        query = """
            SELECT 
                je.entry_date,
                je.entry_number,
                je.description,
                jel.debit,
                jel.credit,
                (SUM(CASE WHEN jel2.debit IS NOT NULL THEN jel2.debit ELSE 0 END) - 
                 SUM(CASE WHEN jel2.credit IS NOT NULL THEN jel2.credit ELSE 0 END)) as running_balance
            FROM journal_entries je
            JOIN journal_entry_lines jel ON je.id = jel.journal_entry_id
            LEFT JOIN journal_entry_lines jel2 ON jel.account_id = jel2.account_id 
                AND jel2.journal_entry_id <= je.id
            WHERE jel.account_id = ?
        """
        
        params = [account_id]
        if start_date and end_date:
            query += " AND je.entry_date BETWEEN ? AND ?"
            params.extend([start_date, end_date])
        
        query += """
            GROUP BY je.id, je.entry_date, je.entry_number, je.description, jel.debit, jel.credit
            ORDER BY je.entry_date, je.id
        """
        
        return db.execute_query(query, tuple(params))
