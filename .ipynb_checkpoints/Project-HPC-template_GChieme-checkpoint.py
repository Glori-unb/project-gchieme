# This library is necessary to get input from a text file.
# Note that this is intended for use on the clusters - the
# regular python library is simply "ast"
from asteval import Interpreter
aeval = Interpreter()

day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


# Insert your weekly report function
# Ensure the function takes 3 pieces of input - the task dictionary,
# habit dictionary, and file name to read the data.

def weekly_report(habit_dict, task_dict, file_name):
    habits = habit_dict #rename to match current code
    tasks = task_dict
    
    weekly_habit = [] #empty list for habits 
    if len(habits) == 0: #check to see if there are any tracked habits
        print("No habits tracked for this week.")
    else: 
        for w_habit, w_hday in habits.items(): #loop through habits 
            comp_rate = sum(1 for h_comp in w_hday.values() if h_comp == True) #completion rate is the amount of completed habits
            weekly_habit.append(f"{w_habit}: {comp_rate}/7 complete") #add to empty dictionary with "number/7 completed"
        print(f"Habits completion for this week are: {weekly_habit}")
    weekly_tasks_comp = [] #empty list for completed tasks
    weekly_tasks_incomp = [] #empty list for incompleted tasks
    if len(tasks) == 0: #check to see if there are any tracked tasks
        print("No tasks were tracked for this week.")
    else: 
        for w_tday, w_task in tasks.items(): #loop through the tasks and days 
            for w_task, w_comp in w_task.items(): #loop through the completion statements
                if w_comp == True:
                    weekly_tasks_comp.append(f"{w_task}({w_tday})") #completed tasks
                else:
                    weekly_tasks_incomp.append(f"{w_task}({w_tday})") #incompleted tasks
        if len(weekly_tasks_comp) == 0 and len(weekly_tasks_incomp) == 0: #an error as it would mean there are no tasks, or they're not marked as true/false
            print("Something has gone wrong! Try again!")
        elif len(weekly_tasks_comp) == 0:
            print(f"No completed tasks this week. The incompleted tasks were: {weekly_tasks_incomp}. Theres always next week!")
        elif len(weekly_tasks_incomp) == 0:
            print(f"Completed tasks were: {weekly_tasks_comp}. There are no incompleted tasks. Good job!")
        else: 
            print(f"Completed tasks this week were: {weekly_tasks_comp}. Good job! The incompleted tasks were: {weekly_tasks_incomp}. Theres always next week!")
    return 

# Provide the list of files to process.
# The dictionaries.txt files each contain a list of
# two dictionaries, the first being for habits and
# the second for tasks. 
#
# Note that the files and this python script should be in the
# same directory when you run it.
file_list = []
for n in range(1,11):
    file_list.append(f"dictionaries_{n}.txt")

# This section will loop through the files in the list above, and 
# run the report_week() function for each file. 
#
# The use of the ast library allows you to read text files
# that contain Python structures, in this case a list of dictionaries
#
# This code loops through each file, assigns the list of dictionaries
# as the variable 'data', then gives the report_week() function
# the appropriate input.
#
# Ensure you edit the final line so it matches your function name,
# and supply the appropriate input.
for file_name in file_list:
    with open(file_name) as f:
        content = f.read()
        data = aeval(content)
        weekly_report(data[0], data[1], file_name)