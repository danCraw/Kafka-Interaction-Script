# Apache Kafka Interaction Script

This Python script allows you to produce and consume messages from Apache Kafka topics.

## Usage
### Note
 Before using the producer and consumer, ensure that your Kafka broker is running \
 and accessible at the specified IP address and port.

### Docker
 To run the Kafka broker using Docker, run:

```
docker-compose up -d
```

This will start Kafka and Zookeeper containers in the background.

After starting Kafka and Zookeeper containers, you can use the producer and \
consumer scripts to interact with Kafka as described above.

Now you can produce and consume messages from your Kafka topics using the provided scripts.

### Usage Examples

#### Producing a Message
To produce message to Kafka topic, run:

```bash
python main.py produce --topic 'hello_topic' --kafka 'ip:port' --message 'Hello, Kafka!'
```

#### Consuming Message
To consume message from Kafka topic, run:

```bash
python main.py produce --topic 'hello_topic' --kafka 'ip:port' --message 'Hello, Kafka!'
```