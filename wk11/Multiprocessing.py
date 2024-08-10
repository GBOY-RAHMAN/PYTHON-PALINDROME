from multiprocessing import Process  # Importing the Process class from the multiprocessing module
import time  # Importing the time module

# Define a function that simulates a long-running task
def long_running_task():
    print("Task started")  # Print a message indicating the task has started
    time.sleep(2)  # Simulate a long-running task by sleeping for 2 seconds
    print("Task completed")  # Print a message indicating the task has completed

if __name__ == '__main__':
    start_time = time.time()  # Record the start time
    processes = []  # Initialize an empty list to hold the process objects

    # Create and start 5 processes
    for _ in range(5):
        process = Process(target=long_running_task)  # Create a new Process object, targeting the long_running_task function
        processes.append(process)  # Append the process to the processes list
        process.start()  # Start the process

    # Wait for all processes to complete
    for process in processes:
        process.join()  # Block until the process completes

    end_time = time.time()  # Record the end time
    print(f"Total time taken (multiprocessing): {end_time - start_time} seconds")  # Print the total time taken
