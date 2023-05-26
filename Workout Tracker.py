import csv
from csv import writer

# Defining Functions

# function that finds the workout for a date
def workout_finder(date):
    x = False
    workout = ''
    out = ''
    for i in outlist:
        if date == i[0]:
            x = True
            workout = i[1:]
    if x == True:
        out = f'Your workout for {date} is {workout}'
    elif x == False:
        out = "There is no workout for this date."
    return out


# Formatting the CSV File
with open("workouts.csv", 'w', newline='') as csvfile:
    row1 = ["Date", "Workout1", "Workout2", "Workout3", "Workout4", "Workout5", "Workout6", "Workout7", "Workout8",
            "Workout9", "Workout10"]
    outlist = csv.writer(csvfile)
    outlist.writerow(row1)


# Function to add workout to csv file
def workoutcsv(wo):
    with open("workouts.csv", 'a', newline='') as csvfile:
        outlist = csv.writer(csvfile)
        outlist.writerow(wo)


# Introduction to Program to user and setting some variables
choice_list = """What would you like to do?
[1]-Log a Workout?
[2]-Show Previous Workout
[3]-Workout from a date
[4]-Exit"""
display_lines = "--------------------------"
print(f"""{display_lines}
Workout Tracker.
{display_lines}
{choice_list}
{display_lines}""")
all_workouts = []
choice = 0
date = ''
choice_1_count = 0

# Beginning of loop for workouts
while choice != 4:
    choice = int(input("Choice> "))
    workout_num = 0

    if choice == 1:
        choice_1_count += 1
        total_workout = []
        workout = ''
        final_workout = ''
        print("Logging a Workout(Up to 10). Type Done for workout name when Finished Tracking")
        date = input("Input a date(Ex:3/4)> ")
        total_workout.append(date)
        for x in range(10):
            workout = ""
            workout_name = input(f"Workout {x + 1} name> ")
            if workout_name == "Done" or workout_name == "done":
                print(f"Your workout for {total_workout[0]} is {total_workout[1:]}")
                break

            workout_sets = input("Sets> ") + " Sets"
            workout_reps = input("Reps> ") + " Reps"
            workout_weight = input("Weight> ") + " Pounds"

            workout = f"{workout_name} for {workout_sets} of {workout_reps} and {workout_weight}"
            total_workout.append(workout)
        workoutcsv(total_workout)
        print(display_lines)
        print(choice_list)
        print(display_lines)

    elif choice == 2:
        out_print = ''
        if choice_1_count >= 1:

            with open("workouts.csv", 'r') as csvfile:
                outlist = list(csv.reader(csvfile, delimiter=','))
                out_print += f'Date:{outlist[-1][0]} - {outlist[-1][1:]}'
                print(out_print)
        else:
            print("No workouts available")
        print(display_lines)
        print(choice_list)
        print(display_lines)

    elif choice == 3:
        if choice_1_count >= 1:
            print('What date would you like to pull a workout from?')
            user_date = input('Date> ')
            with open("workouts.csv", 'r') as csvfile:
                outlist = list(csv.reader(csvfile, delimiter=','))
                out = workout_finder(user_date)
                print(out)
        else:
            print("No workouts available")
        print(display_lines)
        print(choice_list)
    elif choice != 4:
        print("That is not a choice")
        print(display_lines)
        print(choice_list)
print(display_lines)
print("Thanks for using Workout Tracker")
