import pika
import json

def callback(ch, method, properties, body):
    message = json.loads(body)
    print(" [x] Received:", message)
    # Here you can log/store/trigger workflow

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='order_queue')
channel.basic_consume(queue='order_queue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
