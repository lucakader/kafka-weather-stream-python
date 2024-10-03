from kafka import KafkaConsumer
from kafka import TopicPartition
import report_pb2

broker = "localhost:9092"

def debug_consumer():
    consumer = KafkaConsumer(bootstrap_servers=[broker])
    consumer.subscribe(["temperatures"])

    try:
        while True:
            batch = consumer.poll(1000)
            for topic_partition, messages in batch.items():
                for msg in messages:
                    report_message = report_pb2.Report()
                    report_message.ParseFromString(msg.value)
                    debug_dict = {
                    "partition": topic_partition.partition,
                    "key": msg.key.decode("utf-8") if msg.key else None,
                    "date": report_message.date,
                    "degrees": report_message.degrees,
                    }
                    print(debug_dict)
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

if __name__ == "__main__":
    debug_consumer()
