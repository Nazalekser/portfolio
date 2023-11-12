## Dataset Description
In this Kaggle competition we're classifying 104 types of flowers based on their images drawn from five different public datasets. Some classes are very narrow, containing only a particular sub-type of flower (e.g. pink primroses) while other classes contain many sub-types (e.g. wild roses).

This competition is different in that images are provided in TFRecord format. The TFRecord format is a container format frequently used in Tensorflow to group and shard data data files for optimal training performace.
Each file contains the id, label (the class of the sample, for training data) and img (the actual pixels in array form) information for many images. 
