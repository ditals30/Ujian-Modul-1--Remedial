# NOMER 1
def find_short(words):
    mins = min(len(word) for word in words.split())
    print(f'The shortest word has {mins} char(s)')

words = input('Input words: ')

find_short(words)

#NOMER 2

def persistence(number):
    product = 1
    persistence = 0
    if int(number) < 0:
        print('Please input positive numbers only')
    else:
        while int(number) > 9:
            for digit in range(0, len(str(number))):
                product *= int(str(number)[digit])
            print(product)
            persistence += 1
            number = product
            product = 1
        print(f'So it takes {persistence} times multiplication until we get a single digit')

number = input('Input number: ')
persistence(number)
