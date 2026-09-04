import schedule
import time
from datetime import datetime


def automated_task():
    try:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("task_log.txt", "a") as file:
            file.write(f"Task executed successfully at {current_time}\n")

        print(f"Task executed successfully at {current_time}")

    except Exception as error:
        print(f"Error while running task: {error}")


# Run the task every 1 minute
schedule.every(1).minutes.do(automated_task)

print("Automation started...")
print("Task will run every 1 minute.")

while True:
    schedule.run_pending()
    time.sleep(1)