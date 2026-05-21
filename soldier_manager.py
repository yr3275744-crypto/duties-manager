import utils

def add_soldier(soldiers:list, soldier_id: int, name: str) -> None:
    """
    מוסיפה חייל חדש למערכת.
    
    מקבלת:
        soldier_id (int): מספר אישי של החייל
        name (str): שם החייל
    
    מחזירה:
        None - הפונקציה מוסיפה את החייל או זורקת exception
    
    זורקת:
        ValueError: אם id כבר קיים במערכת
        ValueError: אם name ריק או לא תקין
    
    למה הפונקציה קיימת:
    לוגיקה עסקית טהורה של הוספת חייל.
    מבצעת בדיקות תקינות ומוסיפה את החייל לנתונים.
    לא מטפלת בקלט/פלט - רק בלוגיקה.
    זורקת exceptions במקרה של שגיאה במקום להחזיר False.
    """
    if not utils.is_valid_name(name) or type(name) != str:
        raise ValueError
    
    if utils.find_soldier_by_id(soldier_id) or type(soldier_id) != int:
        raise ValueError
    
    soldiers.append({"id":soldier_id, "name":name, "dutiels":[]})
    return None


def remove_soldier(soldiers:list, soldier_id: int) -> None:
    """
    מסירה חייל מהמערכת לפי id.

    מקבלת:
        soldier_id (int): מספר אישי של החייל
    
    מחזירה:
        None - הפונקציה מסירה את החייל או זורקת exception
    
    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת
    
    למה הפונקציה קיימת:
    לוגיקה עסקית של הסרת חייל.
    מבצעת בדיקת קיום ומסירה מהנתונים.
    זורקת exception במקרה שהחייל לא קיים.
    """
    the_soldier = utils.find_soldier_by_id(soldier_id)
    
    if not the_soldier:
        raise KeyError
    
    soldiers.remove(the_soldier)
    


def get_all_soldiers(soldiers:list) -> list:
    """
    מחזירה את רשימת כל החיילים במערכת.
    
    סוג: גישה לנתונים (Data Access)
    
    מקבלת: כלום
    
    מחזירה:
        list: רשימה של מילונים, כל מילון מייצג חייל
              רשימה ריקה אם אין חיילים
    
    זורקת: כלום - תמיד מחזירה רשימה (ריקה או מלאה)
    
    למה הפונקציה קיימת:
    גישה לנתונים בצורה מבוקרת.
    מאפשר לקבל את הנתונים מבלי לגשת ישירות למשתנה הגלובלי.
    """
    return soldiers
