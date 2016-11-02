import turtle as t

def crosses(length,iterations):
    if iterations <= 0:
        pass
    else:
        t.forward(length)
        t.left(90)
        crosses(length/2,iterations-1)
        t.right(90)
        crosses(length/2,iterations-1)
        t.right(90)
        crosses(length/2,iterations-1)
        t.left(90)
        t.back(length)

def main():
    crosses(100,3)
    t.done()

main()