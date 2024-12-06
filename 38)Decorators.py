# These are function that take a function, update it a little and then return it

def pimp(fx):   # This will take the function you wanna decorate with your style (Decoartor function)
    def mfx(*args, **kwargs):  # This is funtion which will do what you want to
            # These are used to take all arguments as a tuple(*args) and dictionary(**kwargs) respectively

        print("I'm a pimp function!")
        fx(*args, **kwargs)
        print("That was guuud, see ya")

    return mfx

@pimp   # This is a decorator
def hello():
    print("I'm a hello!")

# pimp(hello)() # This is the same way to call as above

hello()