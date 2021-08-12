# SimCLR
Contrastive learning for ophthalmology images

### Evaluation

The feature quality is evaluated by the means of:

- a linear classifier (logistic regression) trained on the extracted features of the encoder.
- a fine-tuned classifier, based on a SimCLR model with the last 4 layers (3 convolutional layers + max_pool) trained for 5 epochs.
- a t-SNE visualization.

<!-- These evaluations are performed for 3 fractions of the training data: 100%, 20%, and 5%.
 -->
### Results

The table below lists the top-1 accuracy for all cases. It can be seen that SimCLR improves the classification performance for all fractions of the training set. One can consequently conclude that the feature encoding of the base_model clearly improves thanks to the SimCLR framework.

<p align="center">
 
 <table>
  <thead>
    <tr>
      <th>Fraction of training set</th>
      <th colspan="2">ImageNet (EfficientNet)</th>
      <th colspan="2">FundusNet (SimCLR w/ VGG-16 backbone)</th>
    </tr>
  </thead>
  <tbody>
   <tr>
      <td></td>
    <td>Stylized</td>
    <td>Not stylized</td>
    <td>Stylized</td>
    <td>Not stylized</td>
  </tr>
   <tr>
    <td>100%</td>
    <td>0.7450</td>
    <td>0.7869</td>
    <td></td>
    <td>0.7358</td>
   </tr>
   <tr>
    <td>80%</td>
    <td>0.7427</td>
    <td>0.8075</td>
    <td></td>
    <td>0.7360</td>
   </tr>
   <tr>
    <td>60%</td>
    <td>0.7394</td>
    <td>0.7472</td>
    <td></td>
    <td>0.7369</td>
   </tr>
   <tr>
    <td>40%</td>
    <td>0.7373</td>
    <td>0.7318</td>
    <td></td>
    <td>0.7356</td>
   </tr>
   <tr>
    <td>20%</td>
    <td></td>
    <td>0.7328</td>
    <td></td>
    <td>0.7360</td>
   </tr>
    
  </tbody>
</table>

| <img src=/img/t-SNE_VGG16.png alt="alt text" width="250"/> | <img src=/img/t-SNE_SimCLR.png alt="alt text" width="250"/> |
| :--------------------------------------------------------: | :---------------------------------------------------------: |
|     t-SNE of VGG16-features before SimCLR       |      t-SNE of VGG16-features after SimCLR        |
