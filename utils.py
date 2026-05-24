STATUSES = ["pending", "completed", "missed"]
DUTIES_DAYS = ["sunday", "monday", "tuesday", "wednesday", "thursday"]


def find_soldier_by_id(soldiers:list, soldier_id: int) -> dict | None:
    """Checks for the existence of a soldier in the soldiers list. 
    Returns it if it exists, otherwise None"""

    for soldier in soldiers:
        if soldier["id"] == soldier_id:
            return soldier

        return None


def find_duty_by_name(duties: list, duty_name: str) -> dict | None:
    """Searching for a duty by name in the duties list. 
    return the duty if exists, slse None"""
    
    for duty in duties:
        if duty["name"] == duty_name:
            return duty
        
    return None


def is_valid_status(status: str) -> bool:
    """Checks whether a status appears in the list of valid statuses. 
    Returns a Boolean value accordingly."""
    
    status = status.lower()
    
    if status in STATUSES:
        return True
    else:
        return False


def is_valid_name(name: str) -> bool:
    """Checks whether a name is not empty.
    Returns a Boolean value accordingly."""

    return True if name else False


def soldier_has_duty(soldier: dict, duty_name: str) -> bool:
    """Checks whether a soldier has a specific duty.
    Returns a Boolean value accordingly."""

    for duty in soldier["duties"]:
        if duty["name"] == duty_name:
            return True
        else:
            return False
    
    return False


def is_valid_day(day: str) -> bool:
    """Checks whether a day appears in the list of duties days. 
    Returns a Boolean value accordingly."""

    return True if day in DUTIES_DAYS else False
    
