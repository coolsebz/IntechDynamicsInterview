def IntechDynamics(word):
    if word[len(word)-1] is "D" and word[0] is "I":
        return "INTECH DYNAMICS"

    if word[0] is "I":
        return "INTECH"

    if word[len(word)-1] is "D":
        return "DYNAMICS"

if __name__ == '__main__':
    word = raw_input("Insert a word here: ")
    print IntechDynamics(word)