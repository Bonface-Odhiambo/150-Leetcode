class BankAccount:
    """
    A class to represent a bank account.
    
    Attributes:
        account_number (str): Unique identifier for the account
        balance (float): Current balance in the account
        owner (str): Name of the account owner
        _transaction_history (list): Private list to store transaction records
    """
    
    def __init__(self, account_number: str, owner: str, initial_balance: float = 0.0):
        """
        Initialize a new bank account.
        
        Args:
            account_number (str): The account identifier
            owner (str): The name of the account owner
            initial_balance (float, optional): Starting balance. Defaults to 0.0
        """
        self.account_number = account_number
        self.owner = owner
        self.balance = initial_balance
        self._transaction_history = []  # Private attribute for storing transactions
    
    def deposit(self, amount: float) -> bool:
        """
        Deposit money into the account.
        
        Args:
            amount (float): Amount to deposit
            
        Returns:
            bool: True if deposit successful, False otherwise
            
        Raises:
            ValueError: If amount is negative
        """
        if amount < 0:
            raise ValueError("Deposit amount must be positive")
            
        self.balance += amount
        self._transaction_history.append(f"Deposit: ${amount}")
        return True
    
    def withdraw(self, amount: float) -> bool:
        """
        Withdraw money from the account.
        
        Args:
            amount (float): Amount to withdraw
            
        Returns:
            bool: True if withdrawal successful, False if insufficient funds
            
        Raises:
            ValueError: If amount is negative
        """
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive")
            
        if self.balance >= amount:
            self.balance -= amount
            self._transaction_history.append(f"Withdrawal: ${amount}")
            return True
        return False
    
    @property
    def transaction_history(self) -> list:
        """
        Get the transaction history.
        
        Returns:
            list: Copy of transaction history to prevent direct modification
        """
        return self._transaction_history.copy()
    
    def __str__(self) -> str:
        """
        String representation of the account.
        
        Returns:
            str: Formatted string with account details
        """
        return f"Account({self.account_number}) - Owner: {self.owner}, Balance: ${self.balance:.2f}"
    
    @classmethod
    def create_joint_account(cls, account_number: str, owners: list, initial_balance: float = 0.0):
        """
        Class method to create a joint account.
        
        Args:
            account_number (str): The account identifier
            owners (list): List of account owners
            initial_balance (float, optional): Starting balance. Defaults to 0.0
            
        Returns:
            BankAccount: New joint account instance
        """
        joint_owner_name = " & ".join(owners)
        return cls(account_number, joint_owner_name, initial_balance)

# Example usage:
if __name__ == "__main__":
    # Create a new account
    account = BankAccount("1234", "Bonface Odhiambo", 1000.0)
    
    # Perform some transactions
    account.deposit(500)
    account.withdraw(200)
    
    # Print account information
    print(account)  # Using __str__ method
    
    # Print transaction history
    print("\nTransaction History:")
    for transaction in account.transaction_history:
        print(transaction)
    
    # Create a joint account
    joint_account = BankAccount.create_joint_account("5678", ["Alice", "Bob"], 2000.0)
    print("\nJoint Account:")
    print(joint_account)