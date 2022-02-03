books = {
    9780553078756:{'title':'Ishmael', 'author':'Daniel Quinn', 'page count': 217},
    9788845292613:{'title':'The Lord of the Rings', 'author':'J.R.R. Tolkien', 'page count':1128},
    9780316074292:{'title':'The Luminaries','author':'Eleanor Catton', 'page count':583}
}
for isbn,book_info in books.items():
    print(f"\nISBN {isbn}:")
    title = book_info['title']
    author = book_info['author']
    pageCount = book_info['page count']

    print(f"\tTitle: {title}")
    print(f"\tAuthor: {author}")
    print(f"\tPage count: {pageCount}")