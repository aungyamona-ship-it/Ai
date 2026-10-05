name = input("What's your name? : ")
print("What type of movie do you want to watch: action, horror, or comedy? : ")
movie_type = input().lower()

if movie_type == "action":
    print("Hi", name + "!", "I recommend the movie Jason Bourne!")
elif movie_type == "comedy":
    print("Hi", name + "!", "I recommend the movie Home Alone!")
elif movie_type == "horror":
    print("Hi", name + "!", "I recommend the movie Obsession!")
else:
    print("Sorry", name + ", that genre is not available.")