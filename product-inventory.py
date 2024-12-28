class Product:
    """
    A class to manage product inventory in an e-commerce system.
    Handles stock tracking, pricing, and discounts.
    """
    def __init__(self, id: str, name: str, price: float, stock: int = 0):
        self.id = id
        self.name = name
        self._price = price
        self._stock = stock
        self.discount = 0
        self._low_stock_threshold = 5
        self._stock_history = []

    @property
    def price(self) -> float:
        """Get discounted price"""
        return self._price * (1 - self.discount)

    def add_stock(self, quantity: int) -> None:
        """Add stock and record transaction"""
        self._stock += quantity
        self._stock_history.append(f"Added {quantity} units")
        self._check_stock_level()

    def remove_stock(self, quantity: int) -> bool:
        """Remove stock if available"""
        if self._stock >= quantity:
            self._stock -= quantity
            self._stock_history.append(f"Removed {quantity} units")
            self._check_stock_level()
            return True
        return False

    def _check_stock_level(self) -> None:
        """Alert if stock is low"""
        if self._stock <= self._low_stock_threshold:
            print(f"Low stock alert for {self.name}!")

# Usage example:
laptop = Product("P001", "Gaming Laptop", 999.99, 10)
laptop.discount = 0.1  # 10% discount
laptop.remove_stock(7)  # Will trigger low stock alert