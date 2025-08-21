import csv

class Task:
    def __init__(self, name, desc, priority):
        self.name = name
        self.desc = desc
        self.priority = priority
        
    def __str__(self):
        return f"{self.name} ({self.priority}) - {self.desc}"

class ToDoList:
    def __init__(self, filename="tasks.csv"):
        self.filename = filename
        self.tasks = []
        self.load_from_csv()

    # user adds to do list tasks
    def add_task(self, task):
        self.tasks.append(task)
        self.save_to_csv()

    # user removes certain tasks from the to do list
    def remove_task(self, name):
        for task in self.tasks:
            if task.name == name:
                self.tasks.remove(task)
                self.save_to_csv()
                return True
        return False

    # user views the to do list and its tasks
    def show_tasks(self):
        if not self.tasks:
            print("No tasks added to the list.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}.{task}")
           
    # to do list and tasks are saved in a csv file 
    def save_to_csv(self):
        try:
            with open(self.filename, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Description", "Priority"])

                for task in self.tasks:
                    writer.writerow([task.name, task.desc, task.priority])
                    
        except Exception as error:
            print("Error in saving:", error)
    
    # loading to do list csv file
    def load_from_csv(self):
        try:
            with open(self.filename, "r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                
                for row in reader:
                    task = Task(row["Name"], row["Description"], row["Priority"])
                    self.tasks.append(task)
                    
        except FileNotFoundError:
            pass
        except Exception as error:
            print("Error in loading:", error)
            
# main menu of the program
def menu():
    todo = ToDoList()
    
    while True:
        try:
            print("\n~~~~~~~~ To Do List Menu ~~~~~~~~")
            print("1. Add task")
            print("2. Remove Task")
            print("3. Show Tasks")
            print("4. Exit")

            choice = input("Enter 1, 2, 3, or 4: ")

            # add task
            if choice == "1":
                name = input("Task Name: ")
                desc = input("Description: ")
                priority = input("Priority (High, Medium, Low): ")
                
                task = Task(name, desc, priority)
                
                todo.add_task(task)
                
                print("Task Added ✅")
                
            # remove task
            elif choice == "2":
                name = input("Name of the Task you want to remove: ")
                if todo.remove_task(name):
                    print("Task Removed ✅")
                else:
                    print("Task Not Found ❌")
                
            # show to do list
            elif choice == "3":
                todo.show_tasks()
                
            # exit
            elif choice == "4":
                print("Exiting...")
                break
            
            else:
                print("Invalid Input. Try again...")

        except Exception as error:
            print("An error has occured", error)

    print("\nProgram was successfully implemented.")
            
if __name__ == "__main__":
    menu()
