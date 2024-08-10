import asyncio  # Importing the asyncio module for asynchronous programming
import time  # Importing the time module

# Define an asynchronous function that simulates a long-running task
async def long_running_task():
    print("Task started")  # Print a message indicating the task has started
    await asyncio.sleep(2)  # Simulate a long-running task with an asynchronous sleep
    print("Task completed")  # Print a message indicating the task has completed

# Run the coroutine multiple times sequentially
async def run_sequential_tasks():
    start_time = time.time()  # Record the start time
    for _ in range(5):
        await long_running_task()  # Run the coroutine sequentially
    end_time = time.time()  # Record the end time
    print(f"Total time taken (sequential): {end_time - start_time} seconds")  # Print the total time taken for sequential execution

# Run the coroutine multiple times concurrently
async def run_concurrent_tasks():
    start_time = time.time()  # Record the start time
    await asyncio.gather(*[long_running_task() for _ in range(5)])  # Run the coroutine concurrently
    end_time = time.time()  # Record the end time
    print(f"Total time taken (concurrent): {end_time - start_time} seconds")  # Print the total time taken for concurrent execution

# Run the sequential tasks
print("Running tasks sequentially:")
asyncio.run(run_sequential_tasks())  # Use asyncio.run to run the sequential tasks

# Run the concurrent tasks
print("\nRunning tasks concurrently:")
asyncio.run(run_concurrent_tasks())  # Use asyncio.run to run the concurrent tasks
