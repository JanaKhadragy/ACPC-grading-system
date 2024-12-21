def calculate_waiting_time(task):
    wait_time = task.start_time - task.arrival_time
    return wait_time

def calculate_delay_time(task):
    delay_time = task.completion_time - task.arrival_time
    return delay_time

def process_results(results_queue):
    waiting_times = []
    delay_times = []
    
    while not results_queue.empty():
        task = results_queue.get()
        waiting_times.append(calculate_waiting_time(task))
        delay_times.append(calculate_delay_time(task))
    
    return waiting_times, delay_times

def calculate_statistics(waiting_times, delay_times, queue_lengths):
    return {
        'avg_waiting_time': sum(waiting_times) / len(waiting_times) if waiting_times else 0,
        'avg_delay_time': sum(delay_times) / len(delay_times) if delay_times else 0,
        'avg_queue_length': sum(queue_lengths) / len(queue_lengths) if queue_lengths else 0
    }
