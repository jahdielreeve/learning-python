#Practice if and elif

print('Enter a number:')
number = int(input('>'))
if number > 10:
    print('Too High')
elif number < 10:
    print('Too Low')
elif number == 10:
    print('Just right')