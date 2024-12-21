import multiprocessing as mp
import time
from datetime import datetime, timedelta

from task_generator import create_task, generate_arrival_interval
from computer import process_task
from queue_statistics import process_results, calculate_statistics
#I scaled the mean service time and arrival time to 1/60 of the original values
NUM_COMPUTERS = 3
MEAN_SERVICE_TIME = 42/300 
MEAN_ARRIVAL_TIME = 35/300  
SIMULATION_HOURS = 1/60     

def write_results_to_file(queue_lengths, waiting_times, completion_times):
    with open('simulation_results.txt', 'w') as f:
        f.write("=== ACPC Grading System Simulation Results ===\n\n")
        f.write(f"Average Queue Length: {sum(queue_lengths) / len(queue_lengths):.2f}\n\n")
        f.write(f"Average Waiting Time: {sum(waiting_times) / len(waiting_times):.2f} minutes\n\n")
        f.write(f"Average Completion Time: {sum(completion_times) / len(completion_times):.2f} minutes\n")

def run_simulation():
    task_queue = mp.Queue()
    results_queue = mp.Queue()
    computers_available = mp.Value('i', NUM_COMPUTERS)
    queue_lengths = []
    queue_size = 0  
    task_id = 0

    processes = []
    for i in range(NUM_COMPUTERS):
        p = mp.Process(
            target=process_task, 
            args=(task_queue, results_queue, computers_available)
        )
        p.daemon = True
        p.start()
        processes.append(p)

    print("Starting simulation...")
    start_time = time.time()
    end_time = start_time + 60
    
    while time.time() < end_time:
        current_time = time.time()
        elapsed = current_time - start_time
        total_duration = 60
        progress = (elapsed / total_duration) * 100
        
        if int(progress) % 10 == 0:
            print(f"Progress: {progress:.1f}% (Time elapsed: {elapsed:.1f} seconds)")
        
        arrival_interval = generate_arrival_interval(MEAN_ARRIVAL_TIME)
        time.sleep(arrival_interval)
        
        task = create_task(task_id, MEAN_SERVICE_TIME)
        task_queue.put(task)
        queue_size += 1
        task_id += 1
        
        queue_lengths.append(queue_size)

    print("\nWaiting for remaining tasks to complete...")
    time.sleep(MEAN_SERVICE_TIME) 
    
    for p in processes:
        p.terminate()
        p.join()

    waiting_times, delay_times = process_results(results_queue)
    stats = calculate_statistics(waiting_times, delay_times, queue_lengths)
    
    print(f"\nProcessed {len(waiting_times)} tasks")
    
    write_results_to_file(queue_lengths, waiting_times, delay_times)
    
    return stats

if __name__ == '__main__':
    stats = run_simulation()