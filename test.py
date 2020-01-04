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

wordamount = -1

while wordamount != 0:
    wordamount = int(input("how many letters? (between 2-8), 0 exits: "))
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
    #guess(guesses)
    while guesses > 0:
        if len(board) == 1:
            if board in solution:
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
                board = str(input("\nGuess a letter:\nYou have " + str(guesses) + " incorrect guesses left\n"))
            else:
                guesses -= 1
                guess(guesses)
                for i in range(0, len(blist)):
                    print(blist[i], end = ' ')
                if guesses == 0:
                    break
                else:
                    board = str(input("\nIncorrect!\nYou have " + str(guesses) + " incorrect guesses left\n"))
        else:
            guesses -= 1
            for i in range(0, len(blist)):
                print(blist[i], end = ' ')
            board = str(input("\nIncorrect!\nYou have " + str(guesses) + " incorrect guesses left\n"))

    if guesses == 0:
        print("\nO->-< \nFAILURE, the word was " + solution)
