#!/bin/bash
python3 A3C_FF_LSTM.py Pong-ram-v0 -a configs/vpg.json -n configs/mlp2_lstm_network.json -e 50000 -m 2000 -W 3
