def add_one (x: int) -> int:
    """Return one more than x.
    
    >>> add_one(1)
    2
    >>> add_one(5)
    6
    """
    return x + 1

def max_of_min(num1: float, num2: float, value1: float, value2: float) -> float:
    """Return the maximum of the minimums of the pairs num1 and num2,and value1 
    and value2

    >>> max_of_min (4.0, 3.7, 6.0, 3.5)
    3.7
    """
    
    min_num = min(num1, num2)
    min_value = min(value1, value2)
    return max(min(num1, num2), min(value1, value2))

def get_distance (x: float, y: float) -> float:
    """Return the distance between a point with coordinates (x, y) and the 
    origin.
    
    >>> get_distance (3.0, 4.0)
    5.0
    >>> get_distance (0.0, 0.0)
    0.0
    """
    # How about rewriting the function with a pow function instead of 
    # exponatiation?
    # pow(pow(x, 2) + pow(y, 2) , 2)
    return (x ** 2 + y ** 2) ** 2

def repeat_word(word: str, count:int) -> str:

    """ Return word repeated count times.
    
    Assume that: count >= 0
    
    >>>repeat_word('Marcia ', 3)
    'Marcia Marcia Marcia '
    >>>repeat_word('Mario', 2)
    'MarioMario'
    """
    return word * count

def format_name(first_name: str, last_name: str) -> str:
    
    """Return name in the format of 'last_name, first_name'.
    
    >>> format_name('Rin', 'Kagamine')
    'Kagamine, Rin'
    >>> format_name('Miku', 'Hatsune')
    'Hatsune, Miku'
    """
    return last_name + ', ' + first_name

def to_listening(first_name: str, last_name: str, phone_number: str) -> str:
    
    """Return name in the format of 'last_name, first_name, phone_number'.
    
    >>> to_listening('Miku', 'Hatsune', '39393939')
    'Hatsune, Miku: 39393939'
    """
    
    # return last name + ', ' + first_name + ': ' + phone_number
    return format_name(first_name, last_name) + ': ' + phone_number
