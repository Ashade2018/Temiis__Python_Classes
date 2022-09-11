# #how to build an atm
# #pleese note that this is our second class
# toys=["tiger","pooh bear","piglet","rabbit","kanga","christopher robin","roo"]#list of my favourite toys
# foods=["plantain","bread","yam","egg","potatoes","salad","beans"]#lists of my favourite foods
# favourites= (toys +foods)
# print(favourites)
# first_name= 'Junia'
# last_name = 'Opatola'
# print('{} {}'.format(first_name,last_name))
# My Name
print('Welcome to My Adventure Game!')
print('Written by me')
print('You travel back in time to a land far away.')
print('Try to survive until you can get home!')
print('Available options are in CAPITAL letters or numbers')
print('Any other options exits the program')
print('OPTIONS: LOOK around')
go = input(':: ')
if go == 'LOOK':
    print('right here')
    print('OPTIONS: crawl out LEFT or RIGHT')
    crawl = input(':: ')
    if crawl == 'LEFT':
        print('right here')
        print('You survived!')
    elif crawl == 'RIGHT':
        print('write here')
        print('You did not survive')
else:
    print('You can only do actions given')
    print('Try again')