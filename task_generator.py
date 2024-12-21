import random
import time
from dataclasses import dataclass

@dataclass
class Task:
    id: int
    arrival_time: float
    service_time: float
    start_time: float = None
    completion_time: float = None

def generate_service_time(mean_service_time):
    return random.expovariate(1.0 / mean_service_time)

def generate_arrival_interval(mean_arrival_time):
    return random.expovariate(1.0 / mean_arrival_time)

def create_task(task_id, mean_service_time):
    current_time = time.time()
    task = Task(
        id=task_id,
        arrival_time=current_time,
        service_time=generate_service_time(mean_service_time)
    )
    return task
