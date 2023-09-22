import sys

for element in sys.stdin:
    if 'q' == element.rstrip():
        break
    else:
        print(f'Input:{element}')

print('Exit')


import sys
num = sys.stdin.readline()
print(num)


