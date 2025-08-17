# To-Do List Using Python...............

tasks = []
FILE_NAME = 'tasks.txt'
ENCODING = 'utf-8'

def load_tasks():
    try:
        with open(FILE_NAME, 'r', encoding=ENCODING) as file:
            for line in file:
                tasks.append(line.strip())
                
    except FileNotFoundError:
        pass
            
def save_tasks():
    with open(FILE_NAME, 'w', encoding=ENCODING) as file:
        for task in tasks:
            file.write(f"{task}\n")    

def add_task():
    task = input("Enter task: ").strip()
    if task:
        tasks.append(task)
        print("✔ Task added successfully.")
    else:
        print("❌ Task is required!")

def view_task():
    if not tasks:
        print("❌ Your To-Do List is Empty!")
        return
    
    print("\n📌 Incompleted Tasks:")
    for i, task in enumerate([t for t in tasks if not t.startswith("✔")], start=1):
        print(f"{i}. {task}")
        
    print("\n✅ Completed Tasks:")
    for i, task in enumerate([t for t in tasks if t.startswith("✔")], start=1):
        print(f"{i}. {task}")  

def del_task():
    pending = [t for t in tasks if not t.startswith("✔ ")]
    completed = [t for t in tasks if t.startswith("✔ ")]
    
    print("\n---- Delete Task ----")
    print("1. Delete from pending")
    print("2. Delete from completed")
    
    try:
        choice = int(input("Choose an option: "))
        if choice == 1 and pending:
            for i, task in enumerate(pending,start=1):
                print(f"{i}. {task}")
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(pending):
                remove_task = pending[num - 1]
                tasks.remove(remove_task)
                print(f"✔ Deleted: {remove_task}")
            else:
                print("❌ Invalid task number!")
        
        elif choice == 2 and completed:
            for i, task in enumerate(completed,start=1):
                print(f"{i}. {task}")
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(completed):
                remove_task = completed[num - 1]
                tasks.remove(remove_task)
                print(f"✔ Deleted: {remove_task}")
            else:
                print("❌ Invalid task number!")
        else:
            print("❌ No tasks in that category!")
    except ValueError:
        print("❌ Please enter a valid number!")
        

def search_task():
    search = input("Enter task to search: ").strip()
    found = False
    for task in tasks:
        if search.lower() in task.lower():
            print(f"✔ Task found\n{task}")
            found = True
    if not found:
        print("❌ Task not found!")

def clear_task():
    print("\nYour Tasks:")
    if not tasks:
        view_task()
        return
    view_task()
    
    confirm = input("Do you want to clear all tasks? (yes/no): ").strip().lower()
    if confirm == "yes":
        tasks.clear()
        print("✔ All tasks are cleared.")
    else:
        print("❌ Cancelled! Tasks not cleared.!")

def mark_completed():
    pending = [t for t in tasks if not t.startswith("✔")]
    
    if not pending:
        print("❌ No pending tasks to mark!")
        return
    
    print("\n---- Pending Tasks ----")
    for i, task in enumerate(pending,start=1):
        print(f"{i}. {task}")
        
    try:
        choice = int(input("Enter task number to mark as completed: "))
        
        if 1 <= choice <= len(pending):
            task_to_mark = pending[choice - 1]
            index_in_main = tasks.index(task_to_mark)
            tasks[index_in_main] = "✔ " + task_to_mark
            print(f"✔ Task marked as  completed: {task_to_mark}")
        else:
            print("❌ Invalid task number!")
            
    except ValueError:
        print("❌ Please enter a valid number!")
    
    
def main():
    load_tasks()
    while True:
        print("\n----- To-Do List Menu -----")
        print("1. Add Task")
        print("2. View all Tasks")
        print("3. Delete a Task")
        print("4. Search a Task")
        print("5. Clear all Tasks")
        print("6. Mark task as completed")
        print("7. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_task()
            save_tasks()
        elif choice == "2":
            view_task()
        elif choice == "3":
            del_task()
            save_tasks()
        elif choice == "4":
            search_task()
        elif choice == "5":
            clear_task()
            save_tasks()
        elif choice == "6":
            mark_completed()
            save_tasks()
        elif choice == "7":
            print("🙌 Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please choose between (1-7).")

if __name__ == "__main__":
    main()
  
# ..................................................................................
