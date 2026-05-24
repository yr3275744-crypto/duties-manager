import utils

def add_duty_to_soldier(soldiers:list, soldier_id: int, duty_name: str, day: str) -> None:
    """
    מוסיפה תורנות חדשה לחייל.
    
    מקבלת:
        soldier_id (int): מספר אישי של החייל
        duty_name (str): שם התורנות
        day (str): יום בשבוע (sunday/monday/tuesday/wednesday/thursday)
    
    מחזירה:
        None - הפונקציה מוסיפה את התורנות או זורקת exception
    
    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת
        ValueError: אם תורנות עם שם זה כבר קיימת לחייל
        ValueError: אם day לא חוקי (friday/saturday או ערך לא תקין)
    
    למה הפונקציה קיימת:
    לוגיקה עסקית של הוספת תורנות.
    מבצעת בדיקות ומוסיפה תורנות לחייל.
    זורקת exceptions במקרה של שגיאה במקום להחזיר False.
    """
    the_soldier = utils.find_soldier_by_id(soldiers, soldier_id)
    
    if not utils.is_valid_name(duty_name):
        raise ValueError("You must enter a full name, not empty string")

    if not the_soldier:
        raise KeyError("The soldier's id does not exist.")
    
    if utils.soldier_has_duty(the_soldier, duty_name):
        raise ValueError("The duty already exists.")
    
    if not utils.is_valid_day(day):
        raise ValueError("You must enter a duty day.")
    
    if the_soldier.get("duties"):
        the_soldier["duties"].update({"name":duty_name, "day":day})
    else:
        the_soldier["duties"] = [{"name":duty_name, "day":day}]

    return None

def update_duty_status(soldiers:list, soldier_id: int, duty_name: str, new_status: str) -> None:
    """
    מעדכנת את הסטטוס של תורנות.
    
    מקבלת:
        soldier_id (int): מספר אישי של החייל
        duty_name (str): שם התורנות
        new_status (str): סטטוס חדש (pending/completed/missed)
    
    מחזירה:
        None - הפונקציה מעדכנת את הסטטוס או זורקת exception
    
    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת
        KeyError: אם תורנות עם שם זה לא נמצאה לחייל
        ValueError: אם new_status לא חוקי (לא pending/completed/missed)
    
    למה הפונקציה קיימת:
    לוגיקה עסקית של עדכון סטטוס.
    מבצעת בדיקות ומעדכנת את הסטטוס.
    זורקת exceptions במקרה של שגיאה במקום להחזיר False.
    """
    the_soldier = utils.find_soldier_by_id(soldiers, soldier_id)

    if not the_soldier:
        raise KeyError("The soldier's id does not exist.")
    
    if not utils.find_duty_by_name(the_soldier["duties"], duty_name):
        raise KeyError("The duty does not exists")
    
    if not utils.is_valid_status(new_status):
        raise ValueError("You must enter a valid ststus.")
    
    the_duty = utils.find_duty_by_name(the_soldier["duties"], duty_name)
    the_duty["status"] = new_status


def get_soldier_duties(soldiers:list, soldier_id: int) -> list:
    """
    מחזירה את רשימת התורנויות של חייל.
    
    סוג: גישה לנתונים (Data Access)
    
    מקבלת:
        soldier_id (int): מספר אישי של החייל
    
    מחזירה:
        list: רשימת תורנויות (מילונים)
              רשימה ריקה אם אין תורנויות
    
    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת
    
    למה הפונקציה קיימת:
    גישה מבוקרת לתורנויות של חייל.
    מפרידה בין הנתונים לבין הגישה אליהם.
    זורקת exception אם החייל לא קיים (במקום להחזיר רשימה ריקה).
    """
    the_soldier = utils.find_soldier_by_id(soldiers, soldier_id)
    
    if not the_soldier:
        raise KeyError("The soldier's id does not exist.")
    
    return the_soldier["duties"]