## Dataset Description
In this Kaggle competition we're classifying 104 types of flowers based on their images drawn from five different public datasets. Some classes are very narrow, containing only a particular sub-type of flower (e.g. pink primroses) while other classes contain many sub-types (e.g. wild roses).

This competition is different in that images are provided in TFRecord format. The TFRecord format is a container format frequently used in Tensorflow to group and shard data data files for optimal training performace.
Each file contains the id, label (the class of the sample, for training data) and img (the actual pixels in array form) information for many images. 

## Tensor Processing Units (TPUs)
TPUs are powerful hardware accelerators specialized in deep learning tasks. They were developed (and first used) by Google to process large image databases, such as extracting all the text from Street View.

  <img src="https://storage.googleapis.com/kaggle-media/tpu/tpu_cores_and_chips.png" width="500">
