# CS50P Week 7 - Regular Expressions (Regex)

🎯 Topic: Pattern Matching with Regular Expressions in Python

---

## 🧠 WHY Learn This?

**Regular Expressions (regex)** provide a **powerful way to search, match, and manipulate text**. Instead of manually writing multiple conditions for string validation, regex allows you to define **patterns** that match complex text structures in a concise manner.

By mastering **Regex**, you will:

- 🔍 **Search for patterns** in strings efficiently.
- ✅ **Validate user input** (e.g., emails, phone numbers).
- 🧹 **Extract and clean** messy text data.
- 🔄 **Replace substrings** programmatically.

---

## 📌 WHAT You Need to Learn

### 1️⃣ Basic Regular Expressions in Python

Python provides a built-in `re` module to work with regular expressions.

**Importing** `re`
```python
import re
```

**Basic Syntax**
```python
# Checks if pattern exists in string
re.search(pattern, string)
# Checks if string starts with pattern
re.match(pattern, string)
# Returns all matches
re.findall(pattern, string)
# Replaces pattern with new text
re.sub(pattern, replacement, string)
```

### 2️⃣ Pattern Matching Fundamentals

Regular expressions use **special symbols** to define patterns.

| Pattern  | Description                          | Example  |
|----------|--------------------------------------|------------------------------------------------------|
| `.`      | Matches any character except newline | `"h.t"` matches `"hat"`, `"hit"`, `"hot"` |
| `*`      | Matches 0 or more repetitions        | `"ca*t"` matches `"ct"`, `"cat"`, `"caaaat"` |
| `+`      | Matches 1 or more repetitions        | `"ca+t"` matches `"cat"`, `"caaaat"` but **not** `"ct"` |
| `?`      | Matches 0 or 1 repetition            | `"colou?r"` matches `"color"` and `"colour"` |
| `{m,n}`  | Matches m to n repetitions          | `"a{2,4}"` matches `"aa"`, `"aaa"`, `"aaaa"` but **not** `"a"` |


### 3️⃣ Character Sets and Groups

You can define sets of characters inside `[]`.

| Pattern  | Description                          | Example  |
|----------|--------------------------------------|----------------------------------------------------------|
| `[abc]`  | Matches one of `a`, `b`, or `c`     | `"[abc]"` matches `"bat"` but **not** `"xyz"` |
| `[a-z]`  | Matches any lowercase letter        | `"h[a-z]t"` matches `"hat"`, `"hit"`, `"hot"` |
| `[^t]`   | Matches any character **except** `t` | `"[^t]"` matches `"bear"` but **not** `"beat"` |
| `(abc)`  | Capturing group (extracts substring) | `"(Mr|Ms)\. [A-Z][a-z]+"` matches `"Mr. Smith"`, `"Ms. Taylor"` but **not** `"Dr. Brown"` |


### 4️⃣ Anchors for Position Matching

| Pattern  | Description                  | Example  |
|----------|------------------------------|----------------------------------------------------------|
| `^`      | Matches **start** of string  | `"^Hello"` matches `"Hello world"` but **not** `"World Hello"` |
| `$`      | Matches **end** of string    | `"world$"` matches `"Hello world"` but **not** `"worldwide"` |

### 5️⃣ Shorthand Character Classes

| **Pattern** | **Equivalent To** | **Example** | **Explanation** |
|------------|-----------------|------------|----------------|
| `\d` | `[0-9]` (any digit) | `"\d{4}"` matches `"2023"` | Matches any **digit (0-9)**. |
| `\D` | `[^0-9]` (not a digit) | Matches `"hello"` but **not** `"123"` | Matches any **non-digit** character. |
| `\s` | `[ \t\n\r\f\v]` (whitespace) | Matches spaces and tabs | Matches any **whitespace character** (spaces, tabs, newlines). |
| `\S` | `[^\s]` (non-whitespace) | Matches `"a"`, `"b"`, `"c"` in `"abc 123"` | Matches any **non-whitespace character**, including letters, numbers, and symbols. |
| `\w` | `[a-zA-Z0-9_]` (word character) | Matches `"hello123"` but **not** `"@#$"` | Matches **letters, digits, and underscores** (no spaces or symbols). |
| `\W` | `[^\w]` (non-word character) | Matches `"@"`, `"#"`, `" "` (space) | Matches any **character that is NOT a letter, digit, or underscore** (includes spaces and punctuation). |

### 6️⃣ Using `re` Functions

**Finding Matches**
```python
import re

text = "My email is user@example.com"
pattern = r"\w+@\w+\.\w+"  # Basic email pattern

match = re.search(pattern, text)
if match:
    print("Found:", match.group())  # Output: user@example.com
```

**Extracting All Matches**
```python
text = "Emails: alice@mail.com, bob@work.org"
pattern = r"\w+@\w+\.\w+"

matches = re.findall(pattern, text)
print(matches)  # Output: ['alice@mail.com', 'bob@work.org']
```

**Replacing Text** (`re.sub`)
```python
text = "My phone is 123-456-7890"
pattern = r"\d{3}-\d{3}-\d{4}"

new_text = re.sub(pattern, "XXX-XXX-XXXX", text)
print(new_text)  # Output: My phone is XXX-XXX-XXXX
```

**Splitting Strings** (`re.split`)
```python
text = "Apples, Bananas; Oranges | Mangoes"
pattern = r"[,;|]"

fruits = re.split(pattern, text)
print(fruits)  # Output: ['Apples', ' Bananas', ' Oranges ', ' Mangoes']
```

---

## 🚀 HOW to Learn This?

### Step 1: Understand Basic Patterns

- 🔎 Experiment with `.` `*` `+` `?` `{m,n}`
- 🧑‍💻 Test regex in an online regex tester (e.g., [regex101](https://regex101.com))
  
### Step 2: Practice Pattern Matching

- ✅ Create regex for **emails, phone numbers, dates**.
- 📝 Extract specific patterns from **text files**.

### Step 3: Use `re` in Python Scripts

- 🏗️ Build small projects like:
  - ✉️ **Email validator**
  - ☎️ **Phone number extractor**
  - 📄 **Log file parser**

### Step 4: Work with Real Data

- 🔄 Use regex to **clean messy datasets** (e.g., CSV files).
- 🔎 Search and replace **patterns in text**.

---

## 📝 Summary and Key Insights

### Key Takeaways

- 🏆 Regular Expressions simplify text processing.
- 🔍 `re.search()`, `re.match()`, `re.findall()` help **find patterns**.
- 🔄 `re.sub()` and `re.split()` allow **text replacement & splitting**.
- 🎭 Regex uses **wildcards, quantifiers, and character sets**.
- ⚓️ Use **anchors** (`^ $`) and **shorthands** (`\d \w \s`) for precision.

### Common Mistakes

- ❌ Forgetting to escape `.` (Use `\.` to match a literal period).
- ❌ Using `*` instead of `+` (Allows zero matches, may lead to unexpected results).
- ❌ Not using raw strings (`r"pattern"`) to avoid escape character confusion.
- ❌ Forgetting to use `()` for capturing groups when extracting data.

---

## ☘️ Checklist: Mastering Regex in Python

- ✅ I can match **basic patterns** (e.g., email, phone numbers).
- ✅ I understand **shorthands** (`\d`, `\w`, `\s`).
- ✅ I can use `re.search()`, `re.findall()`, `re.sub()`.
- ✅ I can extract **specific data from text**.
- ✅ I have built **at least one real-world project** using regex.

*By mastering regular expressions, **you will handle text processing tasks efficiently**! 🚀*