import random
#Create two seperate lists for player one and player two.
player1 = []
player2 = []
#Each one should contain 10 random numbers between 1 and 50.
count = 0
while count < 10:
  player1.insert(1, random.randrange(1,50))
  player2.insert(1, random.randrange(1,50)) 
  count += 1
#Again, your lists should be random numbers
#Do NOT sort the lists.
#Compare the lists in order. Whichever list has the higher number wins.
round = 0
listspot = 0

onewin = 0
twowin = 0

while round < 10:
  if player1[listspot] > player2[listspot]:
    onewin += 1
    round += 1
    listspot += 1
  elif player1[listspot] < player2[listspot]:
    twowin += 1
    round += 1
    listspot += 1
  else:
    round += 1
    listspot += 1

#Keep track of how many times each list wins.
#Find the highest number in each list and it's index. If the number occers multiple times take the first instsance.
onehighest = max(player1)
twohighest = max(player2)
onehighplace = player1.index(onehighest)
twohighplace = player2.index(twohighest)
#Find the lowest number in each list and it's index. If the number occers multiple times take the first instsance.
onelowest = min(player1)
twolowest = min(player2)
onelowplace = player1.index(onelowest)
twolowplace = player2.index(twolowest)
#A tie is not record as a win for either player
#Display the lists
#Report to the user how many times each player won and the information from lines 6 and 7.
#For the example output I am limiting the range to 1 to 9 to keep it more readable.

#Player One = 5,7,2,9,1,1,3,8,6,9
print(f"Player One = {player1}")
#Player Two = 3,8,5,5,8,1,4,7,4,7
print(f"Player Two = {player2}")
#Player one won 5 times
print(f"Player one won {onewin} times.")
#Player two won 4 times
print(f"Player two one {twowin} times.")
#Player one's highest number is 9 at index 3
#Player two's highest number is 8 at index 1
#Player one's lowest number is 1 at index 4
#Player two's lowest number is 1 at index 5
print(f"Player one's highest number is {onehighest} at index {onehighplace}")
print(f"Player two's highers number is {twohighest} at index {twohighplace}")
print(f"Player ine's lowest number is {onelowest} at index {onelowplace}")
print(f"Player two's lowest number is {twolowest} at index {twolowplace}")