# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 19:57:41 2020

@author: DELL
"""

'''Hangman game in python'''
import random
from collections import Counter
someWords="apple mango banana jackfruit lemon orange pineapple melons papaya cherry peach litchi grapes berries tomato watermelon cheeku"
someWords= someWords.split(' ')
#randomly choosing fruits 
word= random.choice(someWords)
if __name__=='__main__':
    print('Guess the word!HINT:Its a fruit name')
    for i in word:
        print('_', end= ' ')
    print()
    playing=True
    letterGuessed= ''  #list for storing letters choosed by player
    chances= len(word)+2
    correct=0
    flag=0
    try:
        while(chances!=0) and flag==0:  #flag updated when choice is correct
            print()
            chances-=1
            try:
                guess=str(input('Enter letter to guess: '))
            except:
                print('Enter only a single letter')
                continue
            if not guess.isalpha():    #validation of guess
                print('Enter only letter')
                continue
            elif len(guess)>1:
                print('Enter only single letter')
                continue
            elif guess in letterGuessed:
                print('you have already guessed this letter')
                continue
            if guess in word:      #if letter guessed correctly
                k=word.count(guess)  #stores no. of times guessed letter occurs
                for _ in range(k):
                    letterGuessed += guess #letter guessed is added as many times it occurs
            #print the word
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed)!= Counter(word)):
                    print(char, end=' ')
                    correct +=1
                #if user guessed all letters correct
                elif(Counter(letterGuessed)== Counter(word)):
                    print("the word is: ", end=' ')
                    print(word) 
                    flag=1
                    print('right guess,YOU WON!')
                    break  #break outer for loop
                    break   #break while loops 
                else:
                    print('_', end= ' ')
            #if user has used all his chances
        if chances <=0 and (Counter(letterGuessed)!= Counter(word)):
            print()
            print('YOU LOST!TRY AGAIN....')
            print('The word was {}'.format(word))
    except KeyboardInterrupt:
        print()
        print('BYE!')
        exit()
        