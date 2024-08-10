import threading  # Importing the threading module
import time  # Importing the time module

# Define a function that simulates a long-running task
def long_running_task():
    print(f"{threading.current_thread().getName()} started")  # Print a message indicating the thread has started
    time.sleep(2)  # Simulate a long-running task by sleeping for 2 seconds
    print(f"{threading.current_thread().getName()} completed")  # Print a message indicating the thread has completed

threads = []  # Initialize an empty list to hold the thread objects

# Create and start 5 threads
for i in range(5):
    thread = threading.Thread(target=long_running_task, name=f"Thread-{i}")  # Create a new Thread object, targeting the long_running_task function and naming the thread
    threads.append(thread)  # Append the thread to the threads list
    thread.start()  # Start the thread

# Wait for all threads to complete and check if they are alive
for thread in threads:
    thread.join()  # Block until the thread completes
    print(f"Is {thread.getName()} alive? {thread.is_alive()}")  # Print whether the thread is alive or not after joining
