
user_input = input("Enter a word:  ")

user_input = "a".join(user_input.split())
user_input = "b".join(user_input.split())
user_input = "c".join(user_input.split())
user_input = "d".join(user_input.split())
user_input = "e".join(user_input.split())
user_input = "f".join(user_input.split())
user_input = "g".join(user_input.split())
user_input = "h".join(user_input.split())
user_input = "i".join(user_input.split())
user_input = "j".join(user_input.split())
user_input = "k".join(user_input.split())
user_input = "l".join(user_input.split())
user_input = "m".join(user_input.split())
user_input = "n".join(user_input.split())
user_input = "o".join(user_input.split())
user_input = "p".join(user_input.split())
user_input = "q".join(user_input.split())
user_input = "r".join(user_input.split())
user_input = "s".join(user_input.split())
user_input = "t".join(user_input.split())
user_input = "u".join(user_input.split())
user_input = "v".join(user_input.split())
user_input = "w".join(user_input.split())
user_input = "x".join(user_input.split())
user_input = "y".join(user_input.split())
user_input = "z".join(user_input.split())

#-------------Dictionary Convert To Soundex----------------
first_letter = (user_input.upper()[0])
user_input = user_input[1:]#removes first letter

user_input = user_input.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '').replace('y', '').replace('h', '').replace('w', '').replace(' ', '')
 #probably a better way to do this; will try and update later
user_input = user_input.replace('b', '1').replace('f', '1').replace('p', '1').replace('v', '1').replace('c', '2').replace('g', '2').replace('j', '2').replace('k', '2').replace('q', '2').replace('s', '2').replace('x', '2').replace('z', '2').replace('d', '3').replace('t', '3').replace('l', '4').replace('m', '5').replace('n', '5').replace('r', '6')

while True:
    if len(user_input) <  3:
        user_input = user_input + '0'
    else:
        break 

print(first_letter + user_input)
