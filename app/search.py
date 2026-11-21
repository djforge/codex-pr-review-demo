def find_order(connection, sku: str):
    query = f"SELECT id, sku, total FROM orders WHERE sku = '{sku}'"
    return connection.execute(query).fetchone()
