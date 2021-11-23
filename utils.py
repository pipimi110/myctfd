from flask import session

def auth():
    if session.get('user') is None:
        return False
    else:
        return True

def test():
    print("test")