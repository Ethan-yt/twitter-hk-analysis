#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time : 2019-10-23 15:20
# @Author : Ethan
# @Email : yantan@bit.edu.cn
# @File : data_loader
import logging
import os

from transformers import DataProcessor, InputExample

logger = logging.getLogger(__name__)


class CLSProcessor(DataProcessor):
    """Processor for the MRPC data set (GLUE version)."""

    def get_example_from_tensor_dict(self, tensor_dict):
        """See base class."""
        return InputExample(tensor_dict['idx'].numpy(),
                            tensor_dict['sentence1'].numpy().decode('utf-8'),
                            tensor_dict['sentence2'].numpy().decode('utf-8'),
                            str(tensor_dict['label'].numpy()))

    def get_train_examples(self, file_path):
        """See base class."""
        logger.info("LOOKING AT {}".format(file_path))
        return self._create_examples(
            self._read_tsv(file_path), "train")

    def get_dev_examples(self, file_path):
        """See base class."""
        logger.info("LOOKING AT {}".format(file_path))
        return self._create_examples(
            self._read_tsv(file_path), "dev")

    def get_pred_examples(self, file_path):
        """See base class."""
        logger.info("LOOKING AT {}".format(file_path))
        return self._create_examples(
            self._read_tsv(file_path), "pred")

    def get_labels(self):
        """See base class."""
        return ["0", "1"]

    def _create_examples(self, lines, set_type):
        """Creates examples for the training and dev sets."""
        examples = []
        for (i, line) in enumerate(lines):
            guid = "%s-%s" % (set_type, i)
            text_a = line[1]
            label = line[0]
            if set_type == 'pred':
                label = '0'
                guid = line[0]
            examples.append(InputExample(guid=guid, text_a=text_a, label=label))
        return examples


class IEProcessor(CLSProcessor):
    def get_labels(self):
        """See base class."""
        return ["I", "E"]


class NSProcessor(CLSProcessor):
    def get_labels(self):
        """See base class."""
        return ["N", "S"]


class PJProcessor(CLSProcessor):
    def get_labels(self):
        """See base class."""
        return ["P", "J"]


class TFProcessor(CLSProcessor):
    def get_labels(self):
        """See base class."""
        return ["T", "F"]
