#--------------------------Functions---------------------------------


# _______________________________________________________
#|              Adding Sleep & Screen Times              |
#|_______________________________________________________|

'''Note: These two operate similarly, codes are identical'''

#Concerns inputting your Sleep Hours
def add_sleep(sleep_data):

    
    #Resets your sleep hours every time you add new sleeping hours of the week
    sleep_data = []
    print('\nEnter sleep hours for each day of the week:')
    
    #Ask user for input for all the days in the week
    for day in range(7):
        while True:
            val = input(f'Day {day+1}: ')
            
            #You are able to skip a day if you don't remember your hours
            if val == '':
                sleep_data.append(None)
                
                #Skips to the next day!
                break
            try:
                hours = float(val)

                if hours < 0 or hours > 24:
                    print('Invalid input. Enter a number between 0 and 24.')
                    continue

                sleep_data.append(hours)
                
                #Skips to the next day!
                break
            except ValueError:
                print('Invalid input. Enter a number or press Enter to skip.')
                
                #redoes the input until you enter a valid one
                continue
    return sleep_data


#Concerns inputting your Screen Time!
def add_screen(screen_data):

    #Resets your screen time everytime you add more every week
    screen_data = []
    print('\nEnter screen time hours for each day of the week:')
    
    #Ask user for input for all the days in the week
    for day in range(7):
        while True:
            val = input(f'Day {day+1} : ')
            
            #You are able to skip a day if you don't remember your hours
            if val == '':
                screen_data.append(None)
                
                #Skips to the next day!
                break

            try:
                hours = float(val)

                if hours < 0 or hours > 24:
                    print('Invalid input. Enter a number between 0 and 24.')
                    continue

                screen_data.append(hours)
                
                #Skips to the next day!
                break
            
            except ValueError:
                print('Invalid input. Enter a number or press Enter to skip.')
                
                #redoes the input until you enter a valid one
                continue
    return screen_data


# _______________________________________________________
#|             Adding & Clearing To-Do List              |
#|_______________________________________________________|

#Concerns adding a task to your To-Do List
def add_todo(todo_list):
    task = input('\nEnter a task for your to-do list: ')
    todo_list.append(task)
    print('Task added.')
    return todo_list

#Concerns clearing your whole To-Do List, only use if you are done with your previous
def clear_todo(todo_list):
    todo_list.clear()
    print('\nAll tasks removed and reset.')
    return todo_list


# _______________________________________________________
#|                   View Your Stats                     |
#|_______________________________________________________|

'''Same principles, mainly for visual cohesion'''

#Allows you to look at your all your statistics
def view_everything(sleep_data, screen_data, todo_list):

    print('\n              ___Your Habit Summary___\n\n')
    
    
    if sleep_data:
        print('                     __Sleep__')
        print(f'Sleep hours: {sleep_data}')
        
        valid_sleep = [s for s in sleep_data if s is not None]

        if valid_sleep:
            print('Average sleep:', round(sum(valid_sleep) / len(valid_sleep), 2))
        else:
            print("No valid sleep data.")
        
    #No input found
    else:
        print('\nNo sleep data available.')

    if screen_data:
        print('\n                  __Screen Time__')
        print(f'Screen time hours: {screen_data}')
        
        valid_sc = [s for s in screen_data if s is not None]

        if valid_sc:
            print('Average screen:', round(sum(valid_sc) / len(valid_sc), 2))
        else:
            print("No valid screen data.")
    
    #No input found
    else:
        print('\nNo screen time data available.')

    if todo_list:
        print('\n                 ___To-do List:___')
        for t in todo_list:
            print(f'- {t}')
    
    #No input found
    else:
        print('\nNothing to do.')


# _______________________________________________________
#|               Saving and Loading Files                |
#|_______________________________________________________|

#Allows you to save your current data for future input
def save_data(sleep_data, screen_data, todo_list):

    try:
        #'w' overwrites the previous habit_data file
        with open('habit_data.txt', 'w') as f:
            
            #Creates new 'Sleep:' list
            f.write('Sleep:\n')
            for sleep in sleep_data:
                f.write(f'{sleep}\n')
                
            #Creates new 'Screen:' list
            f.write('Screen:\n')
            for screen in screen_data:
                f.write(f'{screen}\n')
                
            #Creates new 'To-do:' list
            f.write('To-do:\n')
            for todo in todo_list:
                f.write(f'{todo}\n')
        
        #Confirms that it is in fact saved
        print('\nData saved successfully.')
        
    #Gives you the error that occured
    except Exception as ex:
        print(f'Error saving data: {ex}')


#Concerns loading the actual saved file
def load_data():
    
    #Creates a local list to call within this function
    sleep_data, screen_data, todo_list = [], [], []
    
    try:
        with open('habit_data.txt', 'r') as f:
            sect = None
            for line in f:
                line = line.strip()
                
                #Still continues after an empty space
                if not line:
                    continue
                
                #All below checks if the lines are under their respective categories
                if line.lower() == 'sleep:':
                    sect = 'sleep'
                elif line.lower() == 'screen:':
                    sect = 'screen'
                elif line.lower() == 'to-do:':
                    sect = 'to-do'
                else:
                    if sect == 'sleep':
                        if line == 'None':
                            sleep_data.append(None)
                        else:
                            sleep_data.append(float(line))
                    elif sect == 'screen':
                        if line == 'None':
                            screen_data.append(None)
                        else:
                            screen_data.append(float(line))
                    elif sect == 'to-do':
                        todo_list.append(line)
        #if sect == 'sleep':
        #Confirms the loading has worked
        print('\nData loaded successfully.')
    
    #No file found, pretty self explanatory
    except FileNotFoundError:
        print('\nNo saved data found. Please save data first.')
        
    #Gives Error found
    except Exception as ex:
        print(f'\nError loading data: {ex}')
        
    return sleep_data, screen_data, todo_list

# _______________________________________________________
#|                        MAIN                           |
#|_______________________________________________________|

'''Looks at user input and activates functions that correspond to that
- Allows you to access all resources
- Main Menu Options, etc
'''

def main():
    sleep_data, screen_data, todo_list = [], [], []


#I used this format to make it more readable on the interactive console
#Very visually appealing and straight-forward
    menu_text = '''
______________________

Choose an option:
1. Add Sleep Hours
2. Add Screen Time
3. Add To-do Task
4. Clear To-do Task
5. View Everything
6. Save Data
7. Load Data
8. Exit
______________________
'''

    print('\n*** Welcome to the Habit Tracker ***')
    _exit_ = False
    
    #Loops over your options until you choose 'exit'
    while not _exit_:
        choice = input(f'\n{menu_text}\n\nChoice: ')

        #Adding sleep time
        if choice == '1':
            sleep_data = add_sleep(sleep_data)
            
        #Adding screen time
        elif choice == '2':
            screen_data = add_screen(screen_data)
            
        #Adding to-do list
        elif choice == '3':
            todo_list = add_todo(todo_list)
        
        #Clearing to-do list
        elif choice == '4':
            todo_list = clear_todo(todo_list)
            
        #Viewing everything
        elif choice == '5':
            view_everything(sleep_data, screen_data, todo_list)
            
        #Saving your data
        elif choice == '6':
            save_data(sleep_data, screen_data, todo_list)
            
        #Loading saved data
        elif choice == '7':
            sleep_data, screen_data, todo_list = load_data()
            
        #Exit!!!
        elif choice == '8':
            print('Keep tracking those habits, goodbye!')
            _exit_ = True
        else:
            print('Invalid choice. Enter a number between 1-8.')

if __name__ == '__main__':
    main()
