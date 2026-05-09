"""
Week 05 - Transactions: Multi-step writes should stay consistent.

This file demonstrates the idea of grouping related operations together.
"""

import sqlite3


def create_tables(connection):
    """Create two small tables for the transaction example."""
    connection.executescript(
        """
        CREATE TABLE accounts (
            id INTEGER PRIMARY KEY,
            owner_name TEXT NOT NULL,
            balance INTEGER NOT NULL
        );

        CREATE TABLE transfers (
            id INTEGER PRIMARY KEY,
            from_account_id INTEGER NOT NULL,
            to_account_id INTEGER NOT NULL,
            amount INTEGER NOT NULL
        );
        """
    )


def seed_accounts(connection):
    """Insert two accounts with starting balances."""
    connection.executemany(
        "INSERT INTO accounts (owner_name, balance) VALUES (?, ?)",
        [("Asha", 1000), ("Ravi", 700)],
    )


def transfer_money(connection, from_account_id, to_account_id, amount):
    """Transfer money between accounts as one transaction boundary."""
    with connection:
        connection.execute(
            "UPDATE accounts SET balance = balance - ? WHERE id = ?",
            (amount, from_account_id),
        )
        connection.execute(
            "UPDATE accounts SET balance = balance + ? WHERE id = ?",
            (amount, to_account_id),
        )
        connection.execute(
            """
            INSERT INTO transfers (from_account_id, to_account_id, amount)
            VALUES (?, ?, ?)
            """,
            (from_account_id, to_account_id, amount),
        )


def show_balances(connection):
    """Print the current balances for both accounts."""
    rows = connection.execute(
        "SELECT owner_name, balance FROM accounts ORDER BY id"
    ).fetchall()

    for owner_name, balance in rows:
        print(f"{owner_name}: {balance}")


def main():
    """Run the small transaction demo."""
    connection = sqlite3.connect(":memory:")
    create_tables(connection)
    seed_accounts(connection)

    print("Before transfer:")
    show_balances(connection)

    transfer_money(connection, from_account_id=1, to_account_id=2, amount=200)

    print("-" * 40)
    print("After transfer:")
    show_balances(connection)


if __name__ == "__main__":
    main()
