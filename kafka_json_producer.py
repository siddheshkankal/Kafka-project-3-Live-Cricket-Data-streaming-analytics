


# A simple example demonstrating use of JSONSerializer.

import argparse
import json
import requests
from msilib.schema import Registry
from uuid import uuid4
from six.moves import input
from confluent_kafka import Producer
from confluent_kafka.serialization import StringSerializer, SerializationContext, MessageField
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.json_schema import JSONSerializer
#from confluent_kafka.schema_registry import *
import pandas as pd
from typing import List




API_KEY = 'A6IN47KT7DECACSV'
ENDPOINT_SCHEMA_URL  = 'https://psrc-zj6ny.us-east-2.aws.confluent.cloud'
API_SECRET_KEY = 'OYLYcDWBYYQjogIpVOVSpr3458ZobfHMKTxeOwDC/2dtn9YE6tDhowRWA4bYMX1h'
BOOTSTRAP_SERVER = 'pkc-ymrq7.us-east-2.aws.confluent.cloud:9092'
SECURITY_PROTOCOL = 'SASL_SSL'
SSL_MACHENISM = 'PLAIN'
SCHEMA_REGISTRY_API_KEY = 'GRBH4TYEXHJIKAD3'
SCHEMA_REGISTRY_API_SECRET = 'S3fIxbfFMAr15wB4dp9BjQegt/hnk2XxnGXYGSMERww6uT5UZW/XKMkdwT19uV2o'


def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    return sasl_conf



def schema_config():
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

    }




def delivery_report(err, msg):
    """
    Reports the success or failure of a message delivery.
    Args:
        err (KafkaError): The error that occurred on None on success.
        msg (Message): The message that was produced or failed.
    """

    if err is not None:
        print("Delivery failed for User record {}: {}".format(msg.key(), err))
        return
    print('User record {} successfully produced to {} [{}] at offset {}'.format(
        msg.key(), msg.topic(), msg.partition(), msg.offset()))


def main(topic):



    schema_registry_conf = schema_config()
    schema_registry_client = SchemaRegistryClient(schema_registry_conf)

#********************  first approact to get schema from schema Registry using subjects  ********************
    # subjects = schema_registry_client.get_subjects()
    # for sub in subjects:
    #     if sub == 'student-exams-data-value':
    #         schema = schema_registry_client.get_latest_version(sub)
    #         schema_str = schema.schema.schema_str

#********************  second  approact to get schema from schema Registry using schema_id  ********************    
    schema_str = schema_registry_client.get_schema(schema_id = 100003).schema_str
    

    url = 'https://api.cricapi.com/v1/currentMatches?apikey=8990f916-8107-4f70-9e8e-dcbd9639b687&offset=0'

    download  = requests.get(url).text
    json_data = json.loads(download)

    string_serializer = StringSerializer('utf_8')
    # json_serializer = JSONSerializer(schema_str, schema_registry_client, json_data['data'])

    # res = json.dumps( json_data['data'][i] )
    # print( res )

    producer = Producer(sasl_conf())

    print("Producing user records to topic {}. ^C to exit.".format(topic))
    #while True:
        # Serve on_delivery callbacks from previous calls to produce()
    producer.poll(0.0)

    # info --> counter is used to know how many records published to the topic 
    counter = 0
    try:
        for i in range(len(json_data['data'])): 
        
            print(json_data['data'][i])
            producer.produce(topic=topic,
                                key=string_serializer(str(uuid4()),(json.dumps( json_data['data'][i]['id'] ))),
                                # string_serializer(str(uuid4()), json_data['data'][i]['id']),
                                value=json.dumps( json_data['data'][i] ),
                                on_delivery=delivery_report)
            counter += 1

            # info --> loop is break when counter is 5 because we want to publish only 5 records as of now
            if counter == 2:
                break

        # info --> printing at the end how many records got published successfully 
        print(f'totoal number of recorded published are : {counter}')

    except KeyboardInterrupt:
        pass
    except ValueError:
        print("Invalid input, disrestaurantding record...")
        pass

    print("\nFlushing records...")
    producer.flush()

main("cricket-live-data")
