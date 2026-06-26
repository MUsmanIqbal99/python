tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        for i in range(len(tasks)):
            print(i + 1, "-", tasks[i])

def add_task(task):
    tasks.append(task)

def remove_task(number):
    index = number - 1
    if index >= 0 and index < len(tasks):
        removed = tasks.pop(index)
        print("Removed:", removed)
    else:
        print("No task with that number.")

while True:
    print("\n1. Add task")
    print("2. Show tasks")
    print("3. Remove task")
    print("4. Quit")
    choice = input("Choose: ")

    if choice == "1":
        new_task = input("Enter task: ")
        add_task(new_task)
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        task_num = int(input("Task number to remove: "))
        remove_task(task_num)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")