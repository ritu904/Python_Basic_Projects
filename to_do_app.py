tasks =[]

def addTask():
    task= input("Please enter a task ")
    tasks.append(task)
    print(f"Task '{task}' has been added to the list.")

def listTask():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")

def deleteTask():
    listTask()
    try:
      taskToDelete = int(input("Enter the # to delete: "))
      if taskToDelete>=0 and taskToDelete < len(tasks):
          tasks.pop(taskToDelete)
          print (f"task {taskToDelete} has been deleted.")
      else:
          print(f"task {taskToDelete} was not found.")
    except:
        print("Invalid input.")



if __name__== "__main__" :
    while True:
        print("\n")
        print("Please select one of the following options:")
        print("------------------------------------------")
        print("1. Add task")
        print("2. Delete task")
        print("3. List task")
        print("4. Quit")

        choice = input ("Enter your choice: ")

        if (choice=="1"):
            addTask()
           
        elif (choice =="2"):
            deleteTask()

        elif (choice =="3"):
            listTask()

        elif (choice=="4"):
            break

        else :
           print("Invalid input. Please try again later.")

    print ("Good bye!!")





