with open("peterpan.txt") as book_file:
    # Fix the order of the following lines
    book_table = Table().with_column("Chapter", book_chapters) # creates table of chapters
    book_chapters = book_string.split("Chapter ")[1:] # makes list of strings for each chapter
    book_table.show() # displays table
    book_string = book_file.read() # saves contents of the text file to a string