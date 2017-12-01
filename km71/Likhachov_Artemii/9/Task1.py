def distance(x1, y1, x2, y2):
    return (pow(x2-x1,2)+pow(y2-y1,2))**(1/2)

a, b, c, d = [int(i) for i in input().split()]
print(distance(a, b, c, d))
