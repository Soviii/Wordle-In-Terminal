#Author: Sovial Sonzeu

import curses
from curses import A_BLINK, A_BOLD, wrapper
import random
import time

validInputs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "\n", "KEY_BACKSPACE", "\b", "\x7f"]

wordBank = []
fiveCharWords = []
timeVar = 0.6

"""Erases extra info from each line"""
def cleanWord(word):
    spacesDeleted = 0
    indexAndCounter = 0 
    length = len(word)
    while spacesDeleted < 5:
        if word[indexAndCounter] == " ":
            word = word[indexAndCounter+1:]
            indexAndCounter = 0
            spacesDeleted += 1
        else:
            indexAndCounter += 1
    
    if word[-1] == '\n':
        word = word[:-1]

    return word

"""Better way of reading a file (automatically closes it)"""
with open ('file.txt') as f:
    for line in f:
        wordBank.append(line.lower()[:-1]) #[:-1] deletes last char which is \n


with open ('dictionary.txt') as f:
    for line in f:
        newWord = cleanWord(line)
        fiveCharWords.append(newWord.lower()) #goes to the last character


"""Chooses random word from word bank"""
def chooseWord(wordList) ->str:
    selection = random.choice(wordList)
    return selection

"""If returns True, marks it green"""
def rightCharAndIndex(correctWord, inputWord, x) ->bool:
    if inputWord[x] == correctWord[x]:
        return True
    else:
        return False


"""If returns True, marks it yellow"""
def rightCharOnly(correctWord, inputWord, x) ->bool:
    if inputWord[x] in correctWord:
        return True
    else:
        return False


"""Checks wordBank for validating input"""
def validWord(word1):
    if word1.lower() in wordBank:
        return True
    else:
        return False


def main(stdscr):

    def displayInstructions():
        rulesWin = curses.newwin(20,50, 0, 0)
        rulesWin.clear()
        rulesWin.addstr("\t Instructions and Rules\n", curses.A_BOLD)
        rulesWin.addstr("You have 6 attempts to guess the right word.\n\nEach attempt must be a valid 5-letter word.\n\n")
        rulesWin.addstr("Accuracy of the letters will be displayed by such:\n")
        rulesWin.addstr("- White means it's not present in the word\n")
        rulesWin.addstr("- Yellow means it's present but in the wrong spot\n")
        rulesWin.addstr("- Green means it's correct\n\nEX: ")
        rulesWin.addstr("correct word is: ")
        rulesWin.addstr("helps\n", A_BOLD)
        rulesWin.addstr("you entered: ")
        rulesWin.addstr("p ", yellowChar)
        rulesWin.addstr("a ", blackChar)
        rulesWin.addstr("l ", greenChar)
        rulesWin.addstr("m ", blackChar)
        rulesWin.addstr("s ", greenChar)
        rulesWin.addstr("\n\n\tPress enter to start the game", A_BLINK)
        rulesWin.refresh()
        while True:
            startKey = rulesWin.getkey()
            if startKey in ("\n", curses.KEY_ENTER):
                rulesWin.clear()
                rulesWin.refresh()
                break
            else:
                continue


    def checkWord(compWord, chosenWord, win):
        letterCheck = 0

        for i in range(5):
            if rightCharAndIndex(chosenWord, compWord, i):
                letterCheck += 1
                win.addstr(f"{compWord[i]} ", greenChar)
                win.refresh()
                time.sleep(timeVar)

            elif rightCharOnly(chosenWord, compWord, i):
                win.addstr(f"{compWord[i]} ", yellowChar)
                win.refresh()
                time.sleep(timeVar)

            else:
                win.addstr(f"{compWord[i]} ", blackChar)
                win.refresh()
                time.sleep(timeVar)

        if letterCheck == 5:
            return True 
        else:
            return False


    def currWindow(win, indX) ->str:
        status = curses.newwin(1 , 50, 3 + (2*indX), 15)
        status.clear()

        word = ""

        letterCount = 0
        while True:
            key = win.getkey()
            if key not in validInputs:
                continue
            if key in ("KEY_BACKSPACE", "\b", "\x7f"):
                if letterCount > 0:
                    word = word[:-2]
                    win.clear()
                    win.addstr(f"{word}", blackChar)
                    win.refresh()
                    letterCount-= 1
                else:
                    continue
            
            elif key in ("\n", curses.KEY_ENTER):
                if letterCount == 5:
                    wordCopy = word.replace(" ", "")
                    if validWord(wordCopy):
                        status.clear()
                        status.addstr("valid word; checking now")
                        status.refresh()
                        time.sleep(timeVar)
                        status.clear()
                        status.refresh()
                        return wordCopy
                    
                    else:
                        status.clear()
                        status.addstr(f"invalid word - {wordCopy}")
                        status.refresh()
                        
                else:
                    status.clear()
                    status.addstr(f"not enough letters")
                    status.refresh()

            elif letterCount < 5:
                if key in validInputs:
                    word += f"{key} "
                    win.clear()
                    win.addstr(f"{word}", blackChar)
                    win.refresh()
                    letterCount += 1


    def userWon(win) ->bool:
        win7.addstr("Good job!")
        win7.refresh()
        win7.getch()
        return True


    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_GREEN)
    blackChar = curses.color_pair(1)
    yellowChar = curses.color_pair(2)
    greenChar = curses.color_pair(3)

    wordleWin = curses.newwin(1, 30, 1, 1)
    win1 = curses.newwin(1, 12, 3, 1)
    win2 = curses.newwin(1, 12, 5, 1)
    win3 = curses.newwin(1, 12, 7, 1)
    win4 = curses.newwin(1, 12, 9, 1)
    win5 = curses.newwin(1, 12, 11, 1)
    win6 = curses.newwin(1, 12, 13, 1)
    win7 = curses.newwin(1, 20, 15, 1)
    
#                      Main Driver
#--------------------------------------------------------#
    chosenWord = chooseWord(fiveCharWords)
    winner = False

    displayInstructions()

    wordleWin.addstr(f"\tWordle in Terminal!", A_BOLD)
    wordleWin.refresh()
    
    
    """Main for loop for running program"""
    for i in range(6):
        compWord = ""
    
        if i == 0:
            compWord = currWindow(win1, i)
            win1.clear()
            if checkWord(compWord, chosenWord, win1):
                winner = userWon(win7)
                break

        elif i == 1:
            compWord = currWindow(win2, i)
            win2.clear()
            if checkWord(compWord, chosenWord, win2):
                winner = userWon(win7)
                break

        elif i == 2:
            compWord = currWindow(win3, i)
            win3.clear()
            if checkWord(compWord, chosenWord, win3):
                winner = userWon(win7)
                break

        elif i == 3: 
            compWord = currWindow(win4, i)
            win4.clear()
            if checkWord(compWord, chosenWord, win4):
                winner = userWon(win7)
                break

        elif i == 4:
            compWord = currWindow(win5, i)
            win5.clear()
            if checkWord(compWord, chosenWord, win5):
                winner = userWon(win7)
                break

        elif i == 5:
            compWord = currWindow(win6, i)
            win6.clear()
            if checkWord(compWord, chosenWord, win6):
                winner = userWon(win7)
                break


    if not winner:
        win7.addstr(f"Wordle was {chosenWord}")
        win7.refresh()
        win7.getch()

wrapper(main)
