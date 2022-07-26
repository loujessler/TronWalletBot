def is_number(message):
    try:
        float(message)
        return True
    except ValueError:
        return False