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

<table>
    <tr>
        <th>Pattern</th>
        <th>Description</th>
        <th>Example</th>
    </tr>
    <tr>
        <td><code>.</code></td>
        <td>Matches any character except newline</td>
        <td><code>"h.t"</code> matches <code>"hat"</code>, <code>"hit"</code>, <code>"hot"</code></td>
    </tr>
    <tr>
        <td><code>*</code></td>
        <td>Matches 0 or more repetitions</td>
        <td><code>"ca*t"</code> matches <code>"ct"</code>, <code>"cat"</code>, <code>"caaaat"</code></td>
    </tr>
    <tr>
        <td><code>+</code></td>
        <td>Matches 1 or more repetitions</td>
        <td><code>"ca+t"</code> matches <code>"cat"</code>, <code>"caaaat"</code> but <b>not</b> <code>"ct"</code></td>
    </tr>
    <tr>
        <td><code>?</code></td>
        <td>Matches 0 or 1 repetition</td>
        <td><code>"colou?r"</code> matches <code>"color"</code> and <code>"colour"</code></td>
    </tr>
    <tr>
        <td><code>{m}</code></td>
        <td>Matches m repetitions</td>
        <td><code>"a{2}"</code> matches <code>"aa"</code> but <b>not</b> <code>"a"</code>, <code>"aaa"</code>, <code>"aaaa"</code></td>
    </tr>
    <tr>
        <td><code>{m,n}</code></td>
        <td>Matches m to n repetitions</td>
        <td><code>"a{2,4}"</code> matches <code>"aa"</code>, <code>"aaa"</code>, <code>"aaaa"</code> but <b>not</b> <code>"a"</code></td>
    </tr>
</table>

### 3️⃣ Character Sets and Groups

You can define sets of characters inside `[]`.

<table>
    <tr>
        <th>Pattern</th>
        <th>Description</th>
        <th>Example</th>
    </tr>
    <tr>
        <td><code>[abc]</code></td>
        <td>Matches one of <code>a</code>, <code>b</code>, or <code>c</code></td>
        <td><code>"[abc]"</code> matches <code>"bat"</code> but <b>not</b> <code>"xyz"</code></td>
    </tr>
    <tr>
        <td><code>[a-z]</code></td>
        <td>Matches any lowercase letter</td>
        <td><code>"h[a-z]t"</code> matches <code>"hat"</code>, <code>"hit"</code>, <code>"hot"</code></td>
    </tr>
    <tr>
        <td><code>[^t]</code></td>
        <td>Matches any character <b>except</b> <code>t</code></td>
        <td><code>"[^t]"</code> matches <code>"bear"</code> but <b>not</b> <code>"beat"</code></td>
    </tr>
    <tr>
        <td><code>(abc)</code></td>
        <td>Capturing group (extracts substring)</td>
        <td><code>"(Mr|Ms)\. [A-Z][a-z]+"</code> matches <code>"Mr. Smith"</code> and <code>"Ms. Taylor"</code> but <b>not</b> <code>"Dr. Brown"</code></td>
    </tr>
</table>

### 4️⃣ Anchors for Position Matching

<table>
    <tr>
        <th>Pattern</th>
        <th>Description</th>
        <th>Example</th>
    </tr>
    <tr>
        <td><code>^</code></td>
        <td>Matches <b>start</b> of string</td>
        <td><code>"^Hello"</code> matches <code>"Hello world"</code> but <b>not</b> <code>"World Hello"</code></td>
    </tr>
    <tr>
        <td><code>$</code></td>
        <td>Matches <b>end</b> of string</td>
        <td><code>"world$"</code> matches <code>"Hello world"</code> but <b>not</b> <code>"worldwide"</code></td>
    </tr>
</table>

### 5️⃣ Shorthand Character Classes

<table>
    <tr>
        <th>Pattern</th>
        <th>Equivalent To</th>
        <th>Example</th>
        <th>Explanation</th>
    </tr>
    <tr>
        <td><code>\d</code></td>
        <td><code>[0-9]</code> (any digit)</td>
        <td><code>"\d{4}"</code> matches <code>"2023"</code></td>
        <td>Matches any <b>digit (0-9)</b>.</td>
    </tr>
    <tr>
        <td><code>\D</code></td>
        <td><code>[^0-9]</code> (not a digit)</td>
        <td>Matches <code>"hello"</code> but <b>not</b> <code>"123"</code></td>
        <td>Matches any <b>non-digit</b> character.</td>
    </tr>
    <tr>
        <td><code>\s</code></td>
        <td><code>[ \t\n\r\f\v]</code> (whitespace)</td>
        <td>Matches spaces and tabs</td>
        <td>Matches any <b>whitespace character</b> (spaces, tabs, newlines).</td>
    </tr>
    <tr>
        <td><code>\S</code></td>
        <td><code>[^\s]</code> (non-whitespace)</td>
        <td>Matches <code>"a"</code>, <code>"b"</code>, <code>"c"</code> in <code>"abc 123"</code></td>
        <td>Matches any <b>non-whitespace</b> character, including letters, numbers, and symbols.</td>
    </tr>
    <tr>
        <td><code>\w</code></td>
        <td><code>[a-zA-Z0-9_]</code> (word character)</td>
        <td>Matches <code>"hello123"</code> but <b>not</b> <code>"@#$"</code></td>
        <td>Matches <b>letters, digits, and underscores</b> (no spaces or symbols).</td>
    </tr>
    <tr>
        <td><code>\W</code></td>
        <td><code>[^\w]</code> (non-word character)</td>
        <td>Matches <code>"@"</code>, <code>"#"</code>, <code>" "</code> (space)</td>
        <td>Matches any <b>character that is NOT</b> a letter, digit, or underscore (includes spaces and punctuation).</td>
    </tr>
</table>


### 6️⃣ Using `re` Functions

**Finding Matches**
```python
import re

text = "My email is user@example.com"
pattern = r"\w+@\w+\.\w+"  # Basic email pattern
match = re.search(pattern, text)
if match:
    # Output: user@example.com
    print("Found:", match.group())
```

**Extracting All Matches**
```python
text = "Emails: alice@mail.com, bob@work.org"
pattern = r"\w+@\w+\.\w+"
matches = re.findall(pattern, text)
# Output: ['alice@mail.com', 'bob@work.org']
print(matches)
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
# Output: ['Apples', ' Bananas', ' Oranges ', ' Mangoes']
fruits = re.split(pattern, text)
print(fruits)
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