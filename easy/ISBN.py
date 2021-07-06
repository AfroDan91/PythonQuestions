# ISBN = 123456789012

# ISBM = str(ISBN)

# magicNumber = 0

# for letter in ISBM:
#     if letter == 1 or letter == 3 or letter == 5 or letter == 7 or letter == 9:
#         {letter} * 3 + magicNumber

#     else:
#         letter+magicNumber
    
#     print(magicNumber)
#####################################
code = "978030640615"
odds_should_b = ["9", "8", "3", "6", "0", "1"]
evens_should_b = ["7", "0", "0", "4", "6", "5",]

odds = []
evens = []

odds_total = []

last_number = 0
code_split = " ".join(code).split() # splits the code into a list of strings containing each number 

for number in range(0, len(code_split)): #splits code_split into odds and evens by index 
    if number % 2:
        evens.append(int(code_split[number]))
    else:
        odds.append(code_split[number])


for odd in odds:
    new_odd =(int(odd) * 3)
    odds_total.append(new_odd)

odds_final = sum(odds_total)
evens_final = sum(evens)

num_tot = 10 - (odds_final + evens_final) % 10

#print(code_split)
# print(last_number)
# print(odds)
# print(odds_should_b)
#print (evens)
# print(evens_should_b)
#print(odds_total)
print(num_tot)
