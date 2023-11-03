"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start = 100):
        """
        create initial value
        """
        self.current_val = start

    def generate(self):
        """
        retrieve current value and increase stored value by 1
        """
        val = self.current_val
        self.current_val += 1
        return val

    def reset(self):
        """
        reset current value
        """
        self.current_val = 100
