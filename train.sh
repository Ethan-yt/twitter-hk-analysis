#!/usr/bin/env bash

export CUDA_VISIBLE_DEVICES='0,1,4,6'

python run_cls.py \
--model_type bert \
--task_name cb \
--model_name_or_path models/cb \
--do_train \
--do_lower_case \
--data_dir data/cyberbullying \
--max_seq_length 128 \
--per_gpu_eval_batch_size 16 \
--per_gpu_train_batch_size 8 \
--learning_rate 2e-5 \
--output_dir output \
--evaluate_during_training \
--logging_steps 50 \
--overwrite_output_dir \
--num_train_epochs 5
