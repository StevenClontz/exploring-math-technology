book_table = book_table.with_columns([
    "Peter", [c.count("Peter") for c in book_chapters],
    "Tink", [c.count("Tink") for c in book_chapters],
])
book_table.show()