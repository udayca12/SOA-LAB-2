import pika
import json

def publish_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='order_queue')

    message = {
        "order_id": 123,
        "item": "Laptop",
        "status": "new"
    }

    channel.basic_publish(
        exchange='',
        routing_key='order_queue',
        body=json.dumps(message)
    )
    print(" [x] Sent message:", message)

    connection.close()

if __name__ == "__main__":
    publish_message()
