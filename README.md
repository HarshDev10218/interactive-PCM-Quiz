# 🎯 Intermediate Quiz Application

A simple command-line quiz application written in Python that uses SQLite to store and retrieve questions. The quiz covers three subjects:

* 📐 Mathematics
* ⚛️ Physics
* 🧪 Chemistry

Users can choose a specific subject or take a mixed quiz containing questions from all subjects.

---

## Features

* Multiple-choice questions (A, B, C, D)
* Subject-wise quizzes
* Mixed quiz mode
* Random question selection
* Adjustable number of questions (1–10)
* Score calculation with percentage
* SQLite database storage
* Option to quit early during the quiz

---

## Requirements

* Python 3.x
* SQLite3 (included with Python)

No external libraries are required.

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd <repository-folder>
```

---

## Running the Program

Execute:

```bash
python Quiz.py
```

When started, the program:

1. Creates and initializes the database.
2. Inserts quiz questions.
3. Displays the available quiz channels.
4. Asks how many questions you want.
5. Starts the quiz and calculates your final score.

---

## Quiz Categories

### Mathematics

Topics include:

* Calculus
* Matrices
* Vectors
* Probability
* Complex Numbers
* Differential Equations

### Physics

Topics include:

* Mechanics
* Thermodynamics
* Electrostatics
* Optics
* Modern Physics
* Magnetism

### Chemistry

Topics include:

* Organic Chemistry
* Inorganic Chemistry
* Physical Chemistry
* Chemical Bonding
* Acids and Bases
* Crystal Structures

---

## Example

```
=== INTERMEDIATE LEVEL QUIZ CHANNELS ===

1. Mathematics
2. Physics
3. Chemistry
4. Mixed (All Subjects)

Choose a topic (1-4): 2
How many questions do you want? (default: 3): 5

--- Physics Quiz Starting ---

Q1: What is the SI unit of force?
A) Joule
B) Pascal
C) Newton
D) Watt

Your answer: C
Correct! Excellent.
```

---

## Database Schema

Table: `quiz_questions`

| Column         | Type    |
| -------------- | ------- |
| id             | INTEGER |
| subject        | TEXT    |
| question       | TEXT    |
| option_a       | TEXT    |
| option_b       | TEXT    |
| option_c       | TEXT    |
| option_d       | TEXT    |
| correct_answer | TEXT    |

---

## Future Improvements

* Difficulty levels (Easy, Intermediate, Advanced)
* Timer for each question
* Leaderboard system
* Save scores to database
* Graphical User Interface (Tkinter/PyQt)
* Add more subjects
* Import questions from CSV or JSON files

---

## Author

Created using **Python** and **SQLite**.

---

# interactive-PCM-Quiz
