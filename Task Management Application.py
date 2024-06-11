def add_task(tasks):
    try:
        n = input("Enter a task: ")
        tasks.append(n)
    except ValueError:
        print("Invalid Input!")

def show_task(tasks):
    if len(tasks)==0:
        print("You dont have any task to do.")
    for i, value in enumerate(tasks):
        print(f"{i+1} : {value}")

def completed_task(task,comp_task):
    try:
        n = int(input("Which Task have you completed? PLease choose the index of that Task"))
    except ValueError:
        print("Invalid Input! Please Enter the index of a task")
    for i in range(len(task)+1):
        if i == n:
            comp_task.append(task[i-1])
            task.remove(task[i-1])
    print(comp_task)

def clear_tasks(task):
    task.clear()
    print("All the tasks have been cleared")
    return task

def delete_certain_task(task):
    try:
        n = int(input("Which Task have you completed? PLease choose the index of that Task"))
        if n<1 or n>len(task):
            print("Invalid Index")
    except ValueError:
        print("Invalid Input! Please Enter the index of a task")
    deleted_task = task.pop(n-1)
    print(f"{deleted_task} has been deleted")


def main():
    task = []
    comp_task = []
    while True:
        n = int(input("Enter 1 to add task/ 2 to mark completed task/ 3 to delete task / 4 to show the tasks/ 5 to clear the task and 6 to close your application."))
        if n==1:
            add_task(task)
        elif n==2:
            completed_task(task,comp_task)
        elif n==3:
            delete_certain_task(task)
        elif n==4:
            show_task(task)
        elif n==5:
            task = clear_tasks(task)
        elif n==6:
            print("Exiting the application. Say Goodbye")
            break
        else:
            print("Invalid Input! Please Enter a Valid input")


if __name__ == "__main__":
    main()

