error_counter = 0
with open("app.log") as file:
    for line in file:
        if "ERROR" in line:
            error_counter += 1

print(error_counter)