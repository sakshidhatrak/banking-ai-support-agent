import time
import logging


logging.basicConfig(
    filename="logs/runtime_monitor.log",
    level=logging.INFO
)


def monitor_latency(function):

    def wrapper(*args, **kwargs):

        start_time = time.time()

        result = function(*args, **kwargs)

        end_time = time.time()

        latency = end_time - start_time

        logging.info(
            f"Latency: {latency:.2f} seconds"
        )

        return result

    return wrapper