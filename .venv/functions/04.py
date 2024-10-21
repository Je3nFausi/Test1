def calculate_statistics(numbers):
    """

    doc string / Documentation String
    
    Functionality of the function
    Calculate total, count, average

    parameters:
    list of numbers

    return:
    total, count, average
    """
    total = sum(numbers)
    count = len(numbers)
    average = total / count if count != 0 else 0
    return total, count, average

argument_numbers = [1, 2, 3, 4, 5]
total, count, average = calculate_statistics(argument_numbers)
print(f"Total: {total}, Count: {count}, Average: {average}")