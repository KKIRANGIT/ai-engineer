/**
 * Week 07 Exercise
 * ----------------
 * This file introduces the JavaScript data and function patterns that most
 * Node and frontend code relies on every day.
 */

const books = [
  { title: "Designing Data-Intensive Applications", pages: 616, finished: false },
  { title: "Clean Code", pages: 464, finished: true },
  { title: "Refactoring", pages: 448, finished: false },
];

function getFinishedBooks(items) {
  return items.filter((book) => book.finished);
}

function getBookTitles(items) {
  return items.map((book) => book.title);
}

function createReadingSummary(name, items) {
  const totalPages = items.reduce((sum, book) => sum + book.pages, 0);
  return `${name} is tracking ${items.length} books totaling ${totalPages} pages.`;
}

function printObjectDestructuringExample(book) {
  const { title, pages } = book;
  console.log(`Destructured book -> title: ${title}, pages: ${pages}`);
}

function main() {
  console.log("All titles:", getBookTitles(books));
  console.log("Finished books:", getFinishedBooks(books));
  console.log(createReadingSummary("Asha", books));
  printObjectDestructuringExample(books[0]);
}

main();
