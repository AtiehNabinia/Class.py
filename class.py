class Book:
    library_name='Markazi'
    book_count=0
    def __init__(self,titel,writer,page):
        self.page=page
        self.writer=writer
        self.titel=titel
        Book.book_count +=1
    def show_book(self):
        print(f'book name:{self.titel}')
        print(f'writer={self.writer}')
        print(f'library={Book.library_name}')
        print('-'*30)

Book1=Book('badam','Son Won Pyung',171)
Book1.show_book()
Book2=Book('melat ashgh','Elif Shafak',480)
Book2.show_book()
Book3=Book('The Monk Who Sold His Ferrari','Robin Sharma',191)
Book3.show_book()

print(f'book count={Book.book_count}')
print(f'library={Book.library_name}')