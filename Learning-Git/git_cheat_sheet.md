# Git Cheat Sheet for Projects

## 📌 Project Setup Checklist

### 1️⃣ Create a GitHub Repository

1. Go to [GitHub](https://github.com) and log in.
2. Click on **New Repository**.
3. Fill in the details:
   - Repository Name: `YourProjectName`
   - Description: Short summary of the project.
   - Visibility: Public or Private.
4. Leave **Initialize Repository** unchecked if starting locally, or check it if you want a README/.gitignore.
5. Click **Create Repository**.

---

### 2️⃣ Clone the Repository Locally

Run the following commands in your terminal:
```bash
# Clone the GitHub repository to your machine
git clone https://github.com/<your-username>/YourProjectName.git

# Navigate into the project directory
cd YourProjectName
```

---

### 3️⃣ Add Project Files

1. Create necessary files and directories for your project:
   ```bash
   touch README.md main.py requirements.txt
   ```
2. Add content to these files using your text editor or IDE.

---

### 4️⃣ Track and Commit Changes

1. Stage your changes:
   ```bash
   git add .
   ```
2. Commit the changes:
   ```bash
   git commit -m "Initial commit: added base files"
   ```

---

### 5️⃣ Push Changes to GitHub

Push your local changes to the remote repository:
```bash
git push origin main
```

---

## 📌 Daily Git Workflow

### 1️⃣ Sync Your Local Branch

Always start by pulling the latest changes from the remote repository:
```bash
git pull origin main
```

---

### 2️⃣ Create a Feature Branch

Use branches for new features or bug fixes:
```bash
git checkout -b feature/your-feature-name
```

---

### 3️⃣ Work on the Feature

After completing your changes:

1. Stage the changes:
   ```bash
   git add .
   ```
2. Commit the changes:
   ```bash
   git commit -m "Implemented [feature-name]"
   ```

---

### 4️⃣ Merge Feature Branch into Main

1. Switch back to the main branch:
   ```bash
   git checkout main
   ```
2. Merge the feature branch:
   ```bash
   git merge feature/your-feature-name
   ```

---

### 5️⃣ Push the Updated Main Branch

```bash
git push origin main
```

---

## 📝 Useful Git Commands

### Basic Commands

<table>
    <tr>
        <th>Command</th>
        <th>Description</th>
    </tr>
    <tr>
        <td><code>git init</code></td>
        <td>Initialize a new local Git repository.</td>
    </tr>
    <tr>
        <td><code>git clone &lt;repo-url&gt;</code></td>
        <td>Clone a remote repository to your machine.</td>
    </tr>
    <tr>
        <td><code>git add &lt;file&gt;</code></td>
        <td>Stage changes for commit.</td>
    </tr>
    <tr>
        <td><code>git commit -m "message"</code></td>
        <td>Commit staged changes with a message.</td>
    </tr>
    <tr>
        <td><code>git push origin &lt;branch&gt;</code></td>
        <td>Push changes to the remote branch.</td>
    </tr>
    <tr>
        <td><code>git pull origin &lt;branch&gt;</code></td>
        <td>Pull the latest changes from the remote branch.</td>
    </tr>
</table>

---

### Branch Management

<table>
    <tr>
        <th>Command</th>
        <th>Description</th>
    </tr>
    <tr>
        <td><code>git branch</code></td>
        <td>List all local branches</td>
    </tr>
    <tr>
        <td><code>git branch &lt;branch-name&gt;</code></td>
        <td>Create a new branch.</td>
    </tr>
    <tr>
        <td><code>git checkout &lt;branch-name&gt;</code></td>
        <td>Switch to an existing branch.</td>
    </tr>
    <tr>
        <td><code>git checkout -b &lt;branch-name&gt;</code></td>
        <td>Create and switch to a new branch.</td>
    </tr>
    <tr>
        <td><code>git merge &lt;branch-name&gt;</code></td>
        <td>Merge a branch into the current branch.</td>
    </tr>
</table>

---

### Conflict Resolution

<table>
    <tr>
        <th>Command</th>
        <th>Description</th>
    </tr>
    <tr>
        <td><code>git status</code></td>
        <td>Check the status of your working directory.</td>
    </tr>
    <tr>
        <td><code>git add &lt;file&gt;</code></td>
        <td>Mark conflict-resolved files as staged.</td>
    </tr>
    <tr>
        <td><code>git commit</code></td>
        <td>Commit resolved conflicts.</td>
    </tr>
    <tr>
        <td><code>git merge --abort</code></td>
        <td>Abort a merge in progress.</td>
    </tr>
</table>

---

### Undo Changes

<table>
    <tr>
        <th>Command</th>
        <th>Description</th>
    </tr>
    <tr>
        <td><code>git checkout -- &lt;file&gt;</code></td>
        <td>Discard changes in the working directory.</td>
    </tr>
    <tr>
        <td><code>git reset HEAD &lt;file&gt;</code></td>
        <td>Unstage a file but keep changes.</td>
    </tr>
    <tr>
        <td><code>git revert &lt;commit&gt;</code></td>
        <td>Revert a specific commit.</td>
    </tr>
</table>

---

## 💭 Pro Tips

1. **Write Clear Commit Messages**: Use descriptive messages that explain what the commit does.
2. Use Branches for Features: Keep the `main` branch clean and stable.
3. Pull Before Pushing: Always pull the latest changes from the remote branch before pushing.
4. Avoid Force Pushes: Use `git push -f` only if absolutely necessary.
5. Use Git Aliases: Save time by creating shortcuts for commonly used commands.

---

This cheat sheet is designed to help you manage your Git projects efficiently. 🚀