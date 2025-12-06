from kafka import KafkaConsumer
import json
import logging
import time

# Set up detailed logging
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Enable Kafka client logging
kafka_logger = logging.getLogger("kafka")
kafka_logger.setLevel(logging.DEBUG)

try:
    consumer = KafkaConsumer(
        "otp-topic",
        bootstrap_servers="localhost:29092",
        group_id="otp-consumer-group",
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        auto_commit_interval_ms=5000,  # Commit every 5 seconds
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        consumer_timeout_ms=10000,  # 10 second timeout for testing
    )

    print("Consumer created successfully!")
    print(f"Consumer configuration: {consumer.config}")
    print(f"Subscribed topics: {consumer.subscription()}")
    print(f"Consumer group ID: {consumer.config['group_id']}")

    # Check if topic exists and get partitions
    print(f"Available topics: {consumer.topics()}")

    # Poll once to trigger group coordination
    print("Polling for messages...")

    message_count = 0
    for message in consumer:
        message_count += 1
        print(f"Message {message_count}:")
        print(f"  Topic: {message.topic}")
        print(f"  Partition: {message.partition}")
        print(f"  Offset: {message.offset}")
        print(f"  Value: {message.value}")
        print(f"  Timestamp: {message.timestamp}")
        print("-" * 50)

        # Manually commit after processing
        consumer.commit()

        # Add a small delay to see the consumer group in UI
        time.sleep(1)

except KeyboardInterrupt:
    print("Consumer interrupted by user")
except Exception as e:
    print(f"Error: {e}")
    logging.exception("Consumer error")
finally:
    if "consumer" in locals():
        consumer.close()
        print("Consumer closed")
