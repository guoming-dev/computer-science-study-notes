# CS50P Week 1 - Conditionals

🎯 Topic: Conditionals and Decision-Making in Python

---

## 🧠 WHY Learn This?

Conditionals allow a program to **make decisions** based on data. Imagine you are writing software that checks if a user is old enough to vote, a bank account has sufficient funds, or a game character has enough health to continue. **Without conditionals, all programs would execute in a linear fashion without any intelligence.**

By mastering conditionals, you will:

- 🌟 Learn how to **control the flow** of your programs.
- 🚀 **Optimize logic** by making smarter decisions in your code.
- 🎓 Prepare for more advanced programming concepts like **loops and algorithms*.

---

## 📌 WHAT You Need to Learn

### 1️⃣ Comparison Operators

Python provides several operators to compare values:

- `>` (greater than)
- `<` (less than)
- `>=` (greater than or equal to)
- `<=` (less than or equal to)
- `==` (equal to)
- `!=` (not equal to)

---

### 2️⃣ Boolean Expressions

These expressions evaluate to `True` or `False`, which are fundamental in decision-making.

```python
x = 5
y = 10
print(x < 5) # Output: True
```

---

### 3️⃣ The `if` Statement

A simple decision-making construct:

```python
if x < y:
    print("x is smaller than y")
```

---

### 4️⃣ The `if-else` Statement

Executing different blocks of code based on conditions:

```python
if x < y:
    print("x is smaller")
else:
    print("x is greater or equal")
```

---

### 5️⃣ The `elif` Statement

Handling multiple conditions:

```python
if x > y:
    print("x is greater")
elif x == y:
    print("x and y are equal")
else:
    print("x is smaller")
```

---

### 6️⃣ Logical Operators (`and`, `or`, `not`)

Combining multiple conditions:

```python
age = 25
income = 50000

if age > 18 and income > 30000:
    print("Eligible for loan")
```

---

### 7️⃣ The `match` Statement (Python 3.10+)

A new way to handle multiple conditions (similar to switch-case in other languages):

```python
color = "red"

match color:
    case "red":
        print("Stop!")
    case "green":
        print("Go!")
    case "yellow":
        print("Slow down!")
    case _:
        print("Invalid color")
```

---

## 🚀 HOW to Learn This?

### Step 1: Understand the Theory

- 🌟 Read about conditionals and compare different ways they are used.
- 📖 Study flowcharts to **visualize decision-making**.
- 🤓 Explain conditionals in **plain English** to yourself (*Feynman Technique*).

---

### Step 2: Write Small Programs:

Practice with real-world examples:

- 🔒 Age Verification: Check if a user is old enough to enter a website.
- 🌡️ Temperature Check: Print a message based on a given temperature.
- 🧮 Basic Calculator: Perform different operations based on user input.

---

### Step 3: Debug Your Code

- ⚠️ Remove indentation and see what error appears.
- ⚡️ Try using `=` instead of `==` in conditions to understand assignment vs comparison.

---

### Step 4: Optimize Using `elif` and `match`

Refactor messy `if` statements by making them **cleaner and more efficient**.

---

## 📝 Summary and Key Insights

### Key Takeaways

- ⚖️ Conditionals allow your program to make decisions.
- ✨ `if`, `elif`, and `else` are used for **branching** logic.
- ⽐ Comparison and logical operators help create **Boolean expressions**.
- 🔁 The `match` statement is an **advanced alternative** to `if-elif-else`.
- 👍 Always test with edge cases like `0`, `negative values`, and `None`.

### Common Mistakes

- ❌ Using `=` instead of `==` in conditions.
- ⛔️ Forgetting to **indent** blocks of code.
- ⛨ Overusing `if` instead of optimizing with `elif` or `match`.

---

## ☘️ Checklist: Conditionals in Python

- ✅ I understand **comparison operators** and **Boolean expressions**.
- ✅ I can use **if, else, and elif** statements correctly.
- ✅ I can apply **logical operators (`and`, `or`, `not`)**.
- ✅ I have tried using the **`match` statement** (if on Python 3.10+).
- ✅ I have **debugged** common mistakes like incorrect indentation or misplaced operators.
- ✅ I can write **clean and optimized** conditional statements.