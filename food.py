#Create a list
#Prompt the user to enter five foods, and store the responses in the list
#Display the list on one line, each item seperated by commas
#Calculate how many characters were entered and display this to the user
#Hint: Using the len() function will be useful here
#Below is a sample of what your output might look like. You do not have to follow the text exactly.
#
#Enter a food: pizza
#Enter a food: beef jerkey
#Enter a food: rice triangles
#Enter a food: steamed chinese bun
#Enter a food: fried chicken
#
#Your entered foods are:
#pizza, beef jerkey, rice triangles, steamed chinese bun, fried chicken 
#You entered a total of 62 characters




list = [input("Enter a food: "),input("Enter a food: "),input("Enter a food: "),input("Enter a food: "),input("Enter a food: ")]

cherecters = 0
for x in list: 
    cherecters += len(x)

print(f"Tour entered foods are: {list[0]}, {list[1]}, {list[2]}, {list[3]}, {list[4]}")
print(f"you entered a total of {(cherecters)} cherecters")