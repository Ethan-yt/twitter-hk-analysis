#!/usr/bin/env bash

export CUDA_VISIBLE_DEVICES='0'

python run_cls.py \
--model_type bert \
--task_name cb \
--model_name_or_path models/cb/checkpoint-1450 \
--do_predict \
--do_lower_case \
--data_dir data/cyberbullying \
--dev_path predict.txt \
--max_seq_length 128 \
--per_gpu_eval_batch_size 512 \
--learning_rate 2e-5 \
--output_dir models/cb/checkpoint-1450
