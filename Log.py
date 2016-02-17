logging_enabled = True


def log(message):
    """ Create a log entry.

    Pretty barebones atm. Simply prints it to the console. Might be useful later on though.

    Args:
        message (str): The message to log.
    """
    if logging_enabled:
        print(message)
