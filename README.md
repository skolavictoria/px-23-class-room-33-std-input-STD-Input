# README: Understanding Standard Input in C (CLI Arguments)

This repository provides a comprehensive tutorial for learning and practicing **standard input** (CLI arguments) in C programming. It includes detailed explanations, example outputs, and tasks to practice concepts progressively.

---

## **Project Structure**

Ensure your project follows this structure:

```
project/
│
├── tasks/
│   ├── task1.c  # Task 1: Display Arguments
│   ├── task2.c  # Task 2: Sum Two Numbers
│   ├── task3.c  # Task 3: Reverse the Arguments
│   ├── task4.c  # Task 4: Perform Operations Based on a Flag
│   ├── task5.c  # Task 5: Count Word Frequency
│
├── tests/
│   ├── test_tasks.py  # Pytest for Task 1
│
├── README.md          # This file
```

---

## **How to Perform Tasks**

Each task requires writing a program in C that takes **command-line arguments** (CLI arguments) and produces specific outputs. Below are the requirements, expected inputs, and outputs for each task.

---

### **Task 1: Display the Arguments**

**Objective**: Create a program (`task1.c`) that prints all arguments passed to it, one per line, along with their index.

**Expected Inputs and Outputs**:
- **Input**: CLI arguments (any number of strings).
- **Output**:
  ```bash
  $ ./task1 Hello World
  Argument 0: ./task1
  Argument 1: Hello
  Argument 2: World
  ```

---

### **Task 2: Sum Two Numbers**

**Objective**: Create a program (`task2.c`) that takes exactly two numbers as arguments and prints their sum.

**Expected Inputs and Outputs**:
- **Input**: Two integers.
- **Output**:
  ```bash
  $ ./task2 5 7
  Sum: 12
  ```

**Error Handling**:
- If fewer or more than two numbers are provided:
  ```bash
  $ ./task2 5
  Error: Please provide exactly two numbers.
  ```

---

### **Task 3: Reverse the Argument Order**

**Objective**: Create a program (`task3.c`) that reverses the order of arguments and prints them on a single line.

**Expected Inputs and Outputs**:
- **Input**: CLI arguments (any number of strings).
- **Output**:
  ```bash
  $ ./task3 one two three
  three two one
  ```

**Error Handling**:
- If no arguments are provided:
  ```bash
  $ ./task3
  Error: No arguments to reverse.
  ```

---

### **Task 4: Perform Operations Based on a Flag**

**Objective**: Create a program (`task4.c`) that performs basic operations (addition, subtraction, multiplication, division) based on a flag argument.

**Expected Inputs and Outputs**:
- **Input**: A flag (`add`, `subtract`, `multiply`, `divide`) followed by two numbers.
- **Output**:
  ```bash
  $ ./task4 add 4 6
  Result: 10

  $ ./task4 divide 8 2
  Result: 4
  ```

**Error Handling**:
- If an unsupported flag is provided:
  ```bash
  $ ./task4 power 2 3
  Error: Unsupported operation. Use add, subtract, multiply, or divide.
  ```

- If fewer arguments are provided:
  ```bash
  $ ./task4 add 5
  Error: Please provide an operation and two numbers.
  ```

- If division by zero is attempted:
  ```bash
  $ ./task4 divide 4 0
  Error: Division by zero is not allowed.
  ```

---

### **Task 5: Count Word Frequency**

**Objective**: Create a program (`task5.c`) that counts how many times each word appears in the arguments.

**Expected Inputs and Outputs**:
- **Input**: CLI arguments (words).
- **Output**:
  ```bash
  $ ./task5 apple banana apple orange banana
  apple: 2
  banana: 2
  orange: 1
  ```

**Error Handling**:
- If no arguments are provided:
  ```bash
  $ ./task5
  Error: No words to count.
  ```
