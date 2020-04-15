def prod(a,b):
    output = a*b
    return output

def fact_gen():
    i = 1
    n = i
    while True:
        output = prod(n, i)
        yield output
        i += 1
        n = output

my_gen = fact_gen()
num = 5
for i in range(num):
    print(next(my_gen))