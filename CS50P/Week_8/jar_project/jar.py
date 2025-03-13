class Jar:
    def __init__(self, capacity=12):
        # Initialize the cookie jar with a given capacity.
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = capacity   # Use _capacity to indicate it's private
        self._cookies = 0   # Start with an empty jar

    def __str__(self):
        # Return a string representation of the cookie jar.
        return "🍪" * self._cookies

    def _validate_amount(self, n):
        # Helper method to validate cookie amount.
        if not isinstance(n, int) or n < 0:
            raise ValueError("Number of cookies must be a non-negative integer.")

    def deposit(self, n):
        # Add cookies to the jar if within capacity.
        self._validate_amount(n)
        if self._cookies + n > self._capacity:
            raise ValueError("Not enough space in the jar.")
        self._cookies += n

    def withdraw(self, n):
        # Remove cookies from the jar if enough are available.
        self._validate_amount(n)
        if n > self._cookies:
            raise ValueError("Not enough cookies to withdraw.")
        self._cookies -= n

    @property
    def capacity(self):
        # Return the jar's capacity.
        return self._capacity

    @property
    def size(self):
        # Return the number of cookies currently in the jar.
        return self._cookies
