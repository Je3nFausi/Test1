# working with default values
def login(username, isadmin=False):
    print(f"The name is {username} and the status is this {isadmin}")

print(login("Dennis",True))
print(login("Dennis"))