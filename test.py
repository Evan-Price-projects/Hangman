import csv
import random
#got scrabbles words from http://www.poslarchive.com/math/scrabble/lists/common-6.html

def guess(guesses):
    if guesses == 6:
        print("\nO\n")
    if guesses == 5:
        print("\nO-\n")
    if guesses == 4:
        print("\nO-/\n")
    if guesses == 3:
        print("\nO->\n")
    if guesses == 2:
        print("\nO->-\n")
    if guesses == 1:
        print("\nO->-/\n")

def scores(words, score):
    for i in range(0,len(words)):
        print(words)
        print(len(words))
        helper0 =['h','u','n','a','i','l','o','t']
        helper1 =['e','s']                
        helper2 =['d','z']
        helper3 =['k']
        helper4 =['g','y']
        helper5 =['w']                
        helper6 =['b']
        helper7 =['c','j','m']
        if words in helper0:
            score = score + 1
            return score
        if words in helper1:
            score = score + 2
            return score
        if words in helper2:
            score = score + 3
            return score
        if words in helper3:
            score = score + 4
            return score
        if words in helper4:
            score = score + 5
            return score
        if words in helper5:
            score = score + 7
            return score
        if words in helper6:
            score = score + 8
            return score
        if words in helper7:
            score = score +10
            return score

wordamount = -1
scoreboard = 0
while wordamount != 0:
    wordamount = random.randint(2,8)
    if wordamount == 0:
        break
    guesses = 6
    csv_reader = csv.reader(open('words.csv', mode='r'))
    line_count = 0
    colm_count = 0
    va = 0
    changer = []
    solution = ""
    #cnt = 0
    for row in csv_reader:
        line_count += 1
        if len(list(row[1])) == wordamount:
            changer.append(line_count)

    x = random.randint(min(changer), max(changer))

    csv_reader = csv.reader(open('words.csv', mode='r'))
    top = 0
    i = 0
    for col in csv_reader:
        colm_count += 1
        if colm_count == x:
            if row[i] != " ":
                top += 1
            d = random.randint(0, (top-1))
            solution = col[d]
            print(col[d])

    guess(guesses)
    bord = ""
    for i in range(0,wordamount):
            bord += "_"
            print("_ ", end = '')
    blist = list(bord)
    board = str(input("\nGuess a letter:\nYou have " + str(guesses) + " incorrect guesses left\n"))
    while guesses > 0:
        if len(board) == 1:
            if board in solution:
                scoreboard = scores(board, scoreboard)
                print("\nScore: " + str(scoreboard))
                solspt = list(solution)
                for va in range(0, len(solspt)):
                    if board == solspt[va]:
                        blist[va] = board
                guess(guesses)
                for i in range(0, len(blist)):
                    print(blist[i], end = ' ')
                if "_" not in blist:
                    print("success")
                    break
                print("\nScore: " + str(scoreboard))
                board = str(input("\nGuess a letter:\nYou have " + str(guesses) + " incorrect guesses left\n"))
            else:
                guesses -= 1
                guess(guesses)
                for i in range(0, len(blist)):
                    print(blist[i], end = ' ')
                if guesses == 0:
                    break
                else:
                    print("\nScore: " + str(scoreboard))
                    board = str(input("\nIncorrect!\nYou have " + str(guesses) + " incorrect guesses left\n"))
        else:
            guesses -= 1
            for i in range(0, len(blist)):
                print(blist[i], end = ' ')
            print("\nScore: " + str(scoreboard))
            board = str(input("\nIncorrect!\nYou have " + str(guesses) + " incorrect guesses left\n"))

    if guesses == 0:
        print("\nO->-< \nFAILURE, the word was " + solution)
        print("\nScore: " + str(scoreboard))

