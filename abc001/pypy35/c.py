deg, des = map(int, input().split(' '))

# 2750 628
# 275.0
#
deg_mod = (deg + 112) // 225

deg_list = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
            'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']


def my_round(val, digit=0):
    p = 10 ** digit
    return (val * p * 2 + 1) // 2 / p


speed = my_round(des / 60, 1)
if speed <= 0.2:
    w = 0
elif speed <= 1.5:
    w = 1
elif speed <= 3.3:
    w = 2
elif speed <= 5.4:
    w = 3
elif speed <= 7.9:
    w = 4
elif speed <= 10.7:
    w = 5
elif speed <= 13.8:
    w = 6
elif speed <= 17.1:
    w = 7
elif speed <= 20.7:
    w = 8
elif speed <= 24.4:
    w = 9
elif speed <= 28.4:
    w = 10
elif speed <= 32.6:
    w = 11
else:
    w = 12

print('C' if w == 0 else deg_list[deg_mod], w)
