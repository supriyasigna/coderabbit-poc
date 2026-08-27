import os
import sqlite3
import json


def connect_db():
    conn = sqlite3.connect("inventory.db")
    return conn


def get_item_by_name(conn, name):
    # BUG: SQL injection via string formatting instead of parameterized query
    query = "SELECT * FROM items WHERE name = '%s'" % name
    cursor = conn.execute(query)
    return cursor.fetchone()


def add_discount(prices, discount=0.1, seen=[]):
    # BUG: mutable default argument (classic Python gotcha)
    seen.append(discount)
    return [p - (p * discount) for p in prices]


def average_price(prices):
    # BUG: divide by zero not handled when prices is empty
    total = sum(prices)
    return total / len(prices)


def find_duplicates(items):
    # BUG: O(n^2) nested loop where a set/dict would be O(n)
    duplicates = []
    for i in range(len(items)):
        for j in range(len(items)):
            if i != j and items[i] == items[j] and items[i] not in duplicates:
                duplicates.append(items[i])
    return duplicates


def load_config(path):
    try:
        with open(path) as f:
            return json.load(f)
    except:
        # BUG: bare except swallows all errors silently
        return {}


def apply_bulk_update(conn, item_ids, new_price):
    # BUG: off-by-one, skips the last item in the list
    for i in range(len(item_ids) - 1):
        conn.execute(
            "UPDATE items SET price = ? WHERE id = ?", (new_price, item_ids[i])
        )
    conn.commit()


def get_env_key():
    # BUG: hardcoded secret instead of reading from environment safely
    api_key = "sk-live-12345-hardcoded-secret"
    return api_key


if __name__ == "__main__":
    conn = connect_db()
    prices = [10.0, 20.0, 30.0]
    print(average_price(prices))
    print(add_discount(prices))
