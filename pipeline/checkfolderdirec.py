import os
from icecream import ic
    
    
project_root = os.path.dirname(os.path.abspath(__file__))
data_folder = os.path.join(project_root, 'data')
checkpoint_folder = os.path.join(project_root, 'checkpoint')
lora_folder = os.path.join(project_root, 'lora')

ic(project_root)
ic(data_folder)
ic(checkpoint_folder)
ic(lora_folder)