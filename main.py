import soldier_manager
import duty_manager
import utils


def show_menu() -> None:
    """print the menu."""
    print("""Select the action you want to perform:
          1. Adding a soldier to the list of soldiers.
          2. Removing a soldier from the list of soldiers.
          3.Printing the list of soldiers
          4.Adding a soldier to duty
          5.Duty status update
          6.Printing all of a soldier's duties
          7.exit.
          """)


def get_user_choice() -> int:
    """
    מקבלת בחירה מהמשתמש.
    
    מקבלת: כלום
    מחזירה: מחרוזת המייצגת את בחירת המשתמש
    
    למה הפונקציה קיימת:
    הפרדת קבלת קלט מהמשתמש מהלוגיקה של עיבוד הבחירה.
    מאפשר להחליף את שיטת הקלט בעתיד (למשל, GUI).
    """
    the_user_choice = input("Enter yor choice:")
    if not the_user_choice:
        raise ValueError

    try:
        if 0 < int(the_user_choice) < 7:
           return int(the_user_choice)
        else:
            raise ValueError("You must enter a number between 0 - 7")
    except ValueError:
        raise ValueError("You must enter a number between 0 - 7")


def handle_add_soldier(soldiers:list) -> None:
    """
    מטפלת בתהליך הוספת חייל חדש.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    מפרידה בין הקלט/פלט לבין הלוגיקה העסקית.
    main.py אחראי על אינטראקציה עם המשתמש,
    soldier_manager.py אחראי על הלוגיקה.
    """
    soldier_name = input("Enter the soldier name: ")
    try:
        soldier_id = int(input("Enter the soldier id: "))
    except TypeError:
        raise TypeError("you must enter a number.")
    
    soldier_manager.add_soldier(soldiers, soldier_id, soldier_name)


def handle_remove_soldier(soldiers:list) -> None:
    """
    מטפלת בתהליך הסרת חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    try:
        soldier_id = int(input("Enter the soldier id: "))
    except TypeError:
        raise TypeError("you must enter a number.")
    soldier_manager.remove_soldier(soldiers, soldier_id)


def handle_view_soldiers(soldiers:list) -> None:
    """
    מטפלת בתהליך הצגת כל החיילים.
    קוראת לפונקציה המתאימה ומציגה את התוצאה.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין קבלת הנתונים לבין הצגתם.
    """
    soldiers = soldier_manager.get_all_soldiers(soldiers)
    
    for soldier in soldiers:
        for key,value in soldier.items():
            if key != "duties":
                print(f"the soldier's {key} is {value}")
    
    return None


def handle_add_duty(soldiers:list) -> None:
    """
    מטפלת בתהליך הוספת תורנות לחייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    """
    try:
        soldier_id = int(input("Enter the soldier id: "))
    except TypeError:
        raise TypeError("you must enter a number.")
    
    duty_name = input("Enter the duty name: ")
    day = input("Enter the duty day: ")
    duty_manager.add_duty_to_soldier(soldiers, soldier_id, duty_name, day)
    
    return None
        

def handle_update_duty_status(soldiers:list) -> None:
    """
    מטפלת בתהליך עדכון סטטוס תורנות.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    """
    try:
        soldier_id = int(input("Enter the soldier id: "))
    except TypeError:
        raise TypeError("you must enter a number.")
    
    duty_name = input("Enter the duty name: ")
    new_status = input("Enter the new status: ")
    
    duty_manager.update_duty_status(soldiers, soldier_id, duty_name, new_status)

    return None


def handle_view_soldier_duties(soldiers:list) -> None:
    """
    מטפלת בתהליך הצגת תורנויות של חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    try:
        soldier_id = int(input("Enter the soldier id: "))
    except TypeError:
        raise TypeError("you must enter a number.")
    
    duty_manager.get_soldier_duties(soldiers, soldier_id)

    return None


def main() -> None:
    """
    הפונקציה הראשית של התוכנית.
    מריצה לולאה ראשית שמציגה תפריט, מקבלת בחירה ומפעילה פעולה.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    נקודת הכניסה לתוכנית. מנהלת את הזרימה הראשית.
    """
    while user_choice != 7:
        show_menu()
        try:
            user_choice = get_user_choice()
        except ValueError as e:
            print(e)