## Dataset Description
In this Kaggle competition we're classifying 104 types of flowers based on their images drawn from five different public datasets. Some classes are very narrow, containing only a particular sub-type of flower (e.g. pink primroses) while other classes contain many sub-types (e.g. wild roses).

This competition is different in that images are provided in TFRecord format. The TFRecord format is a container format frequently used in Tensorflow to group and shard data data files for optimal training performace.
Each file contains the id, label (the class of the sample, for training data) and img (the actual pixels in array form) information for many images. 

## Tensor Processing Units (TPUs)
TPUs are powerful hardware accelerators specialized in deep learning tasks. They were developed (and first used) by Google to process large image databases, such as extracting all the text from Street View.

  <img src="https://storage.googleapis.com/kaggle-media/tpu/tpu_cores_and_chips.png" width="500">
At approximately 20 inches (50 cm), a TPU v3-8 board is a fairly sizeable piece of hardware. It sports 4 dual-core TPU chips for a total of 8 TPU cores. Each TPU core has a traditional vector processing part (VPU) as well as dedicated matrix multiplication hardware capable of processing 128x128 matrices. This is the part that specifically accelerates machine learning workloads. TPUs are equipped with 128GB of high-speed memory allowing larger batches, larger models and also larger training inputs. 

TPUs are now available on Kaggle, for free. You can use up to 20 hours per week of TPUs and up to 9h at a time in a single session. 
