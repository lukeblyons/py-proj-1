### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.
# Code here

# title = input("Enter the title of the book: ")
# author = input("Enter the author of the book: ")
# year = int(input("Enter the year the book was published: "))
# rating = float(input("Enter the rating of the book: "))
# pages = int(input("Enter the number of pages in the book: "))



### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.
# Code here


# title = input("Enter the title of the book: ")
# author = input("Enter the author of the book: ")
# year = int(input("Enter the year the book was published: "))
# rating = float(input("Enter the rating of the book: "))
# pages = int(input("Enter the number of pages in the book: "))



### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.
# Code here


# def input_book_info():
#     title = input("\nWhat is the title of the book you would like to add? - ")
#     author = input("Who is the author of the book you would like to add? - ")

#     while True:
#         try:
#             year = int(input("What year was this book published? - "))
#             break
#         except ValueError:
#             print("Invalid input. Please type a number.")

#     while True:
#         try:
#             rating = float(input("What rating out of 5 would you give this book? - "))
#             break
#         except ValueError:
#             print("Invalid input. Please type a number.")
        
#     while True:
#         try:
#             pages = int(input("What is the page count of the book? - "))
#             break
#         except ValueError:
#             print("Invalid input. Please type a number.")
    
#     return {"title": title, "author": author, "year": year, "rating": rating, "pages": pages}




### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.
# Code here

# def main_menu(books_source):
#     active = True

#     while active:
#         choice = input("\nChoose 1 to add a book. Choose 2 to see all your books. Choose 3 to exit. - ")

#         if choice == "1":
#             books_source.append(input_book_info())
#         elif choice == "2":
#             print_all_books(books_source)
#         elif choice == "3":
#             print("\nGoodbye")
#             active = False
#         else:
#             print("\nSorry please type a number for one of the options.\n")

# # Call main_menu with your book data to start the program
# main_menu(books_source)



### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

# Here are your existing books in the library
my_book_list = [
    {
        "title": "Harry Potter and the Philosopher's Stone",
        "author": "J.K. Rowling",
        "year": 1997,
        "rating": 4.47,
        "pages": 309
    },
    {
        "title": "Harry Potter and the Chamber of Secrets",
        "author": "J.K. Rowling",
        "year": 1998,
        "rating": 4.41,
        "pages": 341
    },
    {
        "title": "Harry Potter and the Prisoner of Azkaban",
        "author": "J.K. Rowling",
        "year": 1999,
        "rating": 4.55,
        "pages": 435
    }
]

# Your book data fetching functions
def get_book_title(book_dictionary):
    return book_dictionary["title"]

def get_book_author(book_dictionary):
    return book_dictionary["author"]

def get_book_year(book_dictionary):
    return book_dictionary["year"]

def get_book_rating(book_dictionary):
    return book_dictionary["rating"]

def get_book_pages(book_dictionary):
    return book_dictionary["pages"]

def create_new_book():
    title = input("\nWhat is the title of the book you would like to add? - ")
    author = input("Who is the author of the book you would like to add? - ")
    try:
        year = int(input("What year was this book published? - "))
    except ValueError:
        year = int(input("Please type a number? - "))
    try:
        rating = float(input("What rating out of 5 would you give this book? - "))
    except ValueError:
        rating = float(input("Please type a number? - "))
    try:
        pages = int(input("What is the page count of the book? - "))
    except ValueError:
        pages = int(input("Please type a number? - "))

    return {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

def print_all_books(list_of_books):
    for book in list_of_books:
        title = get_book_title(book)
        author = get_book_author(book)
        year = get_book_year(book)
        rating = get_book_rating(book)
        pages = get_book_pages(book)

        print(f"Title: {title}, Author: {author}, Year: {year}, Rating: {rating}, Pages: {pages}")

def main_menu(books_source):
    active = True

    while active:
        choice = input("\nChoose 1 to add a book...\nChoose 2 to see all your books...\nChoose 3 to see a count of your books...\nChoose 4 to see a count of the pages of your books...\nChoose 5 to exit.\nType here: ")

        if choice == "1":
            books_source.append(create_new_book())
        elif choice == "2":
            print_all_books(books_source)
        elif choice == "3":
            print(f"\nYou have a total of {len(books_source)} books.\n")
        elif choice == "4":
            print(f"\nYou books page count totals {sum([get_book_pages(x) for x in books_source])} pages!\n")
        elif choice == "5":
            print("\nGoodbye")
            active = False
        else:
            print("\nSorry please type a number for one of the options.\n")

main_menu(my_book_list)
