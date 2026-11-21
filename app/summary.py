from app.orders import Order


def order_summary(order: Order) -> str:
    return f"{order.quantity} × {order.sku}: ${order.total():.2f}"
