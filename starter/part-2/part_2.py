### Step 1 - Lists ###

# Fill in this list with several authors you are a fan of. At least 7 or 8 should do.
my_authors = ["J.K. Rowling", "Ernest Hemingway", "Jane Austen", "Mark Twain", "Harper Lee", "William Shakespeare", "George Orwell", "Agatha Christie"]

# Now let's add a new author to the end with the .append() method. Type your code below.
# Code here
my_authors.append("Stephen King")

# Now let's remove an element in the list
# Code here
my_authors.remove("Stephen King")

# Now access an element by it's index. (Remember it indexes start at 0.)
# Code here
author_5 = my_authors[4]

# Now slice the list.
# Code here
authors_2_through_7 = my_authors[1:6]



### Step 2 - Tuples ###

# Create your tuple below. Assign it to a variable name you can reference later in the exercise.
# Code here
my_authors_tuple = ("J.K. Rowling", "Ernest Hemingway", "Jane Austen", "Mark Twain", "Harper Lee", "William Shakespeare", "George Orwell", "Agatha Christie")



### Step 3 - Sets ###

# Create a set with your authors.
# Code here
my_authors_set = {"J.K. Rowling", "Ernest Hemingway", "Jane Austen", "Mark Twain", "Harper Lee", "William Shakespeare", "George Orwell", "Agatha Christie"}
print(my_authors_set)

# Add a new author to your set.
# Code here
my_authors_set.add("Luke Lyons")
print(my_authors_set)

# Try adding the same author again, and be sure to print your set.
# Code here
my_authors_set.add("Luke Lyons")
print(my_authors_set)



### Step 4 - For Loops ###

# Create a for-loop for each of the data-structures above.
# Code here
for author in my_authors:
    print(author)

for author in my_authors_tuple:
    print(author)

for author in my_authors_set:
    print(author)

