import csv
import random
import time
#got scrabbles words from http://www.poslarchive.com/math/scrabble/lists/common-6.html

def scores(words, score, counter):
    print(words)
    print(len(words))
    helper0 =['e','a','i','o','n','r','t','l','s','u']
    helper1 =['d','g']                
    helper2 =['b','c','m','p']
    helper3 =['f','h','v','w','y']
    helper4 =['k']
    helper5 =['j','x']                
    helper6 =['q','z']
    if words in helper0:
        score = score + (1 * counter)
        return score
    if words in helper1:
        score = score + 2 * counter
        return score
    if words in helper2:
        score = score + 3 * counter
        return score
    if words in helper3:
        score = score + 4 * counter
        return score
    if words in helper4:
        score = score + 5 * counter
        return score
    if words in helper5:
        score = score + 8 * counter
        return score
    if words in helper6:
        score = score +10 * counter
        return score

def scoretable(board, solution, blist, scoreboard, timeout_start, len_soln):
    counter = 0
    x=0
    while time.time() < timeout_start:
        print(timeout_start + 1 - time.time())    
        if len(board) == 1:
            counter = 0
            if board in solution:
                solspt = list(solution)
                for va in range(0, len(solspt)):
                    if board == solspt[va]:
                        counter = counter + 1
                        blist[va] = board
                for i in range(0, len(blist)):
                    print(blist[i], end = ' ')
                scoreboard = scores(board, scoreboard, counter)
                print("\nScore: " + str(scoreboard))
                counter = 0
                if "_" not in blist:
                    print("success")
                    timeout_start = timeout_start + len_soln
                    return scoreboard
                board = str(input("\nGuess a letter:\n"))
            else:
                for i in range(0, len(blist)):
                    print(blist[i], end = ' ')
        else:
            for i in range(0, len(blist)):
                print(blist[i], end = ' ')
            print("\nScore: " + str(scoreboard))
            board = str(input("\nIncorrect!\n"))

wordamount = -1
scoreboard = 0
timeout_start = time.time() + 1
while wordamount != 0:
    wordamount = random.randint(2,8)
    len_soln=(5*wordamount)
    while time.time() < timeout_start:# Petr Krampl  https://stackoverflow.com/questions/13293269/how-would-i-stop-a-while-loop-after-n-amount-of-time
        timeout_start = timeout_start + len_soln
        print(timeout_start + 1 - time.time())
        if wordamount == 0:
            break
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
        bord = ""
        for i in range(0,wordamount):
                bord += "_"
                print("_ ", end = '')
        blist = list(bord)
        board = str(input("\nGuess a letter:\n"))
        scoreboard = scoretable(board, solution, blist, scoreboard, timeout_start, len_soln)
    if time.time() >= timeout_start + len_soln:
        print("Game Over: \nFinal Score: " + str(scoreboard))
    

