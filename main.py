"""
Module for interacting with Apache Kafka.

This module provides functions for producing and consuming messages from Apache Kafka topics.

Usage:
    To produce a message to a Kafka topic:
        python main.py produce --topic 'my_topic' --kafka 'ip:port' --message 'Hello, Kafka!'

    To consume messages from a Kafka topic:
        python main.py consume --topic 'my_topic' --kafka 'ip:port'
"""

import asyncio
from argparse import ArgumentParser
from typing import List

from aiokafka import AIOKafkaProducer, AIOKafkaConsumer


async def produce_message(bootstrap_servers: List[str], topic: str, message: str) -> None:
    """
    Produce a message to Kafka topic.

    Args:
        bootstrap_servers (List[str]): List of Kafka server addresses.
        topic (str): Kafka topic to produce message to.
        message (str): Message to be produced to Kafka topic.

    Returns:
        None
    """

    producer = AIOKafkaProducer(bootstrap_servers=bootstrap_servers)

    await producer.start()
    await producer.send_and_wait(topic, message.encode('utf-8'))
    await producer.stop()

    print(f"Message '{message}' produced to topic '{topic}'")


async def consume_messages(
        bootstrap_servers: List[str],
        topic: str,
        group_id: str,
        auto_offset_reset: str = 'earliest'
) -> None:
    """
    Consume messages from Kafka topic.

    Args:
        bootstrap_servers (List[str]): List of Kafka server addresses.
        topic (str): Kafka topic to consume messages from.
        group_id (str): The consumer group id.
        auto_offset_reset (str, optional): A string specifying what to do when there is
        no initial offset in Kafka or if the current offset does not exist any more on the server.
            Possible values:
                'earliest' to automatically reset the offset to the earliest offset,
                'latest' to automatically reset the offset to the latest offset,
                'none' to throw an exception if no previous offset is found.
            Default is 'earliest'.

    Returns:
        None
    """

    consumer = AIOKafkaConsumer(
        topic,
        bootstrap_servers=bootstrap_servers,
        group_id=group_id,
        auto_offset_reset=auto_offset_reset,
    )

    await consumer.start()

    try:
        async for message in consumer:
            print(f"Received message: {message.value.decode('utf-8')}")
            await consumer.commit()
    finally:
        await consumer.stop()


if __name__ == "__main__":
    parser = ArgumentParser(description='Apache Kafka interaction script')
    parser.add_argument('action', choices=['produce', 'consume'], help='Action to perform')
    parser.add_argument('--topic', help='Kafka topic')
    parser.add_argument('--kafka', help='Kafka server address')
    parser.add_argument('--message', help='Message to produce')

    args = parser.parse_args()

    if args.action == 'produce':
        asyncio.run(produce_message([args.kafka], args.topic, args.message))
    elif args.action == 'consume':
        group_id = "hello_consumer"
        asyncio.run(consume_messages([args.kafka], args.topic, group_id))
