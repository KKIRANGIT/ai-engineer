import type { Book } from "./models";

export type ApiSuccess<T> = {
  data: T;
};

export type ApiError = {
  error: string;
  message: string;
  details?: string[];
};

export type BookListResponse = ApiSuccess<Book[]>;
export type BookDetailResponse = ApiSuccess<Book>;
export type CreateBookResponse = ApiSuccess<Book> | ApiError;
