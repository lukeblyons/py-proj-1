my_book = {
    "title": "Harry Potter and the Philosopher's Stone",
    "author": "J.K. Rowling",
    "year": 1997,
    "rating": 4.47,
    "pages": 309
}

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

def book_parser(book_dictionary):
    book_string = f"This books name is {book_dictionary['title']}, and was written by {book_dictionary['author']}. It was published in the year {book_dictionary['year']} and currently holds a rating of {book_dictionary['rating']}. The length of the book is {book_dictionary['pages']} pages."
    return book_string

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

def book_parser_from_list(book_dictionary_list):
    for book_dictionary in book_dictionary_list:
        print(book_parser(book_dictionary))

def get_set_of_authors(book_dictionary_list):
    author_set = set()
    for book_dictionary in book_dictionary_list:
        author_set.add(book_dictionary["author"])
    return author_set

def get_total_pages(book_dictionary_list):
    total_pages = 0
    for book_dictionary in book_dictionary_list:
        total_pages += book_dictionary["pages"]
    return total_pages

print(book_parser(my_book))
print(get_book_title(my_book))
print(get_book_author(my_book))
print(get_book_year(my_book))
print(get_book_rating(my_book))
print(get_book_pages(my_book))

book_parser_from_list(my_book_list)
print(get_set_of_authors(my_book_list))
print(get_total_pages(my_book_list))
