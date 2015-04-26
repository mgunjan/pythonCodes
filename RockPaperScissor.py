import sys
import random

def game():
    gesture_list = ['Rock', 'Paper', 'Scissors']
    dic_game ={"Paper":"Rock",'Scissors':'Paper','Rock':'Scissors'}
    print('Welcome to the Game of Rock-Paper-Scissors Game!****\n')

    while True :
        print('The available Gesture are:')
        print('\t0:Rock\n\t1:Paper\n\t2.Scissors')

        g = int(input('Please select your gesture(-1 to exit):'))
        if g == -1:
            sys.exit()
        while g> 2 or g < 0:
            g = int(input('Please select your gesture(-1 to exit):'))
            if g == -1:
                sys.exit() 
        gesture = gesture_list[g]
        print('Your Gesture is {}'.format(gesture))
        r = random.randrange(3)
        my_gesture= gesture_list[r]
        print('My Gesture is {}'.format(my_gesture))

        if dic_game[gesture]== my_gesture:
            print('Your are the Winner')

        elif gesture == my_gesture:
            print('This is a tie')
        else:
            print('I am the winner')

try:
    game()

except SystemExit:
    print('It was nice playing with you. Have a Nice Day')
    
