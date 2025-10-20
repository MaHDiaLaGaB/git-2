class Calculator:
    """A simple calculator class with basic arithmetic operations."""
    
    def add(self, x, y):
        """Add two numbers."""
        return x + y
    
    # TODO: Implement subtraction as homework
    def subtract(self, x, y):
        """Subtract y from x."""
        return x - y
    
    # TODO: Implement multiplication as homework
    def multiply(self, x, y):
        """Multiply two numbers."""
      
        return x * y 
    
   
    def divide(self, x, y):
        """Divide x by y."""
        if y == 0:
            raise ValueError
        return x / y
            
    
    # TODO: Implement power operation as homework
    def power(self, x, y):
        """Calculate x to the power of y (** operation)."""
        
        return x ** y
    

    # TODO: Implement power operation as homework
    def sqr(self, x):
        """Calculate x to the power of y (** operation)."""
        return x ** y
    