print('Hello', 'How are you?', end=',', sep='-')

def print_letter_count(text, letter='a'):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)
    

print_letter_count('How many letters a are here?')

print_letter_count()



    
    
