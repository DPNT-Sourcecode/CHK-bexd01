

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    assert isinstance(friend_name, str)
    return "Hello, " + friend_name+"!"