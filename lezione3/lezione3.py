# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
# • Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
# • Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!

frasi: list = ["mi piace tanto la ", "vorrei avere una ", "vorrei ordinare la "]
pizzas: list = ['margherita', 'diavola' , "rossa con i wusstel/salsiccia"]


for f,i in zip(frasi,pizzas) :
    print(f"{f} Pizza {i}")
print(f"Mi piace molto la pizza margerita ma ogni tanto per cambiare prendo anche la {pizzas[-2]} e la", pizzas[-1])        



# 4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
# • Modify your program to print a statement about each animal, such as A dog would make a great pet.
# • Add a line at the end of your program, stating what these animals have in common. You could print a sentence, such as Any of these animals would make a great pet!

animalLove: list = [" is one of my favourite pets."," is the best friend of the human being and i think that's true because i love them even more than cats."," can be a pet for arguable people that want exotic pets. i don't raccomand though."]
pets :list = ['Cat', 'Dog' , "Shark"]
for a,i in zip(pets,animalLove) :
    print(f"{a}{i}")
print(f"I really like either {pets[0]} and {pets[1]} {pets[2]} non lo è e mi fa paura")    


# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.


for i in range(1,21):
    print(i)



# 4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)




#My_list: list = [*range(1, 1000000,1)]  #Commenting these lines otherwise can't see terminal properly
#print(My_list)





# 4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.


#minimun: int = min(My_list)
#maximum : int = max(My_list)
#sum : int = sum(My_list)
#print(sum)





# 4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.




for a in range(1,21):
    if a % 2 != 0:
        print("Il numero dispari è  ", a)





# 4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.

listanumerimultipli : list  = []
start : int = 3
for a in range(3,30 + 1):
    if a % start == 0:
        listanumerimultipli.append(a)
print("lista multipli di 3" , listanumerimultipli)
# 4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.        


for a in range(1,10 + 1):
    print(a**3)



cubes = [a**3 for a in range(1, 11)]

print(cubes)





# 4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
# • Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
# • Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
# • Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.




for i in range(1,21)[0:3:1]:
    print("The first three items in the list are:", i)


for i in range(1,21)[8:11:1]:
    print("Three items from the middle of the list are:", i)

for i in range(1,21)[17:21:1]:
    print("The last three items in the list are:", i)


# Definizione della variabile car
car = 'subaru'

# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement
# describing each test and your prediction for the results of each test. Your code
# should look something like this:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# • Look closely at your results, and make sure you understand why each line
# evaluates to True or False.
#  •  Create at least 10 tests. Have at least 5 tests evaluate to True and another
# 5 tests evaluate to False.




# Test condizionali
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("Is car.lower() == 'subaru'? I predict True.")
print(car.lower() == 'subaru')

print("\nIs car.upper() == 'SUBARU'? I predict True.")
print(car.upper() == 'SUBARU')

print("\nIs car != 'ford'? I predict True.")
print(car != 'ford')

print("Is car.startswith('s')? I predict True.")
print(car.startswith('s'))

print("Is car.endswith('ru')? I predict True.")
print(car.endswith('ru'))

print("Is len(car) == 6? I predict True.")
print(len(car) == 6)

print("Is 'sub' in car? I predict True.")
print('sub' in car)

print("Is 'audi' not in car? I predict True.")
print('audi' not in car)



# 5-2. More Conditional Tests: You don’t have to limit the number of tests you cre-
# ate to 10. If you want to try more comparisons, write more tests and add them

# to conditional_tests.py. Have at least one True and one False result for each of
# the following:
# • Tests for equality and inequality with strings
# • Tests using the lower() method
# • Numerical tests involving equality and inequality, greater than and less
# than, greater than or equal to, and less than or equal to
# • Tests using the and keyword and the or keyword
# • Test whether an item is in a list
# • Test whether an item is not in a list


Variabile : str = "Python"

lista : list = [1,2,4,5]


print( Variabile == "Python")

print(Variabile != "Python")

print(Variabile.lower() == "Python")


print( 5 >= 4)

print( 4 == 4)

print(3 < 2)

print( 3 > 2)

print(3==3 and 3 > 2)

print (len(Variabile) <= 6)

print(3 >= 3 or 4 < 6)

print(1 in lista)

print(6 not in lista)


# 5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
# • Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
# • Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.


alien_color : str = "green"
if alien_color == "green":
    print("Player earned 5 points")


if alien_color == "yellow":
    print("player earned 5 points ")    




# 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
# • If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
# • If the alien’s color isn’t green, print a statement that the player just earned 10 points.
# • Write one version of this program that runs the if block and another that runs the else block.


if alien_color == "yellow":
    print("player just earned 5 points for shooting the alien")
else:
    print("the player just earned 10 points.")



# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.

# • If the alien is green, print a message that the player earned 5 points.
# • If the alien is yellow, print a message that the player earned 10 points.
# • If the alien is red, print a message that the player earned 15 points.
# • Write three versions of this program, making sure each message is printed for the appropriate color alien.    




if alien_color == "green":
    print("player just earned 5 points for shooting the alien")
elif alien_color == "yellow" :
       print("the player just earned 10 points.")
else:
    print("the player just earned 15 points.")





if alien_color == "yellow":
    print("player just earned 5 points for shooting the alien")
elif alien_color == "greem" :
       print("the player just earned 10 points.")
else:
    print("the player just earned 15 points.")





if alien_color == "black":
    print("player just earned 5 points for shooting the alien")
elif alien_color == "yellow" :
       print("the player just earned 10 points.")
else:
    print("the player just earned 15 points.")



# 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
# • If the person is less than 2 years old, print a message that the person is a baby.
# • If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
# • If the person is at least 4 years old but less than 13, print a message that the person is a kid.
# • If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
# • If the person is at least 20 years old but less than 65, print a message that the person is an adult.
# • If the person is age 65 or older, print a message that the person is an elder.


person : int = 30 

if person < 2 :
    print("the person is a baby")
elif person >= 2 and person <= 4 :
    print("the person is a toddler")
elif person >= 4 and person <= 13 :
    print("the person is a kid")
elif  person >= 13 and person <= 20 :
    print("the person is a teeneager")
elif person >= 65 :
    print("the person is an elder")    



# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
# • Make a list of your three favorite fruits and call it favorite_fruits.
# • Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as You really like Apples!    


favouirete_fruits :list = ["banana","apple","cocco","watermelon"]

if "banana" in favouirete_fruits :
    print("i like banana")
if "apple" not in favouirete_fruits :
    print("i like banana")
if "watermelon" in favouirete_fruits :
    print("i really like watermelon")
if "cocco" in favouirete_fruits :
    print("i like cocco")
if "apple" in favouirete_fruits :
    print("i like apple")
        


# 5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user.
# • If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
# • Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.        
        
        
user_names: list = ["admin","user123","johndoe","sarahsmith","techguru45"]


user_names = ["admin", "user123", "johndoe", "sarahsmith", "techguru45"]



admin_printed = False  # Variabile per capire se "admin" è stato stampato



for x in user_names:
    if x == "admin": # controllo se admin è presente nella lista 
        if not admin_printed:  # Controlla se "admin" non è ancora stato stampato
            print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " , x , ", thank you for logging in again.")
