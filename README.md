# EECE570-Final-Project
code for EECE570 Final Report "Improving Fairness in Image Classification via Sketching Style Combination"

Ruichen Yao

84951482


## Overall Pipeline
![avatar](./img/method.png)
I convert the original input images into sketch style combined images instead of sketch images with only one style. Then I feed sketch style combined images to the following classification model for prediction. To further fairness improvement, I introduce a fairness loss function to mitigate the bias in the model.

## Sketching Method

For sketch generation model $S$, we employ the latest image-to-sketching method [Quality Metric Guided Portrait Line Drawing Generation From Unpaired Training Data
](https://ieeexplore.ieee.org/document/9699090) to convert input image $x_i$ into its corresponding sketch $S(x_i)$.

The code are available [here](https://github.com/yiranran/QMUPD).
