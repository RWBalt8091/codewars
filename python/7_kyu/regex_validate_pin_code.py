def validate_pin(pin):
    try:
        int(pin)
        
        if len(pin) == 4:
            return True
        elif len(pin) == 6:
            return True
        else:
            return False
    except:
        return False