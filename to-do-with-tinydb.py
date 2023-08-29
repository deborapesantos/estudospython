from tinydb import TinyDB, Query

class TodoItem:
    def __init__(self, task, completed=False):
        self.task = task
        self.completed = completed

class TodoList:
    def __init__(self, db_file):
        self.db = TinyDB(db_file)
        self.todo_table = self.db.table("todo")

    def add_task(self, task):
        self.todo_table.insert({"task": task, "completed": False})

    def mark_task_completed(self, task):
        self.todo_table.update({"completed": True}, Query().task == task)

    def get_tasks(self, show_completed=False):
        tasks = self.todo_table.all()
        if not show_completed:
            tasks = [task for task in tasks if not task["completed"]]
        return tasks

def main():
    db_file = "todo_db.json"
    todo_list = TodoList(db_file)

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Mark Task Completed")
        print("3. View Tasks")
        print("4. View Completed Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
            print("Task added successfully!")

        elif choice == "2":
            task = input("Enter task to mark as completed: ")
            todo_list.mark_task_completed(task)
            print("Task marked as completed!")

        elif choice == "3":
            tasks = todo_list.get_tasks()
            if tasks:
                print("\nCurrent Tasks:")
                for idx, task in enumerate(tasks, start=1):
                    status = "✓" if task["completed"] else " "
                    print(f"{idx}. [{status}] {task['task']}")
            else:
                print("No tasks in the list.")

        elif choice == "4":
            completed_tasks = todo_list.get_tasks(show_completed=True)
            if completed_tasks:
                print("\nCompleted Tasks:")
                for idx, task in enumerate(completed_tasks, start=1):
                    print(f"{idx}. [✓] {task['task']}")
            else:
                print("No completed tasks.")

        elif choice == "5":
            print("Exiting To-Do List.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
