import time
import sys

def loading_dots(message, dot_count=3, duration=3, interval=0.5):
    """
    Display a loading message with dots to indicate time passing.
    
    Args:
        message (str): The loading message to display.
        dot_count (int): The number of dots to display (default is 3).
        duration (float): The total time the loading animation should run.
        interval (float): The time interval between each dot's appearance.
    """
    # Calculate the total number of iterations based on duration and interval
    iterations = int(duration / interval)
    
    for i in range(iterations):
        # Calculate the current number of dots to display
        num_dots = (i % dot_count) + 1
        # Create the loading message with dots
        loading_message = f"{message}{'.' * num_dots}"
        # Print the loading message with carriage return to overwrite the line
        sys.stdout.write(f"\r{loading_message}")
        sys.stdout.flush()
        # Wait for the specified interval
        time.sleep(interval)
    # Print a newline after the loading animation is complete
    print()

