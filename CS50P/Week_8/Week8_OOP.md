# CS50P Week 8 - Object-Oriented Programming (OOP)

🎯 Topic: Understanding Object-Oriented Programming (OOP) in Python

---

## 🧠 WHY Learn This?

**Object-Oriented Programming (OOP)** is a **powerful paradigm** that helps organize and structure code by bundling **data** and **behavior** into objects.

By mastering **OOP**, you will:

- 🧑‍💻 **Write reusable & maintainable code** with classes and objects.
- 📦 **Encapsulate data** to avoid accidental modification.
- 🔄 **Model real-world entities** effectively in code.
- 🚀 **Simplify complex programs** with structured abstractions.

---

## 📌 WHAT You Need to Learn

### 1️⃣ Understand Classes & Objects

- Class: A blueprint for creating objects.
- Object: An instance of a class.
- Instance Variables: Attributes specific to each object.

```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

# Creating an object
harry = Student("Harry", "Gryffindor")
```

**Key Takeaway**: A class defines a structure, and objects are specific instances with their own values.

### 2️⃣ The `__init__` Method (Constructor)

- Automatically called when an object is created.
- Used to initialize instance variables.

```python
class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

# Creating a car object
my_car = Car("Tesla", 2024)
```

### 3️⃣ Encapsulation & Getters/Setters

- **Encapsulation**: Hides object details and ensures controlled access.
- **Getters**: Methods to access private attributes.
- **Setters**: Methods to modify attributes safely.

```python
class BankAccount:
    def __init__(self, balance):
        # Convention: _balance means "private"
        self._balance = balance  

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = amount
```

**Key Takeaway**: Getters & setters prevent accidental modification and allow validation before changing attributes.

### 4️⃣ Methods: Functions Inside Classes

Let's create a `Pizza` **class** that has:

1. An **instance method** (`describe`) → Works on individual objects.
2. A **static method** (`calculate_price`) → Does not depend on the class or instance.
3. A **class method** (`from_string`) → Creates a new instance from a formatted string.

```python
class Pizza:
    def __init__(self, size, toppings):
        self.size = size    # Instance attribute
        self.toppings = toppings

    def describe(self):     # Instance Method
        return (
            f"Pizza size: {self.size}, "
            f"Toppings: {', '.join(self.toppings)}"
        )

    @staticmethod
    def calculate_price(size):  # Static Method
        prices = {"small": 8, "medium": 12, "large": 15}
        return prices.get(size, "Unknown size")

    @classmethod
    def from_string(cls, pizza_str):    # Class Method
        size, toppings = pizza_str.split(":")
        toppings_list = toppings.split(",")
        # Creates a new instance
        return cls(size.strip(), toppings_list) 

# 📌 Using the instance method
pizza1 = Pizza("large", ["cheese", "pepperoni"])
# Output: "Pizza size: large, Toppings: cheese, pepperoni"
print(pizza1.describe())

# 📌 Using the static method (Doesn't need an instance)
print(Pizza.calculate_price("medium"))  # ✅ Output: 12

# 📌 Using the class method to create an object from a string
pizza2 = Pizza.from_string("small: mushrooms, olives")
# ✅ Output: Pizza size: small, Toppings: mushrooms, olives
print(pizza2.describe())
```

**Instance Method** (`describe`)

- Uses `self` to access and modify instance attributes.
- Works only on an object of the class.

**Static Method** (`calculate_price`)

- No `self` or `cls` is used.
- Acts like a **regular function inside the class**.
- Used when **we don't need to access instance or class-level data**.

**Class Method** (`from_string`)

- Uses `cls` instead of `self`.
- **Acts on the class itself**, not on an instance.
- Used to **create new instances in a different way** (like a factory method).

### 5️⃣ Dunder Methods (`__str__`, `__repr__`)

- `__str__`: Defines **how objects print**.
- `__repr__`: A technical representation for debugging.

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

book = Book("1984", "George Orwell")
print(book) # Output: '1984' by George Orwell
```

---

## 🚀 HOW to Learn This?

### Step 1: Understand the Basics

- 📖 Read about **classes, objects, methods, and** `__init__`. 
- 🛠️ Experiment with **creating classes** and **instantiating objects**.

### Step 2: Practice OOP Concepts

- ✅ Implement a `Car` class with attributes like `model` and `year`.
- ✅ Add a method `honk()` that prints **"Beep Beep!"**.
- ✅ Create multiple objects and call `honk()`.

### Step 3: Refactor Old Code Using OOP

- 🔄 Convert procedural code into **class-based OOP** code.
- 🏗️ Build a `Person` class with a `greet()` method.

### Step 4: Use Encapsulation & Properties

- 🏦 Create a `BankAccount` class that **prevents negative balance**.
- 🔍 Implement `@property` and `@balance.setter`.

### Step 5: Learn Advanced Concepts

- 🎭 Understand **inheritance, polymorphism**, and **abstract classes**.
- 🧩 Explore **decorators** and `@classmethod`.

---

## 📝 Summary and Key Insights

### Key Takeaways

- 💻 **OOP helps structure code** using **classes and objects**.
- 🔄 **Encapsulation** hides internal details and prevents modification.
- ✅ **Getters & setters** provide controlled access to data.
- 🎭 **Dunder methods** (`__str__`) make objects **print-friendly**.

### Common Mistakes

- ❌ Forgetting to include `self` in methods.
- ❌ Not using `@property` for validation.
- ❌ Confusing instance variables (`self.x`) with method parameters (`x`).

---

## ☘️ Checklist: Mastering OOP in Python

- ✅ I can define and instantiate **classes and objects**.
- ✅ I understand `__init__`, **instance variables**, and **methods**.
- ✅ I can encapsulate data useing getters and setters.
- ✅ I can use `__str__` and `__repr__` for object representation.
- ✅ I have built a **small project using OOP** (e.g., a student or bank account system).

*By mastering OOP, **you will write more scalable, reusable, and maintainable code**! 🚀*