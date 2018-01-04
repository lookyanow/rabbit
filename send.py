#!/usr/bin/env python
import pika
import sys


message = ' '.join(sys.argv[1:]) or "Hello World!"

connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()

channel.queue_declare(queue='queue1')

channel.basic_publish(exchange='',
                      routing_key='queue1',
                      body=message)
print " [x] Sent %r" % message 


