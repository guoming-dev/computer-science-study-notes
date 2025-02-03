# CS50P Week 0 - Functions, Variables

🎯 Topic: Functions, Variables, and Command Line Basics

---

## 🧠 WHY Learn This?

Programming is a **powerful tool** for solving problems, automating tasks, and building software.
Python, in particular, is widely used for:

- Web Development (Django, Flask)
- Data Science (Pandas, NumPy)
- Artificial Intelligence & Machine Learning (TensorFlow, PyTorch)
- Cybersecurity & Automation (Scripting, Ethical Hacking)

Understanding **how a computer executes code** will help you become a better problem solver and write efficient programs.

---

## 📌 WHAT You Need to Learn

### 1️⃣ What is a Program?

A **program** is a set of instructions that a computer follows to perform a task.

- Example: A calculator program takes numbers as input and give results.
- Programs can be written in many languages: Python, Java, C, etc.

**💡 Computers only understand binary (0s and 1s), but we write code in human-readable languages, which are later translated into binary.**

---

### 2️⃣ What is Python?

Python is a **high-level, interpreted programming language** known for its **simplicity and readability**.

**🔥 Why Python?**

- **✅ Beginner-friendly**: Simple syntax, easy to learn.
- **✅ Multi-purpose**: Used in many fields (Web Dev, Data Science, AI).
- **✅ Huge community support**: Many open-source libraries available.
- **✅ Cross-platform**: Works on Windows, macOS, Linux.

**💡 Unlike compiled languages (C, Java), Python is an interpreted language, meaning it runs line-by-line rather than being compiled into machine code.**

---

### 3️⃣ Setting Up Python & Your First Program

Before we start coding, we need to set up the **Python environment**.

**🔧 Steps to Install Python**
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Install **VS Code** (or any text editor)
3. Open **VS Code Terminal**
4. Type `python --version` to check if Python is installed

**💻 Writing Your First Python Program**

Let's write a simple **"Hello, World!"** program:
```python
print("Hello, World!")
```
🛠️ How It Works:

- `print()` is a **function** that **displays text on the screen**.
- `"Hello, World!"` is a **string** (text enclosed in quotation marks).

Run the program in the **terminal** by typing:
```bash
python hello.py
```

**💡 Python executes code from top to bottom, line by line.**

---

### 4️⃣ Understanding the Command Line Interface (CLI)

The **Command Line Interface (CLI)** is a way to interact with a computer using **text-based commands** instead of clicking icons.

<table>
    <tr>
        <th>Command</th>
        <th>Description</th>
    </tr>
    <tr>
        <td><code>python</code></td>
        <td>Starts Python interactive mode</td>
    </tr>
    <tr>
        <td><code>python script.py</code></td>
        <td>Runs a Python script</td>
    </tr>
    <tr>
        <td><code>ls</code> / <code>dir</code></td>
        <td>Lists files in the directory</td>
    </tr>
    <tr>
        <td><code>cd foldername</code></td>
        <td>Changes directory</td>
    </tr>
    <tr>
        <td><code>exit()</code></td>
        <td>Exits Python interactive mode</td>
    </tr>
</table>

**💡 Python can be run using interactive mode (`python`) or by executing a script (`python file.py`).**

---

### 5️⃣ Functions & Variables

**📌 What is a Function?**

A function is a reusable block of code that performs a specific task.
- Example: The `print()` function prints output to the screen.

**📌 Creating a Function in Python:**
```python
def greet():
    print("Hello!")
greet() # Calling the function
```

**💡 Why Use Functions?**
- ✅ Avoid Repetition
- ✅ Organize code
- ✅ Make programs readable

**📌 What is a Variable?**

A variable stores a value in the computer's memory.
- Example: 
```python
x = 5
name = "Alice"
print(x, name)
```

**💡 Variables help store and reuse data in programs.**

<table>
    <tr>
        <th>Data Type</th>
        <th>Example</th>
    </tr>
    <tr>
        <td>String</td>
        <td><code>"Hello"</code></td>
    </tr>
    <tr>
        <td>Integer</td>
        <td><code>python script.py</code></td>
    </tr>
    <tr>
        <td>Float</td>
        <td><code>3.14</code></td>
    </tr>
    <tr>
        <td>Boolean</td>
        <td><code>True</code> or <code>False</code></td>
    </tr>
</table>

---

### 6️⃣ Debugging & Common Errors

**🛠️ Types of Errors in Python**

<table>
    <tr>
        <th>Error Type</th>
        <th>Example</th>
        <th>Solution</th>
    </tr>
    <tr>
        <td>Syntax Error</td>
        <td><code>print("Hello"</code>(missing <code>)</code>)</td>
        <td>Fix the syntax</td>
    </tr>
    <tr>
        <td>Name Error</td>
        <td><code>print(name)</code> (if <code>name</code> is not defined)</td>
        <td>Define variable first</td>
    </tr>
    <tr>
        <td>Type Error</td>
        <td><code>"2" + 2</code> (mixing types)</td>
        <td>Convert types using <code>int()</code> or <code>str()</code></td>
    </tr>
</table>

💡 Debugging Tips: 
- ✅ Read error messages carefully
- ✅ Print intermediate outputs (`print()`)
- ✅ Use Python's built-in `help()` function

---

## 🚀 HOW to Learn This?

### Step 1: Watch the Lecture & Take Notes

🎥 Watch CS50P's Week 0 Lecture → Write down key ideas:
- ✅ Python is interpreted, not compiled.
- ✅ `print()` is used to display output.
- ✅ Functions store reusable logic.
- ✅ Variables hold different types of data.

---

### Step 2: Hands-on Coding
**✅ Write this simple program:**
```python
name = input("What's your name? ")
print("Hello, " + name)
```
**✅ Modify it to include proper formatting:**
```python
name = input("What's your name? ").strip().title()
print(f"Hello, {name}!")
```

**💡 Use `.strip()` to remove extra spaces and `.title()` to capitalize names.**

---

### Step 3: Debugging Practice

🔎 Fix this broken code:
```python
print("Hello, world!"
```
**✅ Solution:** Add the missing closing parenthesis.

---

### Step 4: Mastery Checklist

- ✅ I installed Python and VS Code
- ✅ I ran my first Python program (`print()`)
- ✅ I understand how Python executes code line by line
- ✅ I used variables to store values
- ✅ I fixed at least one syntax error
