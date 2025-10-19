# Calculator Project - Homework Assignment

## 📝 Homework Tasks

You need to implement the following methods in `app/calculator.py`:

1. **subtract(x, y)** - Subtract y from x (use the `-` operator)
2. **multiply(x, y)** - Multiply two numbers (use the `*` operator)
3. **divide(x, y)** - Divide x by y (use the `/` operator)
   - **Important:** Add a check for division by zero and raise a `ValueError` if y is 0
4. **power(x, y)** - Calculate x to the power of y (use the `**` operator)

### Example Implementation

Replace the `pass` statement in each method with the correct implementation:

```python
def subtract(self, x, y):
    """Subtract y from x."""
    return x - y  # Replace 'pass' with this
```

## 🧪 Testing Your Code

After completing the homework, test your calculator:

```bash
python main.py
```

**Expected output if everything works:**
```
✓ Addition test passed: 2 + 3 = 5
✓ Subtraction test passed: 10 - 4 = 6
✓ Multiplication test passed: 3 * 7 = 21
✓ Division test passed: 20 / 4 = 5.0
✓ Division by zero test passed: Cannot divide by zero
⚠ Power operation not implemented yet (homework): 2 ** 3 = None

✅ All calculator tests passed!
```

If you see any assertion errors, check your implementation!

---

## 🔧 Git & GitHub Workflow (Avoid Conflicts!)

Follow these steps carefully to submit your homework **without conflicts**:

### Step 1: Create Your Own Branch
Always work on your own branch with a unique name:

```bash
git switch -c yourname/homework
# Example: git switch -c john/homework
```

### Step 2: Check What Files Changed
Before committing, see what you modified:

```bash
git status
```

### Step 3: Add Your Changes
Add only the calculator file:

```bash
git add app/calculator.py
```

### Step 4: Commit Your Changes
Save your work with a clear message:

```bash
git commit -m "Complete calculator homework - implement subtract, multiply, divide, power"
```

### Step 5: Pull Latest Changes from Master (IMPORTANT!)
Before pushing, get the latest code to avoid conflicts:

```bash
git pull origin master --no-rebase
```

If there are conflicts, Git will tell you. If no conflicts, continue to Step 6.

### Step 6: Push Your Branch to GitHub
Upload your branch (not master!):

```bash
git push origin yourname/homework
# Example: git push origin john/homework
```

### Step 7: Create a Pull Request on GitHub
1. Go to the GitHub repository page
2. Click the green "Compare & pull request" button
3. Make sure the base branch is `master` and compare branch is `yourname/homework`
4. Add a title: "Homework Submission - [Your Name]"
5. Click "Create pull request"

---

## ⚠️ IMPORTANT RULES TO AVOID CONFLICTS

### ✅ DO:
- ✅ Always create your own unique branch name
- ✅ Pull latest changes before pushing (`git pull origin master`)
- ✅ Only modify `app/calculator.py` for this homework
- ✅ Push to YOUR branch, never directly to `master`
- ✅ Test your code with `python main.py` before submitting

### ❌ DON'T:
- ❌ Never work directly on the `master` branch
- ❌ Never use `git push --force` (this can delete others' work!)
- ❌ Don't modify files other than `app/calculator.py`
- ❌ Don't push without testing first
- ❌ Don't use the same branch name as another student

---

## 🆘 Troubleshooting

### Problem: "Your branch is behind origin/master"
**Solution:**
```bash
git pull origin master --no-rebase
```

### Problem: "Failed to push - rejected"
**Solution:**
```bash
# Make sure you're on your branch, not master
git branch  # Check current branch

# If you're on master by mistake:
git switch -c yourname/homework
git push origin yourname/homework
```

### Problem: Merge conflict after pulling
**Solution:**
1. Open the conflicting file (Git will mark conflicts with `<<<<<<<`, `=======`, `>>>>>>>`)
2. Edit the file to keep the correct code
3. Remove the conflict markers
4. Save the file
5. Run:
```bash
git add app/calculator.py
git commit -m "Resolve merge conflict"
git push origin yourname/homework
```

### Problem: Tests are failing
**Solution:**
- Read the error message carefully
- Check that you implemented all 4 methods (subtract, multiply, divide, power)
- Make sure divide() raises `ValueError` for division by zero
- Run `python main.py` to see which test fails

---

## 📚 Quick Reference

```bash
# Start working
git switch -c yourname/homework

# Save your work
git add app/calculator.py
git commit -m "Your message"

# Get latest changes
git pull origin master --no-rebase

# Upload your work
git push origin yourname/homework

# Then create Pull Request on GitHub
```

---

## ✨ Tips for Success

1. **Test early, test often** - Run `python main.py` after implementing each method
2. **Commit frequently** - Save your progress with small commits
3. **Read error messages** - They tell you exactly what's wrong
4. **Ask for help** - If you're stuck, reach out before the deadline
5. **Use descriptive branch names** - `firstname/homework` is clear and unique

Good luck with your homework! 🚀

