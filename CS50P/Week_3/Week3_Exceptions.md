# CS50P Week 3 - Exceptions

🎯 Topic: Handling Errors and Exceptions in Python

---

## 🧠 WHY Learn This?

Errors are **inevitable** in programming. Instead of letting them crash your program, **exception handling** allows you to anticipate, detect, and manage errors gracefully. Imagine:

- 💸 A banking system incorrectly processes a transaction due to invalid user input.
- 🔢 A calculator program crashes when dividing by zero.
- 👨🏻‍💻 A web scraper stops running because of a temporary connection failure.

By mastering exception handling, you will:

- 🛡️ **Make your programs resilient** by handling unexpected inputs and errors.
- 🧍‍♂️ **Improve user experience** by providing helpful error messages.
- 👨‍🔧 **Debug efficiently** by understanding error types and managing them properly.

---

## 📌 WHAT You Need to Learn

### 1️⃣ Types of Errors in Python

<table>
    <tr>
        <th>Type</th>
        <th>Description</th>
        <th>Example</th>
    </tr>
    <tr>
        <td><strong>Syntax Error</strong></td>
        <td>Code structure is incorrect</td>
        <td><code>print("Hello</code>(missing <code>")</code></td>
    </tr>
    <tr>
        <td><strong>Runtime Error</strong></td>
        <td>Error happens while code is running</td>
        <td><code>5 / 0</code>(ZeroDivisionError)</td>
    </tr>
    <tr>
        <td><strong>Value Error</strong></td>
        <td>Data type is incorrect</td>
        <td><code>int("hello")</code></td>
    </tr>
    <tr>
        <td><strong>Name Error</strong></td>
        <td>Using an undefined variable</td>
        <td><code>print(x)</code>when <code>x</code> is not defined</td>
    </tr>
</table>

---

### 2️⃣ Using `try` and `except` for Error Handling

Python provides `try` and `except` to **catch and handle errors**.

**Basic Structure**
```python
try:
    x = int(input("Enter a number: "))  # Code that might fail
except ValueError:
    print("That's not a valid number!")  # Handle the error
```

If the user enters `"cat"`, the program **won't crash**. Instead, it will print a friendly message.

---

### 3️⃣ Catching Specific Errors

It's better to **catch specific errors** instead of using a generic `except`.

```python
try:
    x = int(input("Enter a number: "))
    y = 10 / x
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

💡 **Key Point**: Multiple `except` blocks handle different types of errors separately.

---

### 4️⃣ Using `else` with `try-except`

If no error occurs, use `else` to execute code **only when everything goes well**.

```python
try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print(f"x is {x}")  # Runs only if `try` succeeds
```

---

### 5️⃣ Using `finally`

The `finally` block **always executes**, whether an error occurs or not.

```python
try:
    file = open("data.txt")
    data = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()  # Ensures file is closed even if an error happens
```

💡 **Key Point**: `finally` is useful for **cleanup operations** like closing files or database connections.

---

### 6️⃣ Handling Loops with Exception Handling

Instead of crashing, **keep prompting** the user until they enter a valid input.

```python
while True:
    try:
        x = int(input("Enter an integer: "))
        break  # Exit loop if input is valid
    except ValueError:
        print("Oops! That's not a number. Try again.")
```

---

## 🚀 HOW to Learn This?

### Step 1: Understand Common Errors

- Run Python code **without error handling** to see the **default** error messages.
- 🔍 **Identify patterns** in error messages (e.g., `ValueError`, `ZeroDivisionError`).
- Practice explaining errors in **plain English** using *Feynman Technique*.

---

### Step 2: Experiment with `try-except`

- 🛠️ Modify the code to **catch multiple types of errors**.
- ⏭️ Test `except Exception:` to **catch all errors** (but avoid overusing it).
- 📌 Use `else` and `finally` to **see when they execute**.

---

### Step 3: Refactor and Optimize

- Replace **manual input validation** with exception handling.
- Move repeated error-handling code into **functions**.
- Improve user experience with **clearer error messages**.

---

## 📝 Summary and Key Insights

### Key Takeaways

- 🛑 **Syntax errors** must be fixed before running the program.
- ⚠️ **Exceptions** happen at runtime and should be handled using `try-except`.
- 🎯 **Catching specific errors** is **better** than using a generic `except`.
- ✅ **Use** `else` when no errors occur.
- 🔄 **Use** `finally` for cleanup tasks like closing files or releasing resources.
- 🔁 **Loop until correct input** instead of immediately exiting on errors.

### Common Mistakes

- ❌ Using a **generic** `except:` (hides bugs, makes debugging hard).
- 🚫 Forgetting to **break out of loops** after valid input.
- ⚠️ Placing **too much code** inside `try`, instead of isolating risky operations.

---

## ☘️ Checklist: Mastering Exceptions in Python

- ✅ I can identify **syntax, runtime, and logical errors**.
- ✅ I understand how `try` and `except` prevent crashes.
- ✅ I know how to **catch specific exceptions** (e.g., `ValueError`, `ZeroDivisionError`).
- ✅ I can use `else` and `finally` blocks properly.
- ✅ I can **loop until valid input** using exception handling.
- ✅ I can **write functions** that handle errors cleanly.

*By learning **exception handling**, you will write **robust** and **error-resistant** programs. 🚀*