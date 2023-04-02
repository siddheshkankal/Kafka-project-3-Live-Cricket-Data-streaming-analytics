import argparse
import os.path
import csv
import json 
from confluent_kafka import Consumer
from confluent_kafka.serialization import SerializationContext, MessageField
from confluent_kafka.schema_registry.json_schema import JSONDeserializer
from confluent_kafka.schema_registry import SchemaRegistryClient


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


# *************** function to write data export to abn excel file which ever data subscribed by consumer ***************
def export_data_excel(header,data,path):
    file_exists = os.path.isfile(path)

    with open(path,'a', newline = '') as f:
        w = csv.DictWriter(f,fieldnames= header)
        if not file_exists:
            w.writeheader()
        w.writerow(data)
        
def main(topic):

    schema_registry_conf = schema_config()
    schema_registry_client = SchemaRegistryClient(schema_registry_conf)

# Info --> ****************** approch 1 to get schema from schema registry using subject ******************
    # subjects = schema_registry_client.get_subjects()
    # for sub in subjects:
    #     if sub == 'student-exams-data-value':
    #         schema = schema_registry_client.get_latest_version(sub)
    #         schema_str = schema.schema.schema_str

# Info --> ****************** approch 2 to get schema from schema registry using schema id ******************

    # schema_str = schema_registry_client.get_schema(schema_id = 100003).schema_str       
    

    consumer_conf = sasl_conf()
    consumer_conf.update({
                     'group.id': 'group1',
                     'auto.offset.reset': "earliest"})

    consumer = Consumer(consumer_conf)
    consumer.subscribe([topic])

    counter = 0
    
    # path = './output.csv'
    while True:
        try:
            # SIGINT can't be handled when polling, limit timeout to 1 second.
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            
            # print(type(msg.value()))
            data = (msg.value().decode('utf-8'))
            json_data = json.loads(data)
            # print(json_data)
            
            # header = list(json_data.keys())
            # print(header)
            # export_data_excel(header,json_data,'./output.csv')

            if json_data is not None:
                print("User record {}: cricket data: {}\n".format(msg.key(), json_data))
                header = list(json_data.keys()) 
                export_data_excel(header,json_data,'./output.csv')      
            

                
            counter+= 1
            print(f'totoal number of recorded subscribed are : {counter}')

        except KeyboardInterrupt:
            break

    consumer.close()

main("cricket-live-data")


# import json
 
# # creating the JSON data as a string
# data = '{"Name" : "Romy", "Gender" : "Female"}'
 
# print("Datatype before deserialization : "
#       + str(type(data)))
  
# # deserializing the data
# data = json.loads(data)
 
# print("Datatype after deserialization : "
#       + str(type(data)))