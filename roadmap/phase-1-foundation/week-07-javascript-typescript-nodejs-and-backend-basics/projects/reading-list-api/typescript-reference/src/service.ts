import type { Book, CreateBookInput } from "./models";

export interface BookRepository {
  loadBooks(): Promise<Book[]>;
  saveBooks(books: Book[]): Promise<void>;
}

export class BookService {
  constructor(private readonly repository: BookRepository) {}

  async listBooks(): Promise<Book[]> {
    return this.repository.loadBooks();
  }

  async getBookById(id: string): Promise<Book | null> {
    const books = await this.repository.loadBooks();
    return books.find((book) => book.id === id) ?? null;
  }

  async createBook(input: CreateBookInput): Promise<Book> {
    const books = await this.repository.loadBooks();

    const newBook: Book = {
      id: `book-${books.length + 1}`,
      title: input.title.trim(),
      author: input.author.trim(),
      tags: input.tags ?? [],
      isRead: false,
    };

    await this.repository.saveBooks([...books, newBook]);
    return newBook;
  }
}
