# hasattr() detects that an obj already exists

class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'): # If an instance exists => serve the same obj again
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

s = Singleton()
print("Object created: ", s)

s1 = Singleton()
print("Object created: ", s1)

# Another method to implement
class Singleton1:
    __instance = None
    def __init__(self):
        if not Singleton1.__instance:
            print("__init__ method called!")
        else:
            print("Instance already created: ", self.getInstance())
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton1()
        return cls.__instance

s = Singleton1()
print("Object created: ", s.getInstance())

s1 = Singleton1()











