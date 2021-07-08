def near(w1, w2):
    longword = w2
    shortword = w1
    if len(w1) > len(w2):   #finds the longer word
        longword = w1
        shortword = w2


    # for letter in longword:
    #     control = longword.replace(f"{letter}","", 1)
    #     # print(f"{control}")
    #     # return control

    #     if control == shortword:
    #         return "Its there"
            
    #     else:
    #         return "Its not there sorry"


    for letter in longword:
        control = longword.replace(f"{letter}","", 1)
        #print(f"{control}")


        if control == shortword:
            return "Its there" 



word1 = input("Give me 2 words and I'll see if one is in the other/nFirst word -> ")

word2 = input("Second word -> ")




if word2 != 0:                     #testing
    result = near(word1, word2)    #testing

print(result)                      #testing

#findout which word is longer then take the longiest one and remove each letter 1 and a time until it
#matches the other word or all letters are used.

