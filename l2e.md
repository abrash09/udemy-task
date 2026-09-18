 Python Beginner-to-Medium Project Roadmap

A practical project-based roadmap for learning Python by building projects that are challenging enough to teach real programming skills without being overwhelming.

---

## How to Use This Roadmap

The projects are arranged progressively. Each project should introduce a few new concepts while reinforcing concepts learned previously.

### Recommended Learning Cycle

**Learn concept → Build feature → Get stuck → Research → Implement → Refactor → Add stretch feature**

Avoid following complete tutorials from start to finish. Instead, research specific problems when you get stuck.

For example:

> Instead of searching: "Build a Python expense tracker tutorial"

Search:

> "How to write JSON to a file in Python"

The goal is to learn how to solve problems, not copy complete solutions.

# Stage 1 — Python Fundamentals

## Project 1: Expense Tracker

### Goal

Build a terminal application that allows a user to record and analyze personal expenses.

### Core Features

- Add an expense
- Specify amount
- Specify category
- Add a description
- View all expenses
- Calculate total spending
- Calculate spending by category
- Delete an expense
- Save expenses to a file
- Load expenses when the program starts

### Example Data Model

```python
{
    "amount": 5000,
    "category": "Food",
    "description": "Lunch"
}
```

### Learning Objectives

#### Python Fundamentals
- Variables
- Strings
- Integers and floats
- Lists
- Dictionaries
- `if/else`
- `for` and `while` loops

#### Functions
- Creating functions
- Parameters
- Return values
- Breaking a program into smaller functions

#### Data Structures
Learn how dictionaries and lists can represent real-world information.

#### File Handling
- Reading files
- Writing files
- Saving application data
- Loading application data

#### Problem Solving
Learn to answer questions such as:
- How should an expense be represented?
- How should totals be calculated?
- How can expenses be grouped by category?

### Stretch Goal

Store expenses as JSON instead of plain text and use Python's `json` module.

---
