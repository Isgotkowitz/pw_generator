
def noSimiListFn(func, val):
    words = []
    words.append(val[0])
    for i in range(1, len(val)):
        found_sim = False
        for j in range(0, len(words)):
            if func(words[j], val[i]) <= 2:
                found_sim = True
                break
        if not found_sim:
            words.append(val[i])

    return words
