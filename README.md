# CS 583 Programming Assignment #2

**Student:** Xiangyu Zeng

This repository contains the completed CIFAR-10 CNN assignment with all code
and execution outputs.

## Submission file

- [Programming2_Xiangyu_Zeng.html](./Programming2_Xiangyu_Zeng.html)
- [Programming2_improved.ipynb](./Programming2_improved.ipynb)

## Improvements

- Six convolution layers arranged in three blocks
- Batch normalization between trainable layers and activations
- Dropout and L2 regularization
- Horizontal-flip and translation data augmentation
- Global average pooling
- Learning-rate reduction, early stopping, and checkpoint restoration
- Final fine-tuning on all 50,000 training samples
- Extended cosine-decay training with light label smoothing

## Results

| Split | Accuracy |
| --- | ---: |
| Training | 87.79% |
| Validation | 85.28% |
| Test | 84.58% |
