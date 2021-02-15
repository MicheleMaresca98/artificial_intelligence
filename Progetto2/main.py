from math import cos

import optimization as op
from numpy import linspace
from matplotlib.pyplot import plot, xlabel, ylabel, show, xscale, yscale, legend
def cost(x):
    x=x[0]
    if x<5.2:
        y=10
    elif 5.2<=x<=20:
        y=pow(x,2)
    elif x>20:
        y=cos(x)+160*x
    return 16001-y

def costi(x):
    if x<5.2:
        y=10
    elif 5.2<=x<=20:
        y=x**2
    elif x>20:
        y=cos(x)+160*x
    return y

D1 = linspace(-100,5.2,1000)
D2 = linspace(5.2,20,1000)
D3 = linspace(20,100,1000)
plot(D1, [10 for x in D1], label="y=10")
plot(D2, [x**2 for x in D2], label="y=x^2")
plot(D3, [cos(x)+160*x for x in D3], label="y=cos(x)+160*x")
xlabel("x")
ylabel("y=f(x)")
legend(loc="upper left", shadow=True)
show()

def run():
    domain=[(-100,100)]
    x=op.hillclimb(domain, cost)[0]
    print('x:',x)
    y=costi(x)
    print('F(x):',y)

    print('Nel caso in cui lo facciamo ripartire più volte')
    h=[0,0,0,0,0,0,0,0,0,0,0]
    valutazioni=[0,0,0,0,0,0,0,0,0,0,0]
    for i in range(1,11):
        h[i]=op.hillclimb(domain, cost)[0]
        print('Posizione (x):',h[i])
        valutazioni[i]=costi(h[i])
        print('Valutazione (F(x)):',valutazioni[i])
    massimo=max(valutazioni)
    print('Massimo raggiunto (F(x)):',massimo)


run()

