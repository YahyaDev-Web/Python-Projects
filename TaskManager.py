print("-------------- Task Manager ✔ --------------")

# things i need for the project
import datetime

tasks = []


def main():
    while True:
        options = """
        1. Add task to list
        2. Mark task as complete
        3. View tasks
        4. Quit
        """
        print(options)
        choice = input("Enter your choice: ")


        # Choices 
        if choice == "1":
            add_tasks()
        elif choice == "2":
            check_tasks()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            break
        else:
            print("⛔ Invalid Choice , Please enter a valid choice")
def add_tasks():
    try:
        # ask user about task
        task = input("Enter task: ")
        # check if the task is empty
        if not task:
             print("📪 Task cannot be empty .")
             return
        # get the date from the user
        task_date = input("Enter task date (yyyy-mm-dd): ")

        # convert the date to int (date)
        year , month , day = map(int, task_date.split("-"))

        # use date func 
        date_tasks = datetime.date(year,month,day)

        # add the task to the list
        task_info = {"Task": task , "Date": date_tasks, "Completed": False}
        tasks.append(task_info)
        # pint that the taks is added to the list
        print("Task added to the list succesfully.")

    except ValueError:
         print("Please, enter a date in yyyy-mm-dd format")



def check_tasks():
    try:
        incomplete_tasks = [task for task in tasks if not task["Completed"]]
        if incomplete_tasks:
            for i,task in enumerate(incomplete_tasks):
                print(f"{i+1}. {task['Task']}")
            num_task = int(input("Enter the number of the task to mark as complete: "))
            incomplete_tasks[num_task - 1]["Completed"] = True
            print("Task Marked as complete")
        else:
            print("Empty List.")
    except IndexError:
        print(f"Please Enter between 1 and {len(incomplete_tasks)}.")
    except ValueError:
        print("Please enter a number not a string.")
def view_tasks():
    # print the task to the user 
    if tasks:
       for i,task in enumerate(tasks):
            task_status = "✔" if task["Completed"] else "❌"
            print(f"{i+1}. {task['Task']} ({task['Date'].strftime('%Y-%m-%d')}) {task_status}")
    else:
        print("📪 The list is empty, Please add some tasks.")



if __name__ == "__main__":
    main()

