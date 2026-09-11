import math
import matplotlib.pyplot as plt

while True:
    a_str = input("Enter a: ")
    if a_str == "":
        break
    a = float(a_str)
    if a == 0:
        print("a cannot be 0")
        continue
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    disc = b**2 - 4*a*c  #lists number of real solutions 

    if disc < 0:
        print("no real solutions")
        x_opt = -b / (2*a) #no roots so we graph around the vertex
        x0 = x_opt - 5
        x1 = x_opt + 5
    elif disc == 0:
        root = -b / (2*a) #both roots are the same point
        print("one solution: {:.5f}".format(root))
        x0 = root - 5
        x1 = root + 5
    else:
        root1 = (-b - math.sqrt(disc)) / (2*a) 
        root2 = (-b + math.sqrt(disc)) / (2*a)
        print("two solutions: x1={:.5f} x2={:.5f}".format(root1, root2))
        x0 = min(root1, root2) - 3 
        x1 = max(root1, root2) + 3

    n = 150
    dx = (x1 - x0) / n
    xs = []
    ys = []
    x = x0
    while x <= x1:
        xs.append(x)
        y = a*x**2 + b*x + c
        ys.append(y)
        x += dx

    plt.plot(xs, ys, "b.")
    plt.show()