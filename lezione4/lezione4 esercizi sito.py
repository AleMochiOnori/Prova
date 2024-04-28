# 8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the function, and make sure the message displays correctly.

print()
def display_message() -> str :
    print("i'm learning python")



display_message()



print()

# 8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as "One of my favorite books is Alice in Wonderland". Call the function, making sure to include a book title as an argument in the function call.



def favorite_book(title: str) -> str :
    print(title,"One of my favorite books is Alice in Wonderland")
favorite_book(title = "Alice in wonderland ---")


# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.


def make_shirt(a: str , b: str) -> str :
        return a , b
print()
    
        
print(make_shirt("Size L","JUST DO IT"))
print(make_shirt(a =  "Size L", b = "JUST DO IT"))

print()
# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.



def make_shirt(size = 'Large', message = 'I love Python'):
    
    print(f"Size: {size}  Message: {message}")
  

make_shirt()

make_shirt(size = "Medium", message = "Python is for beginners" )


make_shirt(size = "Small" , message = "Python is lovely")
print()



# 8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.


def describe_city(city = "Reykjavik" , country = "Iceland") : 
    print(f"{city} is in {country}")

describe_city()
describe_city(city = "Rome" , country = "Italy")
describe_city(city = "New York" , country = "New York")
describe_city(city = "Berlin" , country = "Germany")
print()




# 8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this: "Santiago, Chile". Call your function with at least three city-country pairs, and print the values that are returned.




def city_country(a : str , b: str) -> str :
    return a + b


print(city_country("Rome,", "Italy"))
print(city_country("Moscow,", "Russia"))
print(city_country("London,", "United Kingdom"))
print()



# 8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the  dictionaries are storing the album information correctly. Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs, add that value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album.


def make_album(artist , album, songsNumber = None ) -> dict:
    album = {"Artist ": artist, "Album" : album}
    if songsNumber:
        album['songs'] = songsNumber
    return album

print(make_album("Linkin Park" , "Meteora" , songsNumber= "13"))
print(make_album("If i were you", "InnerSignals"))
print(make_album("If i were you", "The Sleepless"))
print()


# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.