#פונקציה שמקבלת מחרוזת ומזהה את המילה הארוכה ביותר
def lon_word(text):
    num_of_words = text.split()
    print(num_of_words)
    last_length = 1
    for i in num_of_words:
        new_length = len (i)
        if new_length>last_length:
            last_length = new_length
            longest_word = i
    return longest_word
    #print(longest_word)

print(lon_word("today is friday"))