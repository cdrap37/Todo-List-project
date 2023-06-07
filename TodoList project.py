import datetime

class TodoList: 
    def __init__(self):
        self.tasks = []
    
     #The constructor method initializes an empty list to store tasks.
    
    
    def add_task(self, task):  #Method to add a task to the todo list.
        self.tasks.append(task)
    
    
    
    
    def remove_task(self, task): #Method to remove a task from the todo list.
        self.tasks.remove(task)
    
    
    
   
    def view_tasks(self): #Method to view all the tasks in the todo list.
        for task in self.tasks:
            print(task)
   
    
    
    
    def clear_tasks(self): #Method to clear all the tasks from the todo list.
        self.tasks.clear()
    


class Task:
    def __init__(self, description): #The constructor method for Task class. It initializes the description attribute and sets the current date and time as the created_at attribute.
        self.description = description
        self.created_at = datetime.datetime.now()
    
    

    
    def __str__(self): #The __str__ method is overridden to provide a user-friendly string representation of a Task object.
        return f"{self.description} (Created at: {self.created_at})"
    


if __name__ == "__main__":
    todo_list = TodoList()

    while True:
        print("\n==== Todo List ====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Clear Tasks")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            description = input("Enter task description: ")
            task = Task(description)
            todo_list.add_task(task)
            print("Task added successfully!")

        elif choice == "2":
            if todo_list.tasks:
                print("Select a task to remove:")
                for index, task in enumerate(todo_list.tasks):
                    print(f"{index + 1}. {task}")
                task_index = int(input("Enter the task number to remove: ")) - 1
                if 0 <= task_index < len(todo_list.tasks):
                    task = todo_list.tasks[task_index]
                    todo_list.remove_task(task)
                    print("Task removed successfully!")
                else:
                    print("Invalid task number!")
            else:
                print("No tasks to remove!")

        elif choice == "3":
            if todo_list.tasks:
                print("\n==== Tasks ====")
                todo_list.view_tasks()
            else:
                print("No tasks to display!")

        elif choice == "4":
            todo_list.clear_tasks()
            print("All tasks cleared!")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number from 1 to 5.")
