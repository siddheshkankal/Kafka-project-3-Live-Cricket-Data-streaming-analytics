# Kafka-project-3-Live-Cricket-Data-streaming-analytics

<h1 align="center">Hi 👋, I'm Siddhesh Kankal</h1>
<h3 align="center">A passionate data engineer</h3>


- 🔭 I’m currently working on [Kafka-project-2-on-Exam-result-streaming-analytics-](https://github.com/siddheshkankal/Kafka-project-2-on-Exam-result-streaming-analytics-/)

- 👨‍💻 All of my projects are available at [https://github.com/siddheshkankal](https://github.com/siddheshkankal)

- 📝 I regularly write articles on [Data engineering tech stack](Data engineering tech stack)

- 📫 How to reach me **dksidd96@gmail.com**

<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://linkedin.com/in/https://www.linkedin.com/in/siddhesh-kankal-bhavsar-20101996" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://www.linkedin.com/in/siddhesh-kankal-bhavsar-20101996" height="30" width="40" /></a>
</p>

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a> <a href="https://hadoop.apache.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/apache_hadoop/apache_hadoop-icon.svg" alt="hadoop" width="40" height="40"/> </a> <a href="https://hive.apache.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/apache_hive/apache_hive-icon.svg" alt="hive" width="40" height="40"/> </a> <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Architecture](#Architecture)
* [Setup](#setup)

## General info
This project is about Student's Exams result streaming Analytics.
	
## Technologies
Project is created with:
* Confluent Kafka
* PySpark
* Python
	
## Architecture
![architecture](https://user-images.githubusercontent.com/60224016/229360562-fb60e7cf-08e3-45e6-93e6-1ca66ff0157e.jpg)



##Apache Kafka: 
Apache Kafka is a distributed event streaming platform. With an ability to allow applications to manage large amounts of data,Kafka is also fault-tolerant and built to scale. Apache Kafka’s framework is based on Java and the Publish-Subscribe Messaging system. The framework allows data streaming at an unprecedented rate, that too, from multiple sources Kafka is famous in the data community for data streaming services because it can handle Big Data with large input volumes. And, with minimum downtime and low latency, Kafka services are easy to scale up and down.

##Some of Kafka’s most valuable features are as follows:
##High Scalability: 
The partitioned log model allows Kafka services to scale beyond a single server’s capability.
##Low Latency: 
Kafka services separate data streams, allowing low latency and high throughput.
Fault-Tolerant & Durable: In Kafka, partitions are segregated then duplicated across servers. The segregation and duplication process makes Kafka services fault-tolerant by protecting them against ad-hoc server failures like master and database failures. 
High Extensibility: Kafka is highly accessible through various other applications, allowing developers to add more features. 

##problem statment :- 
to create a data pipeline, suppose we have to a pull a data from source and through kafka topic we need to collect that data into target. kafka has a pubsub architecture, prducer is responsible to publish a data into kafka broker inside specific topic (specific area to store some related logical data) into specific partitions and consumer is responsible for to subscribe (read data from topic) data from those partitions. so here use case is like here in terms of source we are pulling data from API  link for live cricket data and dumping data into kafka broker-topic  and from there we are reading data and storing  in output excel.



Detailed Explanation: 
In this project we are getting raw data of cricket live cricket throgh API and through producer code we are producing (or we can say sending data) to 
kafka topic as this is POC project we have only one node cluster kafka setup
and on the other hand we are consuming the data through consumer code(or we can say subsribing the records)
and we are dumping the result set into seperate excel files.


## Setup
To run this project, install it locally:

Then on the Spark shell run the below command from CLI
```
$ Python kafka_producer.py
```
and in another seperate command prompt 
```
$ Python kafka_consumer.py 

```
