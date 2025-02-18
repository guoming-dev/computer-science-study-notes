# CS50P Week 5 - Unit Testing

🎯 Topic: Unit Testing and Writing Reliable Code

---

## 🧠 WHY Learn This?

Testing your code is just as important as writing it. Without tests, bugs can go unnoticed, leading to **unexpected errors, security issues, and broken functionality**. Unit tests allow you to **automate** the process of verifying that your code works as expected.

By mastering **unit testing**, you will:

- 🛡️ **Prevent bugs** by catching errors early.
- 🔄 **Ensure consistency** even when making code changes.
- 🤖 **Automate testing** to save time instead of manual debugging.
- 🏗️ **Improve software quality** by writing more reliable programs.

---

## 📌 WHAT You Need to Learn

### 1️⃣ What is Unit Testing?

Unit testing is the process of **testing individual functions or components** to ensure they work correctly.

- A **unit test** checks a **single function** or module.
- Unit tests are usually **automated** using a testing framework.
- **Good tests** cover normal cases, edge cases, and invalid inputs.

### 2️⃣ Writing a Basic Test Function

Instead of manually running your program multiple times to test it, you can write **automated tests**.

**Example: Square Function Test**

Suppose we have a function that squares a number:
```python
# calculator.py
def square(n):
    return n * n
```
**Basic Test Without Automation**
```python
print(square(2))    # Expect 4
print(square(3))    # Expect 9
```

This approach is **inefficient** because we have to manually check the output every time.

### 3️⃣ Using `assert` for Automated Testing

Instead of manually checking outputs, use **assertions**:
```python
# test_calculator.py
from calculator import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(0) == 0
```
**How it works**:

- If an assertion fails, Python throws an error.
- If no assertion fails, the function is correct.
- **No output** means all tests passed.

💡 **Key Point**: Assertions **only** check expected values. If incorrect, they raise an `AssertionError`.

### 4️⃣ Using `pytest` for Better Testing

Instead of manually running tests, we can use **pytest**, a testing framework.

**Installing pytest**
```bash
pip install pytest
```

**Running Tests with pytest**
```bash
pytest test_calculator.py
```

Expected output:
```bash
.
```
Each `.` represents a passed test. If a test fails, pytest shows detailed output.

**Testing for Expected Errors**

We can check whether a function correctly raises an error:
```python
import pytest
from calculator import square

def test_invalid_input():
    with pytest.raises(TypeError):
        square("cat")   # Expect TypeError
```
This ensures that invalid inputs don't break the program.

### 5️⃣ Handling Edge Cases

Good tests include:
- ✅ Positive numbers
- ✅ Negative numbers
- ✅ Zero
- ✅ Non-integer inputs (expecting errors)

Example:
```python
import pytest
from calculator import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0

def test_invalid_inputs():
    with pytest.raises(TypeError):
        square("hello")
    with pytest.raises(TypeError):
        square(3.5)
    with pytest.raises(TypeError):
        square([2, 3])
```

### 6️⃣ Organizing Tests in a Folder

For large projects, tests should be **separated** into folders.

**Setting Up a Test Folder**
```bash
mkdir tests
cd tests
touch test_calculator.py
```
Inside `test_calculator.py`:
```python
from calculator import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
```
Run all tests in the folder:
```bash
pytest tests/
```

---

## 🚀 HOW to Learn This?

### Step 1: Write Basic Tests

- 🧑‍💻 Start with `assert` statements.
- 🛠️ Run tests manually and check output.

### Step 2: Use pytest for Automation

- 🤖 Install pytest and run `pytest filename.py`.
- ✅ Fix any failing tests.

### Step 3: Test Edge Cases

- 🔥 Try invalid inputs like strings and floats.
- 📌 Ensure the function raises correct errors.

### Step 4: Organize Tests in Folders

- 🏗️ Move tests into a `tests/` directory.
- 🏆 Run `pytest tests/` to execute all tests.

---

## 📝 Summary and Key Insights

### Key Takeaways

- 🧪 **Unit tests ensure fucntions work correctly**.
- ✅ Use `assert` to check expected outputs.
- 🔄 Use `pytest` to **automate testing**.
- ⚠️ Test for **valid inputs, edge cases, and errors**.
- 📂 Organize tests in a `tests/` folder for better structure.

### Common Mistakes

- ❌ Not writing tests at all.
- ❌ Only testing "happy cases" (e.g., positive numbers).
- ❌ Ignoring error handling (e.g., `square("cat")`).
- ❌ Forgetting to use `pytest` for automation.

---

## ☘️ Checklist: Mastering Unit Testing

- ✅ I can write **basic tests** using `assert`.
- ✅ I have used `pytest` to **automate tests**.
- ✅ I have tested **edge cases** (negatives, zero, errors).
- ✅ I have organized my tests in a **separate folder**.
- ✅ I understand the importance of **writing tests early**.

*By mastering **unit testing**, you will write **bug-free, reliable, and scalable code!** 🚀*