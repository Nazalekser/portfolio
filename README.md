# Data Science Portfolio

A repository of projects and challenges I have worked on or am currently working on.

Click on the project name to see the analysis and code or to Brief Project Description link to see a brief description of the project.

## Projects:

### [Flower Classification with TPUs (one model)](https://github.com/Nazalekser/portfolio/blob/main/Projects/Flower%20Classification%20with%20TPUs/flower-classification-with-tpus-one-model.ipynb)
### [Flower Classification with TPUs (ensemble)](https://github.com/Nazalekser/portfolio/blob/main/Projects/Flower%20Classification%20with%20TPUs/flower-classification-with-tpus-ensemble.ipynb)

   <img src="https://github.com/Nazalekser/portfolio/blob/main/Projects/Flower Classification with TPUs/images/flowers.jpg" width="500">

The task is to identify the type of flowers in a dataset of images
    
Steps:
* Create the distribution strategy to train with TPU
* Load the data in .tfrec format, decode images, read labled and unlabeled data
* Define augmengation strategy (random erasing, random flip left and right)
* Define learing rate shedule (linear increase + exponential decay)
* Choose base model (EfficientNet, DenseNet, Xception)
* Evaluate predictions
* Ensemble models

[Brief Project Description](https://github.com/Nazalekser/portfolio/blob/main/Projects/Flower%20Classification%20with%20TPUs/Readme.md)
   
---

### [Winning Space Race](https://docs.google.com/presentation/d/1DRCCmKFTf5TxLaYAUW6bv3_el0f9WQzFUWUNY41vrP0/edit?usp=drive_link)
   
  <img src="https://github.com/Nazalekser/portfolio/blob/main/Projects/Winning%20Space%20Race/My%20presentation.jpg" width="500">

The task is to make recommendations to Space Y, a company that wants to compete with Space X. The presentation file contains all the necessary references with code and analysis.

Steps:
* Data collection using SpaceX REST API and Web Scraping
* Clean up and convert the data into a format that can be summarized in the final data
* EDA with Data Visualization and SQL
* Interactive visual analytics using Folium and Plotly Dash
* Perform predictive analysis using classification models

[Brief Project Description](https://github.com/Nazalekser/portfolio/blob/main/Projects/Winning%20Space%20Race/Readme.md)

---

### [Deep Q-Learning - Lunar Lander](https://github.com/Nazalekser/portfolio/blob/main/Projects/Luna_Lander_Project/Lunar_Lander.ipynb)

   <img src="https://github.com/Nazalekser/portfolio/blob/main/Projects/Luna_Lander_Project/videos/lunar_lander.gif" width="500">

The task is to land the lander safely on the landing pad using OpenAI's Gym Library

* We use the standard “agent-environment loop” formalism.
* The agent has 4 discrete actions available and its observation space consists of a state vector with 8 variables.
* The total reward of an episode is the sum of the rewards for all the steps within that episode.
* The project uses a Target Network (with soft update weights) and Experience Replay techniques to avoid instabilities.

[Brief Project Description](https://github.com/Nazalekser/portfolio/blob/main/Projects/Luna_Lander_Project/Readme.md)

---

### [Neural Translation Model](https://github.com/Nazalekser/portfolio/blob/main/Projects/Neural%20translation%20model/2_5_Capstone_Project.ipynb)

   <img src="https://github.com/Nazalekser/portfolio/blob/main/Projects/Neural%20translation%20model/neural_translation_model_and_key.jpg" width="500">

The task is to develop a neural translation model from English to German

Steps:
* Text preprocessing - use character filters, tokenizing sentenses
* Prepare the data - splite the data at val and train sets, split at sentences, use tf.data.Dataset object and  pre-trained English word embedding module from TensorFlow Hub. Cutting off, padding, batching datasets.
* Create the end token custom layer to add the learned end token embedding to the encoder model using layer subclassing.
* Build the RNN encoder model: end token + masking  + LSTM layer
* Make a custom training loop to train custom neural translation model with the function than computes the forward and backward pass. Decorate the function
* Use the model to translate

[Brief Project Description](https://github.com/Nazalekser/portfolio/blob/main/Projects/Neural%20translation%20model/Readme.md)

---

## [Python Challenges](https://github.com/Nazalekser/portfolio/tree/main/Python)

Here is my work with python challenges from HackerRank.

---
