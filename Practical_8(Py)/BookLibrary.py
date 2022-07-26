# Making a  function for library to issue a book, check if the given book is present or not in the library and to the return book

def issue_book(title):
    if title in lib:
        lib[title] -= 1
        print(title, 'is issued.')

        if lib[title] == 0:
            del lib[title]

        if title in issued_books:
            issued_books[title] += 1
        else:
            issued_books[title] = 1

    else:
        print(title, "is not available.")


def checkif(title):
    if title in lib:
        print(lib[title], 'copies of', title, 'are available.')
    else:
        print(title, "is not available.")


def return_book(title):
    if title in lib:
        lib[title] += 1
        print(title, 'is returned.')
    else:
        lib[title] = 1
        print("Now available:", title)

    if title in issued_books:
        issued_books[title] -= 1
        if issued_books[title] == 0:
            del issued_books[title]


lib = {
    'Thinking fast and slow': 2 ,
    'Steve Jobs': 1,
    'Ikigai': 1,
    'The Power of Habit': 2,
    'Atomic Habits': 4,
    'Mindset': 2,
    'Rich Dad Poor Dad': 5,
    'Smart Thinking': 3 ,
    'Start With Why': 2
}

issued_books = {}

issue_book('Steve Jobs')
checkif('Rich Dad Poor Dad')
issue_book('Smart Thinking')
checkif('Smart Thinking')
issue_book('Atomic Habits')
checkif('Mindset')
return_book('The Power of Habit')
return_book('Ikigai')