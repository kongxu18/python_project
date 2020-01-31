
for i in range(ord('a'), ord('z')+1):
    print(chr(i), end='')

print('')

count = 0
for i in range(1,21):
    count += 1
    print(i, end='\n'if count % 5 == 0 else '')


