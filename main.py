import soldier_manager
import duty_manager


def show_menu() -> None:
    """print the menu."""
    print("""Select the action you want to perform:
          1. Adding a soldier to the list of soldiers.
          2. Removing a soldier from the list of soldiers.
          3. Printing the list of soldiers
          4. Adding a soldier to duty
          5. Duty status update
          6. Printing all of a soldier's duties
          7. exit.
          """)


def get_user_choice() -> int:
    """Accepts a selection from the user, 
    returns it if it is valid and within the desired range, 
    otherwise raises an exception"""
    
    the_user_choice = input("Enter yor choice:")
    if not the_user_choice:
        raise ValueError

    try:
        if 0 < int(the_user_choice) <= 7:
           return int(the_user_choice)
        else:
            raise ValueError("You must enter a number between 0 - 7")
    except ValueError:
        raise ValueError("You must enter a number between 0 - 7")


def handle_add_soldier(soldiers:list) -> None:
    """Handles the process of adding a new soldier.
    Receives input from the user, checks and calls the appropriate functions. 
    If the input is invalid - raises exception"""

    soldier_name = input("Enter the soldier name: ")
    try:
        soldier_id = int(input("Enter the soldier id: "))
    except TypeError:
        raise TypeError("you must enter a number.")
    
    soldier_manager.add_soldier(soldiers, soldier_id, soldier_name)


def handle_remove_soldier(soldiers:list) -> None:
    """Handles the process of removing a soldier.
    Receives input from the user, checks and calls the appropriate functions. 
    If the input is invalid - raises exception"""
    try:
        soldier_id = int(input("Enter the soldier id: "))
    except TypeError:
        raise TypeError("you must enter a number.")
    
    soldier_manager.remove_soldier(soldiers, soldier_id)


def handle_view_soldiers(soldiers:list) -> None:
    """Handles the process of displaying the list of soldiers. 
    Receives nothing and returns None."""
    soldiers = soldier_manager.get_all_soldiers(soldiers)
    
    for i, soldier in enumerate(soldiers):
        print(f"soldier {i + 1}:")
        for key,value in soldier.items():
            if key != "duties":
                print(f"the soldier's {key} is {value}")
    
    return None


def handle_add_duty(soldiers:list) -> None:
    """Handles the process of add duty to a soldier.
    Receives input from the user, checks and calls the appropriate functions. 
    If the input is invalid - raises exception"""
    try:
        soldier_id = int(input("Enter the soldier id: "))
    except TypeError:
        raise TypeError("you must enter a number.")
    
    duty_name = input("Enter the duty name: ")
    day = input("Enter the duty day: ")
    duty_manager.add_duty_to_soldier(soldiers, soldier_id, duty_name, day)
    
    return None
        

def handle_update_duty_status(soldiers:list) -> None:
    """Handles the process of update duty status.
    Receives input from the user, checks and calls the appropriate functions. 
    If the input is invalid - raises exception"""
    try:
        soldier_id = int(input("Enter the soldier id: "))
    except TypeError:
        raise TypeError("you must enter a number.")
    
    duty_name = input("Enter the duty name: ")
    new_status = input("Enter the new status: ")
    
    duty_manager.update_duty_status(soldiers, soldier_id, duty_name, new_status)

    return None


def handle_view_soldier_duties(soldiers:list) -> None:
    """Handles the process of view a soldier duties.
    Receives input from the user, checks and calls the appropriate functions. 
    If the input is invalid - raises exception"""
    try:
        soldier_id = int(input("Enter the soldier id: "))
    except TypeError:
        raise TypeError("you must enter a number.")
    
    print(duty_manager.get_soldier_duties(soldiers, soldier_id))

    return None


def main(soldiers:list) -> None:
    """The main function of the program.
    Runs a main loop that displays a menu, accepts a selection, 
    and triggers an action."""
    
    functions_for_choice = {1:handle_add_soldier,
                            2:handle_remove_soldier,
                            3:handle_view_soldiers,
                            4:handle_add_duty,
                            5:handle_update_duty_status,
                            6:handle_view_soldier_duties}
    
    user_choice = None
    while user_choice != 7:
        show_menu()
        try:
            user_choice = get_user_choice()
        except ValueError as e:
            print(e)
            continue
        
        if user_choice != 7:
            try:
                functions_for_choice[user_choice](soldiers)
                print("=== done ===")
            
            except (ValueError, KeyError) as e:
                print(e)
    
    return None

main([])