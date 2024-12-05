import subprocess


def compile_and_run(task_name, args):
    """
    Helper function to compile a task and run it with arguments.
    Returns the result of the subprocess.
    """
    # Compile the program
    compile_result = subprocess.run(
        ["gcc", "-o", task_name, f"tasks/{task_name}.c"], capture_output=True
    )
    if compile_result.returncode != 0:
        raise AssertionError(f"Compilation failed for {task_name}: {compile_result.stderr.decode()}")
    
    # Run the program with arguments
    run_result = subprocess.run([f"./{task_name}"] + args, capture_output=True, text=True)
    return run_result


def test_task1():
    """Test Task 1: Display Arguments"""
    result = compile_and_run("task1", ["Hello", "World"])
    output = result.stdout.strip().split("\n")
    assert "Argument 0: ./task1" in output
    assert "Argument 1: Hello" in output
    assert "Argument 2: World" in output


def test_task2():
    """Test Task 2: Sum Two Numbers"""
    result = compile_and_run("task2", ["5", "7"])
    assert result.stdout.strip() == "Sum: 12"

    # Test error handling with incorrect arguments
    result = compile_and_run("task2", ["5"])
    assert "Error: Please provide exactly two numbers." in result.stdout.strip()


def test_task3():
    """Test Task 3: Reverse the Arguments"""
    result = compile_and_run("task3", ["one", "two", "three"])
    assert result.stdout.strip() == "three two one"

    # Test error handling with no arguments
    result = compile_and_run("task3", [])
    assert "Error: No arguments to reverse." in result.stdout.strip()


def test_task4():
    """Test Task 4: Perform Operations Based on a Flag"""
    # Test addition
    result = compile_and_run("task4", ["add", "4", "6"])
    assert result.stdout.strip() == "Result: 10"

    # Test division
    result = compile_and_run("task4", ["divide", "8", "2"])
    assert result.stdout.strip() == "Result: 4"

    # Test unsupported operation
    result = compile_and_run("task4", ["power", "2", "3"])
    assert "Error: Unsupported operation. Use add, subtract, multiply, or divide." in result.stdout.strip()

    # Test missing arguments
    result = compile_and_run("task4", ["add", "5"])
    assert "Error: Please provide an operation and two numbers." in result.stdout.strip()

    # Test division by zero
    result = compile_and_run("task4", ["divide", "4", "0"])
    assert "Error: Division by zero is not allowed." in result.stdout.strip()


def test_task5():
    """Test Task 5: Count Word Frequency"""
    result = compile_and_run("task5", ["apple", "banana", "apple", "orange", "banana"])
    output = result.stdout.strip().split("\n")
    assert "apple: 2" in output
    assert "banana: 2" in output
    assert "orange: 1" in output

    # Test error handling with no arguments
    result = compile_and_run("task5", [])
    assert "Error: No words to count." in result.stdout.strip()
