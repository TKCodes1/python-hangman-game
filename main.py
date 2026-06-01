import random

words = ("chicken","water","love","monkey","tickle","monsters")

hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}

#print the ASCII hangman

def draw_man(missed_guesses):
    for man in hangman_art[missed_guesses]:
        print(man)

def display_hints(hints):
    print(" ".join(hints))

def display_answer(answer):
    print(f"The correct answer was {answer}")

def main():
    answer = random.choice(words)
    hints = ["_"] * len(answer)
    missed_guesses = 0
    guessed_letters = set()
    is_running = True

# Loop continues until player wins or loses.

    while is_running:
        draw_man(missed_guesses)
        display_hints(hints)
        guess = input("Put in your letter to guess: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed {guess}. Please enter a different letter!")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hints[i] = guess
        else:
            missed_guesses += 1

        if missed_guesses > 5:
            draw_man(missed_guesses)
            print("You lost!")
            display_answer(answer)
            is_running = False
            print("Thank you for playing.")

        if "_" not in hints:
            display_hints(hints)
            print(f"Hooray! {answer} was the right answer!" + "\n" + f"You had {missed_guesses} incorrect answers." + "\n" + "Thank you for playing!")
            is_running = False

if __name__ == '__main__':
    main()