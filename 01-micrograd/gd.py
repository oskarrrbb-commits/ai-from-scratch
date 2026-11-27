import os

#y = 3x

xs = [1, 2, 3, 4, 5]
ys = [3, 6, 9, 12, 15]

h = 0.0001
lr = 0.01

def loss (w):
    total = 0
    for x, y in zip(xs, ys):
        total = ((w * x - y) **2) + total
    return total/len(xs)

w = 0


for i in range(5000):
    slope = (loss(w + h) - loss(w))/h
    w = w - lr * slope
    loss(w)
    print(loss(w),": ", w, ": ", i)
