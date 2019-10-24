# Twitter HK Analysis

This repo contains dataset and code for the article: **Intrinsic or Situational? Can Internet Trolling Spread from Person to Person?
Examining the Impact of Personality and Network Attributes on Trolling Behavior**

## Task 1

Intent identification: whether there is a cyber bullying.

## Task 2

Analysis of Myers-Briggs Type Indicator in four dimensions.

The Myers–Briggs Type Indicator (MBTI) is an introspective self-report questionnaire indicating differing psychological preferences in how people perceive the world and make decisions.



# Project Structure
```
.
|-- data
|   |-- cyberbullying               # cyber bullying dataset (task 1)
|   |   |-- predict.txt
|   |   |-- test.txt
|   |   `-- train.txt
|   |-- personality                 # personality dataset (task 2)
|   |   |-- personality_ie.test
|   |   |-- personality_ie.train
|   |   |-- personality_ns.test
|   |   |-- personality_ns.train
|   |   |-- personality_pj.test
|   |   |-- personality_pj.train
|   |   |-- personality_tf.test
|   |   |-- personality_tf.train
|   |   |-- predict.txt
|   |   `-- train-raw.csv
|   `-- stat.py
|-- data_loader.py
|-- utils
|   |-- get_metrics.py
|   `-- stat.py
|-- models
|   |-- bert-large-uncased-whole-word-masking # put pretrained model here
|   |   |-- config.json
|   |   |-- pytorch_model.bin
|   |   `-- vocab.txt
|-- predict.sh
|-- readme.md
|-- run_cls.py
`-- train.sh 
```


## Cyberbullying

### Model

We use BERT as a text classifier. The codes were modified from [Transformers](https://github.com/huggingface/transformers). Specifically, we use `bert-large-uncased-whole-word-masking`.

### Data Size

| DataSet | Positive | Negative | Total| Avg Len|
| :------:| :------:  | :------:  |:---:|:---:|
|Train|6293|9707|16000|12.56|
|Validation|1529|2472|4001|12.28|
|Predict| -| -|17324|22.11|

### Result on Validation Set

|Acc|Precision|Recall|F1|
|:---:|:---:|:---:|:---:|
|0.8957760559860035|0.8270588235294117|0.9195552648790059|0.8708578507277794|

### Training 

Before training the model, download `bert-large-uncased-whole-word-masking` from [https://github.com/google-research/bert](https://github.com/google-research/bert)



```bash
python run_cls.py \
--model_type bert \
--task_name cb \
--model_name_or_path models/bert-large-uncased-whole-word-masking \
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
```

### Predict

```bash
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
```


## Personality

### Model

Due to the long length of the input text, we use [fastText](https://github.com/facebookresearch/fastText) rather than BERT.


### Data size

total train examples: 6000

I: 4603, E: 1398

S: 811, N: 5190

P: 3620, J: 2381

T: 2742, F: 3259



|Dataset|Num|Avg len|
|:----:|:----:|:----:|
|Train|6000|1267.15|
|Validation|2674|1256.58|
|Predict|5573|557.65|



### Result on Validation Set

|Personality|Acc|P|R|F1|
|:---:|:---:|:---:|:---:|:---:|
|IE|0.8309648466716529|0.8386287625418061|0.9681467181467182|0.8987455197132618|
|NS|0.8620044876589379|0.8635846911708981|0.9960664335664335|0.9251065557134159|
|PJ|0.7857142857142857|0.7979510529311327|0.8654320987654321|0.83032277169085|
|TF|0.8369483919222139|0.8428277282086479|0.8557491289198607|0.8492392807745505|


### Train

```bash
./fasttext supervised -input personality_ie.train -output model_personality_ie -epoch 20
```

### Test

```bash
awk '!($1="")' personality_ie.test | ./fasttext predict model_personality_ie.bin - > result_ie.txt
python ./utils/get_metrics.py
```

### Predict

```bash
awk '!($1="")' predict.txt | ./fasttext predict model_personality_ie.bin - > pred_ie.txt
```
