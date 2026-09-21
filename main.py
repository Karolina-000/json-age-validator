import json

with open("users.json", "r", encoding="utf-8") as file:
    users = json.load(file)

success_count = 0
fail_count = 0

for user in users:
    if user["age"] >= 18:
        print(f"{user['name']} - წარმატებულია")
        success_count += 1
    else:
        print(f"{user['name']} - წარუმატებელია")
        fail_count += 1

print("Success:", success_count)
print("Fail:", fail_count)
