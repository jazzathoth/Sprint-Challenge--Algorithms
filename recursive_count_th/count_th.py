'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    count = 0

    def is_th(word_r, letters, pos):
        nonlocal count
        if pos > len(word_r):
            return

        elif letters == "th":
            count += 1
            is_th(word_r, word_r[pos:pos + 1], pos + 1)
        else:
            is_th(word_r, word_r[pos-1:pos + 1], pos + 1)

    is_th(word, word[0:2], 1)


    return count