def function(x):
    if x%2 == 0:
        print(x,"Is Even")
    else:
        print(x,"Is Odd")
def main():
    x=int(input("Enter a number: "))
    function(x)
    main()


main()