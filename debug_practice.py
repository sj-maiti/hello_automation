import time

def greet_user(name):
    """Simulate a greeting process."""
    print(f"Preparing to greet {name}...")
    time.sleep(1)  # simulate some delay
    greeting = f"Hello, {name}!"
    print("Greeting created.")
    return greeting

def calculate_square(numbers):
    """Calculate squares of a list of numbers."""
    print("Calculating squares...")
    result = []
    for n in numbers:
        square = n * n
        result.append(square)
        print(f"Square of {n} is {square}")
    print("All squares calculated.")
    return result

def summarize_results(name, squares):
    """Summarize the results."""
    print(f"Summarizing results for {name}...")
    total = sum(squares)
    average = total / len(squares)
    print(f"Total: {total}, Average: {average}")
    return {"total": total, "average": average}

if __name__ == "__main__":
    user_name = "Soumya"
    nums = [2, 4, 6, 8]

    # 🔴 Try setting breakpoints on these lines:
    greeting = greet_user(user_name)
    squares = calculate_square(nums)
    summary = summarize_results(user_name, squares)

    print("\nFinal Output:")
    print(greeting)
    print(summary)