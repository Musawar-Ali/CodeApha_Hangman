#!/usr/bin/env python3
"""
hangman.py
Simple text-based Hangman game.

Usage:
    python hangman.py        # interactive play
    python hangman.py --seed 42   # deterministic for demo
Author: Musawar Ali 
"""

import random
import argparse

HANGMAN_STAGES = [
    # 6 wrong allowed: stages 0..6 (0 = no mistakes)
    """
     +---+
     |   |
         |
         |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    ======""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =======""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =======""",
]

WORD_LIST = [
    "python", "hangman", "android", "github", "variable", "function", "keyboard"
]

MAX_WRONG = 6

def choose_word(seed=None):
    if seed is not None:
        random.seed(seed)
    return random.choice(WORD_LIST).lower()

def display_progress(secret, guessed_letters):
    shown = " ".join([ch if ch in guessed_letters else "_" for ch in secret])
    return shown

def play(seed=None):
    secret = choose_word(seed)
    guessed_letters = set()
    wrong_guesses = 0
    tried_letters = set()

    print("Welcome to Hangman — guess the word one letter at a time!")
    while wrong_guesses < MAX_WRONG:
        print(HANGMAN_STAGES[wrong_guesses])
        print("\nWord: ", display_progress(secret, guessed_letters))
        print(f"Wrong guesses left: {MAX_WRONG - wrong_guesses}")
        print("Tried letters:", " ".join(sorted(tried_letters)) or "(none)")

        choice = input("Enter a letter (or type 'guess' to guess the full word): ").strip().lower()
        if not choice:
            print("Please enter something.")
            continue

        if choice == "guess":
            attempt = input("Your full-word guess: ").strip().lower()
            if attempt == secret:
                print("\n🎉 Correct — you guessed the word!")
                print(f"The word was: {secret}")
                return True
            else:
                wrong_guesses += 1
                print("Nope — wrong guess for the full word.")
                continue

        if len(choice) != 1 or not choice.isalpha():
            print("Enter a single alphabetic character.")
            continue

        if choice in tried_letters:
            print("You already tried that letter.")
            continue

        tried_letters.add(choice)

        if choice in secret:
            guessed_letters.add(choice)
            print("Nice — that letter is in the word!")
            # Win condition
            if all(ch in guessed_letters for ch in secret):
                print("\n🎉 Congratulations! You completed the word:")
                print(" " + " ".join(secret))
                return True
        else:
            wrong_guesses += 1
            print("Sorry — that letter is not in the word.")

    # Loss
    print(HANGMAN_STAGES[wrong_guesses])
    print("\nGame over — you've used all attempts.")
    print(f"The word was: {secret}")
    return False

# Call play() and assign the result to a variable to prevent it from being printed
game_result = play()
