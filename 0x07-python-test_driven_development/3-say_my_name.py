#!/usr/bin/python3
"""
Introducing yourself, the cool way.
"""

def say_my_name(first_name, last_name=""):
    """
    What's your name? Oh wait, I know! Let me say it for you.
    Args:
        first_name (str): First name, needs to be a string.
        last_name (str): Last name, defaults to empty if you're cool like that.
    Returns:
        Nothing. It just prints your name in style.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
