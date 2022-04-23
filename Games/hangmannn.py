
import masach_ptiha        as mp
import auxilarry_functions as aux


def main():
    mp.print_name_of_game()
    magic_word = aux.choose_word("./words_to_guess.txt",42).casefold()

    # TODO: Delete this print!
    print(magic_word)

    aux.print_num_of_lines(magic_word)
    MAX_TRIES = 6
    print("\n",MAX_TRIES)
    num_failures = 1
    old_letters_guessed = []

    while num_failures <= MAX_TRIES+1:
        
        letter_guessed = input("\nenter a letter ").casefold()
        is_valid = aux.try_update_letter_guessed(letter_guessed,old_letters_guessed)
        # אם הניחוש לא תקין, נתעלם ממנו
        if is_valid == False:
            continue
        elif is_valid == True:
            # Check if letter guessed is a new letter in magic word
            if letter_guessed in magic_word:
                current_word_state = aux.show_hidden_word(magic_word, old_letters_guessed)
                print(current_word_state)
                win = aux.check_win(magic_word,old_letters_guessed)
                if win==True:
                    print("WIN")
                    break
            else:
                aux.print_hangman(num_failures)
                num_failures += 1
    if num_failures > MAX_TRIES:
        print("LOSE")

if __name__ == "__main__":
    main()

#צריך לבדוק אם כל הפונקציות באותו השם שנאמר בהוראות
# לעבור על כל ההוראות הסופיות