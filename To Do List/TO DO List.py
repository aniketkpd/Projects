import csv
import pandas as pd


# Global declaration
mylist = []

dataset = pd.read_csv('my_tasks.csv')
dataset.columns = ['Task Name','Status']



# To add tasks to preexisting task list
def create_task(task=None ,status = 'incomplete'):
    
    mylist.append([task,status])

    with open('my_tasks.csv','a', newline='') as file:
        
        # Convert data to csv format
        writer_obj = csv.writer(file)
        
        # Wright all the data to csv
        writer_obj.writerows(mylist)


# To view existing tasks
def view_task():
    dataset = pd.read_csv('my_tasks.csv')
    print() #Space for readability
    print(dataset)



# To remove a single task
def remove_task():
    
    rm = int(input("Enter index of task to remove it: "))
    
    dataset.drop(index=rm, inplace=True)
    
    dataset.to_csv('my_tasks.csv',index=False)
    
    print("\nTask removed\n")


# To remove all the task and reset the task list
def remove_all_tasks():
    x,y = dataset.shape
    
    for i in range(x):
        dataset.drop(index = i,inplace=True)
        dataset.to_csv('my_tasks.csv',index=False)


    print("\nAll tasks Removed\n")



# To mark the task as it is completed
def markAsComplete(index_of_task):
    
    x = dataset.values[index_of_task] 
    x[1] = 'Completed'
    
    dataset.to_csv('my_tasks.csv',index=False)

    print('\nYour Task is now Marked as Completed\n')




#User choice
while True:


    print("\n=== Available Choices ===")
    print("1. View Tasks")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Reset : Remove all Task")
    print("5. Mark a task as Complete")
    print("6. Exit")
    
    try:
        choice = int(input("Enter your choice: "))
    except:
        print('Use only numbers to navigate')
        continue
      

    if choice == 1:
        view_task()
        
    elif choice == 2:
        task = input("Enter task : ")
        create_task(task)
        
    elif choice == 3:
        remove_task()

    elif choice == 4:
        remove_all_tasks()
    
    elif choice == 5:
        
        task_number = int(input("Enter index of that task you have completed: "))
        markAsComplete(task_number)

    elif choice == 6:
        exit()
        
    else:
        print("Enter a valid option.")