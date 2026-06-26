tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        for i in range(len(tasks)):
            print(i + 1, "-", tasks[i])

def add_task(task):
    tasks.append(task)


while True:
    print("\n1. Add task")
    print("2. Show tasks")
    print("3. Quit")
    choice = input("Choose: ")

    if choice == "1":
        new_task = input("Enter task: ")
        add_task(new_task)
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")