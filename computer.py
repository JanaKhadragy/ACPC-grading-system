import time
import queue

def process_task(task_queue, results_queue, computers_available):
    while True:
        try:
            task = task_queue.get(timeout=1)
            
            with computers_available.get_lock():
                computers_available.value -= 1
            
            task.start_time = time.time()
            
            remaining_time = task.service_time
            while remaining_time > 0:
                sleep_interval = min(10, remaining_time)
                time.sleep(sleep_interval)
                remaining_time -= sleep_interval
                if sleep_interval == 10:
                    print(f"Task {task.id} - {(task.service_time - remaining_time) / task.service_time * 100:.1f}% complete")
            
            task.completion_time = time.time()
            
            with computers_available.get_lock():
                computers_available.value += 1
            
            results_queue.put(task)
            
        except queue.Empty:
            continue
        except Exception as e:
            print(f"Error processing task: {str(e)}")
            continue
