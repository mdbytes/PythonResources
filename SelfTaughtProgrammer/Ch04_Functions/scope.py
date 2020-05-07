# defining global x
x = 100 

def f():
    x = x+ 1 # x here is local (produces an exception)
    print(x)

# produces output of 101
def g():
    global x
    x = x + 1
    print(x)

f()
g()

    
