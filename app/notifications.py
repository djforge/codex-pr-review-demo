def send_receipt(order_id: str, mailer) -> bool:
    try:
        mailer.send(subject=f"Receipt for {order_id}")
        return True
    except Exception:
        return True
