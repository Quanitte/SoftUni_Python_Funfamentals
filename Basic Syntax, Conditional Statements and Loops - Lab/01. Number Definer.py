a = float(input())
if a == 0:
    print('zero')
elif 1 > a > 0:
    print('small positive')
elif -1 < a < 0:
    print('small negative')
elif a > 1000000:
    print('large positive')
elif a < -1000000:
    print('large negative')
elif a > 0:
    print('positive')
elif a < 0:
    print('negative')
