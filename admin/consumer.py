import pika

params= pika.URLParameters('amqps://mjgofspf:oORFSE4xbwGQ_HdOznFly3iVsgn0gAIs@crow.rmq.cloudamqp.com/mjgofspf')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="admin")

def callback(db, method, properties, body):
    print('received in admin')
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('started consuming')

channel.start_consuming()

channel.close()