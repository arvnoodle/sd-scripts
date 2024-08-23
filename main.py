# main.py
from icecream import ic
ic.configureOutput(includeContext=True, prefix='DEV DEBUG: ')
import os
import subprocess
import time

import os
import subprocess

def run_gradio():
    # Import the Gradio app from the gradio_app folder
    from gradio_app import gradio_interface
    gradio_interface.app.launch()

def check_and_run_training():
    # Path to the run_training.sh script
    script_path = os.path.join(os.path.dirname(__file__), 'run_training.sh')
    
    if os.path.exists(script_path):
        try:
            result = subprocess.run(['bash', script_path], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"Training started successfully!\n\n{result.stdout}")
            else:
                print(f"Error during training:\n\n{result.stderr}")
        except Exception as e:
            print(f"An error occurred while running the training script: {str(e)}")
    else:
        print("Training script not found!")

def main():
    # Path to the gradio_app folder
    gradio_folder_path = os.path.join(os.path.dirname(__file__), 'gradio_app')
    
    # Check if the gradio_app folder exists
    if os.path.exists(gradio_folder_path):
        print("Gradio app detected. Launching the Gradio interface...")
        run_gradio()
    else:
        print("Gradio app folder not found.")
    
    # After Gradio is triggered, check for the run_training.sh script and run it
    check_and_run_training()

if __name__ == "__main__":
    main()
