function createBookId(existingBooks) {
  return `book-${existingBooks.length + 1}`;
}

export class BookService {
  constructor(storage) {
    this.storage = storage;
  }

  async listBooks() {
    return this.storage.loadBooks();
  }

  async getBookById(id) {
    const books = await this.storage.loadBooks();
    return books.find((book) => book.id === id) ?? null;
  }

  async createBook(input) {
    const books = await this.storage.loadBooks();

    const newBook = {
      id: createBookId(books),
      title: input.title.trim(),
      author: input.author.trim(),
      tags: input.tags ?? [],
      isRead: false,
    };

    const updatedBooks = [...books, newBook];
    await this.storage.saveBooks(updatedBooks);
    return newBook;
  }

  async markBookAsRead(id) {
    const books = await this.storage.loadBooks();
    const book = books.find((item) => item.id === id);

    if (!book) {
      return null;
    }

    book.isRead = true;
    await this.storage.saveBooks(books);
    return book;
  }
}
