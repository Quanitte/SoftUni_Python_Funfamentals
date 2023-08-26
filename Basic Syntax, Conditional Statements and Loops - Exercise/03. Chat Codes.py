a = int(input())
for i in range(a):
    num = int(input())
    if num == 88:
        print('Hello')
    elif num == 86:
        print('How are you?')
    elif not num == 88 and not num == 86 and num < 88:
        print('GREAT!')
    elif num > 88:
        print('Bye.')