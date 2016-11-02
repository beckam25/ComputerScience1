def baz(n,count):
    if n >= 1:
        count = count + 1
        return baz(n//2,count)
    else:
        print(count)
def baz_iter(n):
    count=0
    while n>=1:
        count=count+1
        n=n//2
    print(count)
baz_iter(8)