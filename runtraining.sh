#!/bin/bash

echo "test run"
accelerate launch sdxl_train_network.py --config_file config_lora-db.toml