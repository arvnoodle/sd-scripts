import gradio as gr
import toml
import subprocess
import os
from icecream import ic
# Paths to the TOML file and the script
TOML_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'config_lora-db.toml')
SCRIPT_PATH = os.path.join(os.path.dirname(__file__), '..', 'run_training.sh')
ic(TOML_FILE_PATH)
ic(SCRIPT_PATH)

def update_toml(train_data_dir, output_dir, output_name):
    # Load the TOML file
    with open(TOML_FILE_PATH, 'r') as file:
        config = toml.load(file)
    
    # Update the fields
    config['train_data_dir'] = train_data_dir
    config['output_dir'] = output_dir
    config['output_name'] = output_name
    
    # Save the updated TOML file
    with open(TOML_FILE_PATH, 'w') as file:
        toml.dump(config, file)
    
    return "TOML file updated successfully!"

def start_training(train_data_dir, output_dir, output_name):
    # Update the TOML file
    update_message = update_toml(train_data_dir, output_dir, output_name)
    
    # Run the training script
    try:
        result = subprocess.run(['bash', SCRIPT_PATH], capture_output=True, text=True)
        if result.returncode == 0:
            return f"{update_message}\nTraining started successfully!\n\n{result.stdout}"
        else:
            return f"{update_message}\nError during training:\n\n{result.stderr}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Create Gradio interface
app = gr.Interface(
    fn=start_training,  # This will update TOML and start training
    inputs=[
        gr.Textbox(label="Train Data Directory", placeholder="Enter new train_data_dir"),
        gr.Textbox(label="Output Directory", placeholder="Enter new output_dir"),
        gr.Textbox(label="Output Name", placeholder="Enter new output_name")
    ],
    outputs="text",
    title="TOML Parameter Editor and Training Launcher",
    description="Adjust the parameters of your TOML file and start training."
)