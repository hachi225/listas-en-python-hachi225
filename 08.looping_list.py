todo_list = ["sacar la basura", "barrer la entrada", "alimentar a Illuminati", "regar las plantas"]

for todo in todo_list:
    print(todo)

print("------------------------")

index = 0
while index < len(todo_list):
    print(todo_list[index])
    index += 1

[print(todo) for todo in todo_list]