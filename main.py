from random import randint

def get_result(you , comp):
    #rr,pp,ss
    #condition for draw
    if you == comp:
        return 0
    
    #condition for win

    
    if you == 'r' and comp == 's':
        return 1
    elif you == 's' and comp == 'r':
        return -1

    elif you == 'r' and comp == 'p':
        return -1
    elif you == 'p' and comp == 'r':
        return 1 
    elif you == 'p' and  comp == 's':
        return -1
    elif you == 's' and comp == 'p':
        return 1
        
    
if __name__ == '__main__':
    val = randint(1,3)     
    if val == 1:
        comp = 'r'
    elif val == 2:
        comp = 'p'
    else:
        comp = 's'
    print("Enter 'r' for Rock, 'p' for Paper ans 's' for Scissor : " )
    you = input()
    print(f'You chose {you} and computer chose {comp} ')
    result = get_result(you , comp)
    if result == 1:
        print('You Win !')
    elif result == -1:
        print('You Lose!')
    else:
        print('Draw')
