export interface Book {
  id: string;
  title: string;
  author: string;
  tags: string[];
  isRead: boolean;
}

export interface CreateBookInput {
  title: string;
  author: string;
  tags?: string[];
}
