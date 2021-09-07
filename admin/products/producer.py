import pika
import json

params= pika.URLParameters('amqps://mjgofspf:oORFSE4xbwGQ_HdOznFly3iVsgn0gAIs@crow.rmq.cloudamqp.com/mjgofspf')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    print('publishing to main')
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange = '', routing_key='main', body=json.dumps(body), properties=properties)