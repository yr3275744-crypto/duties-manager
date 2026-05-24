import utils

def add_duty_to_soldier(soldiers:list, soldier_id: int, duty_name: str, day: str) -> None:
    """Adds a duty to a soldier, 
    raising exceptions accordingly if the soldier does not exist, 
    the duty name is invalid, or the duty day is invalid."""

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
    """Updates status to duty. 
    raising exceptions if the soldier's id does not appear, 
    if there is no such duty, 
    or the status is invalid."""

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
    """Returns the list of soldier's duties. 
    Raises an exception if soldier is not in the list."""
    the_soldier = utils.find_soldier_by_id(soldiers, soldier_id)
    
    if not the_soldier:
        raise KeyError("The soldier's id does not exist.")
    
    return the_soldier["duties"]