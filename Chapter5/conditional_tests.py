print("===========True Results===============")
print(f"18 is divisible by 3 with no remainder {18%3 == 0}")
word = "lasagna"
print(f"Lasagna has seven letters {len(word) == 7}")
word = "wizard"
print(f"The word 'wizard' starts with a 'w' {word[0] == 'w'}")
fivesum = sum(list(range(1,6)))
print(f"The average of the first five nonzero integers is 3 {fivesum // 5 == 3}")
newword = "GUITAR"
print(f"guitar is the lowercase version of GUITAR {'guitar'== newword.lower()}")
print(f"6 is divisble by both 3 and 2 {((6 % 3) and (6 % 2)) == 0}")
listy = list(range(13,19))
## print(listy)
print(f"15 or 20 in number list {(15 or 20) in listy}")
print(f"16 and 17 in number list {(16 and 17) in listy}")
print(f"30 is not in number list {30 not in listy}")

print("===========False Results===============")
print(f"5 > 50 {5 > 50}")
print(f"sLeDdInG is the same as SlEdDiNg {'sLeDdInG' == 'SlEdDiNg'}")
print(f"5 times 5 does not equal 25 {5*5 != 25}")
print(f"1 + 2 >= 4 {1+2 >= 4}")
print(f"87 <= 13 {87 <= 13}")
print(f"68 or 57 in number list {(68 or 57) in listy}")
print(f"15 and 21 in number list {(15 and 21) in listy}")
print(f"13 is not in the number list {13 not in listy}")
anotherword = "Westward"
prettysimilarword = "westwarD"
print(f"Westward has fewer than five letters {len(anotherword) < 5}")
print(f"Westward and westwarD remain different even when they're lowercase {anotherword.lower() != prettysimilarword.lower()}")