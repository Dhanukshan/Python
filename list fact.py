import math
if __name__ == "__main__":
    try:
        num_list = []
        for i in range(5):
            num = int(input(f"Enter number {i + 1}: "))
            num_list.append(num)
    except ValueError as e:
        print(f"Error: {e}")
    else:
        factorial_list = [math.factorial(num) for num in num_list]
        print("Sample Output")
        print(factorial_list)