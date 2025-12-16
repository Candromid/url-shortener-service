import string 
import random

from .models import Link

def generate_short_code(length = 6):
    characters = string.ascii_letters + string.digits
    
    short_code = ''.join(random.choice(characters) for _ in range(length))
    
    if not Link.objects.filter(short_code = short_code).exists():
        return short_code