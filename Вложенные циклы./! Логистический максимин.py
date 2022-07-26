maxx = 1000000000
tunnel_of_maxx = 0
number_of_roads = int(input())
for i in range(1,number_of_roads+1):
    tunnel = int(input())
    for j in range(tunnel):
        hight = int(input())
        if hight<maxx:
            maxx = hight
            tunnel_of_maxx = i
print(tunnel_of_maxx, maxx)