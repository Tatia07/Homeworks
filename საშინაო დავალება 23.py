# 1. დაწერე სასურველი პროგრამა. ეცადე დაეყრდნო SOLID პრინციპებს.    

class Product:
    def __init__(self, name, price, stock):
        self._name = name
        self._price = price
        self._stock = stock

    def __str__(self):
        return f"Product name: {self._name}, Price: ${self._price}, Stock: {self._stock}"

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._validate_string_input(name)
        self._name = name

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._validate_positive_float_input(price)
        self._price = price

    def get_stock(self):
        return self._stock

    def set_stock(self, stock):
        self._validate_non_negative_integer_input(stock)
        self._stock = stock
    
# Validation

    def _validate_string_input(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Input must be a non-empty string")

    def _validate_positive_float_input(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Input must be a non-negative float")

    def _validate_non_negative_integer_input(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Input must be a non-negative integer")


class ProductManager:
    def product_info(self, product):
        print(f"Product Information: {product}")

    def update_info(self, product, name=None, price=None, stock=None):
        if name is not None:
            product.set_name(name)
        if price is not None:
            product.set_price(price)
        if stock is not None:
            product.set_stock(stock)

if __name__ == "__main__":
    product = Product(name="Laptop", price=999.99, stock=50)
    
    product_manager = ProductManager()
    product_manager.product_info(product)

    # Update

    product_manager.update_info(product, price=899.99, stock=45)
    product_manager.product_info(product)