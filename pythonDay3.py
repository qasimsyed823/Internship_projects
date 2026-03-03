"""Write two decorators: @timer that measures and prints execution time of
   any function, and @retry(n) that automatically retries a function on failure 
   up to n times."""

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()          
        result = func(*args, **kwargs)    
        end_time = time.time()            
        
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

def retry(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            
            while attempts < n:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed: {e}")
            
            print("All retry attempts failed.")
        return wrapper
    return decorator



@timer
@retry(3)
def test_function():
    print("Running function...")
    time.sleep(1)
    raise ValueError("Error occurred!")


test_function()

#---------------------------------------------------------------------------------------

"""Write a log file parser using regex: extract timestamps, error levels, and messages.
   Group all errors by type and export the summary as a JSON report file."""
import re
import json


# Regex pattern
LOG_PATTERN = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)"


def parse_log_file(filename):
    log_data = {}

    with open(filename, "r") as file:
        for line in file:
            match = re.match(LOG_PATTERN, line)

            if match:
                timestamp, level, message = match.groups()

                
                if level not in log_data:
                    log_data[level] = {
                        "count": 0,
                        "messages": []
                    }

                log_data[level]["count"] += 1
                log_data[level]["messages"].append({
                    "timestamp": timestamp,
                    "message": message
                })

    return log_data


def export_to_json(data, output_file):
    with open(output_file, "w") as json_file:
        json.dump(data, json_file, indent=4)


def main():
    logs = parse_log_file("log.txt")
    export_to_json(logs, "report.json")
    print("JSON report generated successfully!")


if __name__ == "__main__":
    main()




