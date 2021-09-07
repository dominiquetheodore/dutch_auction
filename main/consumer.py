import pika
import json
from main import Product, db

print('===> inside consumer - main <===')

params= pika.URLParameters('amqps://mjgofspf:oORFSE4xbwGQ_HdOznFly3iVsgn0gAIs@crow.rmq.cloudamqp.com/mjgofspf')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="main")

def callback(ch, method, properties, body):
    print('received in main')
    data = json.loads(body)
    print(data)

    if properties.content_type == 'product created':
        product = Product(id=data['id'], title=data['title'], image=data['image'])
        db.session.add(product)
        db.session.commit()
        print('product created')

channel.basic_consume(queue='main', on_message_callback=callback)

print('started consuming')

channel.start_consuming()

# channel.close()

"""
  flower:
    build: .
    command: 'celery -A admin flower'
    volumes:
      - .:/app
    working_dir: /data
    ports:
      - 5555:5555
    environment:
      CELERY_BROKER_URL: redis://redis
      CELERY_RESULT_BACKEND: redis://redis
    depends_on:
      - celery
      - redis
"""