#keyword arguments
def print_details(**kwargs):
    print(kwargs)

#print_details(name="Alice", age=30, city="New York")

# display key and value
def print_details(**kwargs):
    for key, value in kwargs.items():
       print(f"{key}: {value}")

print_details(name="Alice", age=30, city="New York")
