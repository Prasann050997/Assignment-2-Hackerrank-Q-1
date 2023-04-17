# lambda function to find the cube
cube = lambda x: x ** 3

def fibonacci(n):

    a, b, c = 0, 1, 1
              
    # using for loop
    for i in range(n):
        yield a
        
        a, b = b, a + b
              
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))