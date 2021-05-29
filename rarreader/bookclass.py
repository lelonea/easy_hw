"""Есть архив с книгами, необходимо сделать программу помощник читателя
c использованием ООП. Программа должна принять от пользователя слово
или некоторое количество слов, в ответ программа должна выдать все названия книг
в тексте которых есть все введенные пользователем слова."""

from rarfile import RarFile


class BookSearch:

    def __init__(self, search_word):
        self.search_word = search_word
        with RarFile('books.rar') as rar:
            self.dir_list = rar.namelist()
        self.book_list = []
        for bookpath in self.dir_list:
            self.book_list.append(bookpath.replace('books/', ''))

    def search_result(self):
        pass


def run():
    search_word = input('Enter word to search')
    search = BookSearch(search_word)
    search.search_result()
