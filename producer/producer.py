from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers="localhost:29092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)


def send_otp_event(rider_id, customer_id):
    event = {
        "rider_id": rider_id,
        "customer_id": customer_id,
        "event": "arrived_at_destination",
        "timestamp": time.time(),
    }
    producer.send("otp-topic", event)
    print(f"Sent OTP event for rider: {rider_id}")


if __name__ == "__main__":
    for i in range(10):
        send_otp_event(f"rider_{i}", f"cust_{i}")
    producer.flush()  # wait for all messages to be sent
    producer.close()  # shutdown cleanly
