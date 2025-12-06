# OTP Monitoring System

This project demonstrates a real-time monitoring system for an OTP (One-Time Password) delivery service using Kafka, Prometheus, and Grafana. It simulates OTP events being produced by a rider app and consumed by a backend service, with metrics being visualized in Grafana.

## Architecture

-   **Producer (`app.py` / `producer/`)**: A FastAPI application that acts as the source of OTP events. It sends messages to a Kafka topic.
-   **Kafka**: Message broker handling the event stream.
-   **Consumer (`consumer/`)**: A Python script that consumes messages from the Kafka topic.
-   **Kafka Exporter**: Exports Kafka metrics to Prometheus.
-   **Prometheus**: Collects and stores metrics.
-   **Grafana**: Visualizes metrics from Prometheus.
-   **Kafka UI**: Web UI for managing and monitoring Kafka clusters.

## Prerequisites

-   Docker and Docker Compose
-   Python 3.9+

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd otp-sharing
    ```

2.  **Start the infrastructure services:**
    ```bash
    docker-compose up -d
    ```
    This will start Kafka, Zookeeper (embedded in Kafka 4.0), Kafka UI, Prometheus, Grafana, and Kafka Exporter.

3.  **Install Python dependencies:**
    It is recommended to use a virtual environment.
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

## Usage

### 1. Start the Producer API
Run the FastAPI application which exposes an endpoint to trigger OTP events.
```bash
uvicorn app:app --reload
```
The API will be available at `http://localhost:8000`.

### 2. Start the Consumer
Run the consumer script to process messages from Kafka.
```bash
python consumer/consumer.py
```

### 3. Trigger OTP Events
You can trigger events using `curl` or by visiting the Swagger UI at `http://localhost:8000/docs`.

**Using curl:**
```bash
curl -X 'POST' \
  'http://localhost:8000/send' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "rider_id": "rider_123",
  "customer_id": "cust_456"
}'
```

## Monitoring

Access the following dashboards to monitor the system:

-   **Grafana**: [http://localhost:3000](http://localhost:3000)
    -   Default login: `admin` / `admin` (you may be asked to change the password).
    -   You can add Prometheus as a data source (URL: `http://prometheus:9090`) and import dashboards for Kafka Exporter.

-   **Prometheus**: [http://localhost:9090](http://localhost:9090)
    -   View raw metrics and targets.

-   **Kafka UI**: [http://localhost:8080](http://localhost:8080)
    -   View topics, messages, and consumer groups.
