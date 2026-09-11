import math
import matplotlib.pyplot as plt
 
 
def plot_function(fun_str, domain, ns):
    x0, x1 = domain
    dx = (x1 - x0) / (ns - 1)  # step size between points
 
    xs = []
    ys = []
    x = x0
    while x <= x1:
        xs.append(x)
        y = eval(fun_str)  # runs the typed-in function using the current x
        ys.append(y)
        x += dx
 
    # print a simple table, like the sample session shows
    print("{:>10} {:>10}".format("x", "y"))
    print("-" * 21)
    i = 0
    while i < len(xs):
        print("{:>10.4f} {:>+10.4f}".format(xs[i], ys[i]))
        i += 1
 
    plt.plot(xs, ys, "bo-")
    plt.show()
 
 
fun_str = input("Enter function with variable x: ")
xmin = float(input("Enter xmin: "))
xmax = float(input("Enter xmax: "))
n = int(input("Enter number of samples: "))
plot_function(fun_str, (xmin, xmax), n)