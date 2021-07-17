# SimCLR
Contrastive learning for ophthalmology images

### Evaluation

The feature quality is evaluated by the means of:

- a linear classifier (logistic regression) trained on the extracted features of the encoder.
- a fine-tuned classifier, based on a SimCLR model with the last 4 layers (3 convolutional layers + max_pool) trained for 5 epochs.
- a t-SNE visualization.

These evaluations are performed for 3 fractions of the training data: 100%, 20%, and 5%.

### Results

The table below lists the top-1 accuracy for all cases. It can be seen that SimCLR improves the classification performance for all fractions of the training set. One can consequently conclude that the feature encoding of the base_model clearly improves thanks to the SimCLR framework.

<p align="center">

| Fraction of training set  |    ImageNet (VGG-19)           |   FundusNet (SimCLR w/ VGG-16 backbone)    |
| :----------------------:  | :---------:                    | :---------: |
|           100%            | 0.79 ± 0.00                    | 0.82 ± 0.01 |
|           20%             | 0.70 ± 0.00                    | 0.81 ±0.02  |
|            5%             | 0.63 ± 0.00                    | 0.80 ± 0.02 |

| <img src=/img/t-SNE_VGG16.png alt="alt text" width="250"/> | <img src=/img/t-SNE_SimCLR.png alt="alt text" width="250"/> |
| :--------------------------------------------------------: | :---------------------------------------------------------: |
|     t-SNE of VGG16-features before SimCLR       |      t-SNE of VGG16-features after SimCLR        |
