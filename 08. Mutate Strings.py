old_word = input()
new_word = input()
final_word = ""
prev_word = ""
c = 1

for i in range(len(old_word)):
    final_word += new_word[:c] + old_word[c:]
    c += 1
    if final_word != old_word and final_word != prev_word:
        print(final_word)
        prev_word = final_word
        final_word = ""
    else:
        final_word = ""
        continue