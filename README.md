# SimCLR
Contrastive learning for ophthalmology images

### Evaluation

The feature quality is evaluated by the means of:

- a linear classifier (logistic regression) trained on the extracted features of the encoder.
- a fine-tuned classifier, based on a SimCLR model with the last 4 layers (3 convolutional layers + max_pool) trained for 5 epochs.
- a t-SNE visualization.

These evaluations are performed for 3 fractions of the training data: 100%, 20%, and 5%.

### Results

The table below lists the top-1 accuracy for all cases. It can be seen that SimCLR improves the classification performance for all fractions of the training set on both the linear and fine-tuned classifier.

One can consequently conclude that the feature encoding of the base_model clearly improves thanks to the SimCLR framework.

<p align="center">

| Fraction of training set | Classifier |    VGG16    |   SimCLR    |
| :----------------------: | :--------: | :---------: | :---------: |
|           100%           |   Linear   | 0.79 ± 0.00 | 0.82 ± 0.01 |
|                          | Fine-tuned | 0.85 ± 0.01 | 0.87 ± 0.01 |
|           20%            |   Linear   | 0.70 ± 0.00 | 0.81 ±0.02  |
|                          | Fine-tuned | 0.83 ± 0.01 | 0.86 ± 0.01 |
|            5%            |   Linear   | 0.63 ± 0.00 | 0.80 ± 0.02 |
|                          | Fine-tuned | 0.80 ± 0.02 | 0.84 ± 0.03 |

| <img src=/img/t-SNE_VGG16.png alt="alt text" width="250"/> | <img src=/img/t-SNE_SimCLR.png alt="alt text" width="250"/> |
| :--------------------------------------------------------: | :---------------------------------------------------------: |
|     t-SNE of VGG16-features before SimCLR       |      t-SNE of VGG16-features after SimCLR        |
