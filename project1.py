from decimal import MAX_EMAX
import random 

NUM_DIGITS = 3
MAX_GUESSES = 10 

def main():
    print('''숫자야구게임

    Pico   : 숫자는 맞지만, 자리가 다른 경우
    Fermi  : 숫자와 자리가 맞는 경우
    Bagels : No digit is correct.

For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico.'''.format(NUM_DIGITS))

    while True: # 메인 게임 루프 
        # 이것은 사용자가 에측해야 할 비밀번호를 저장한다:
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print(' You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1 
        while numGuesses <= MAX_GUESSES:
            guess = ''
            #유효한 예측값을 입력할 떄까지 루프를 계속 돈다.:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('>')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break # 숫자를 맞췄으니 이 루프에서 빠져나간다. 
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))

        # 다시 게임을 하고 싶은지 묻는다. 
        print('Do you want to play again? (yes or no)')
        if not input('>').lower().startswith('y'):
            break
    print('Thanks for playing!')

def getSecretNum():
    """NUM_DIGITS개의 임의 숫자로 구성된 문자열을 반환한다."""
    numbers = list('0123456789') # 0부터 9까지의 숫자 리스트를 생성한다. 
    random.shuffle(numbers) # 무작위 순서가 되도록 섞는다. 

    # 비밀번호를 뽑기 위해 리스트의 처음부터 NUM_DIGITS자리까지의 수를 얻는다.:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum 

def getClues(guess, secretNum):
    """비밀번호에 대한 단서인 pico, fermi, bagels로 구성된 문자열을 반환한다."""
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # 맞는 숫자이며 위치(자리)도 맞다. 
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # 숫자는 맞지만 잘못된 위치(자리)에 있다. 
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagles' # 일치하는 숫자가 전혀 없다. 
    else: 
        # 힌트를 알파벳순으로 정렬하여 
        # 힌트의 순서가 또 다른 힌트가 되지 않도록 한다. 
        clues.sort()
        # 문자열 힌트 리스트를 가지고 단일 문자열을 만든다. 
        return ' '.join(clues)

# 이 프로그램이 다른 프로그램에 임포트(import)된 게 아니라면 게임이 실행된다:
if __name__ == '__main__':
    main()