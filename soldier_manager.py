import utils

def add_soldier(soldiers:list, soldier_id: int, name: str) -> None:
    """Adds a new soldier to the list.
    Gets the list of soldiers, the soldier's id and name,
    adds it or raises exceptions 
    if it exists in the system or the name is invalid."""
    
    if not utils.is_valid_name(name):
        raise ValueError("You must enter a full name, not empty string")
    
    if utils.find_soldier_by_id(soldiers, soldier_id):
        raise ValueError("The soldier's id already exists.")
    
    soldiers.append({"id":soldier_id, "name":name, "duties":[]})
    
    return None


def remove_soldier(soldiers:list, soldier_id: int) -> None:
    """Removes a soldier from the list by id. 
    If the soldier does not exist - raises exception"""
    
    the_soldier = utils.find_soldier_by_id(soldiers, soldier_id)
    
    if not the_soldier:
        raise KeyError("The soldier's id does not exist.")
    
    soldiers.remove(the_soldier)
    


def get_all_soldiers(soldiers:list) -> list:
    """Receives the list of soldiers and returns it."""
    
    return soldiers
