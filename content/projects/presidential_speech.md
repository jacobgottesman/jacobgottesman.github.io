title: Classifying Presidential Speech Snippets by President
date: 2024-06-10
order: 6
description: A natural language processing project comparing neural network architectures to identify which U.S. president delivered a speech based on short text samples.
image: president-speech.jpg
github_url: https://github.com/jacobgottesman/president_speech_classifier
paper_url: https://drive.google.com/file/d/1ZGHxfKTCquKv1m3ckqAnyYl4X8y8zWQS/view?usp=sharing
tags: [Natural Language Processing, Neural Networks, Text Classification, Python, TensorFlow, LSTM, Transformers]
technologies: [Python, TensorFlow, NLTK, Word2Vec, Neural Networks, LSTM, Transformers]


## Project Overview

This project applies advanced natural language processing techniques to identify which U.S. president delivered a speech based on short text samples (16-word snippets). By implementing and comparing three different neural network architectures, our research demonstrates how machine learning can detect subtle linguistic patterns unique to each president's speaking style.

## The Challenge

Presidential speeches contain distinctive linguistic fingerprints influenced by:
- Personal speaking style, vocabulary choices, and rhetorical patterns
- Historical context and political environment of their era
- The evolution of political discourse across American history
- Subtle patterns that may transcend party lines or time periods

Our challenge was to determine if these patterns are distinctive enough for accurate classification across 43 presidents spanning over two centuries of American history, and to identify which neural network architecture best captures these subtle differences.

## Data Collection and Preparation

Our dataset consists of:
- Over 1,000 presidential speeches from the Miller Center at the University of Virginia
- More than 4.6 million tokens across 182,084 sentences
- 16-word sequence extraction to create training examples
- Word2Vec embeddings to capture semantic relationships
- Minimal preprocessing (case folding and tokenization) to preserve authentic speech patterns
- A minimum threshold of 10,000 tokens per president to ensure sufficient training data

## Neural Network Architectures

### Feed-Forward Neural Network
- Input layer accepting 800-dimension vectors (16 words × 50-dimension embeddings)
- Single hidden layer with 1,000 units
- Classification layer with 43 outputs corresponding to different presidents
- Achieved 18.9% accuracy on the test set

### Long Short-Term Memory Network (LSTM)
- Specialized architecture designed for sequential data
- 400 hidden units capturing temporal dependencies in speech patterns
- Direct processing of the 2D input of shape (16, 50)
- Our best-performing model with 52.8% accuracy on the test set

### Transformer Model
- Encoder architecture with 8 self-attention heads
- 1,000 hidden units with pooling layer
- Sophisticated contextual understanding through attention mechanisms
- Achieved 40.1% accuracy on the test set

## Results and Analysis

Our models demonstrated impressive performance considering the complexity of classifying among 43 different presidents:

- **LSTM Network**: Achieved the highest accuracy at 52.8%, with strong precision (52.4%) and recall (52.8%)
- **Transformer Model**: Reached 40.1% accuracy with balanced precision and recall
- **Feed-Forward Network**: Baseline performance of 18.9% accuracy

Analysis of classification patterns revealed fascinating insights:
- Donald Trump showed the most distinctive speaking style, with highest precision and recall across models
- Presidents from similar historical eras were often confused with each other
- Some presidents with limited training data (like Millard Fillmore and Zachary Taylor) were harder to classify
- Political party affiliation appeared less important than historical era in determining speaking style

## Interactive Examples and Applications

Our project demonstrates potential applications in:
- Historical research and political science analysis
- Authorship attribution and linguistic fingerprinting
- Understanding the evolution of political discourse over time
- Exploring similarities and differences across political eras

## Future Work

Potential extensions of this research include:
- Implementing pre-trained language models like BERT to enhance performance
- Expanding the architecture with additional layers and tuning hyperparameters
- Analyzing the relationship between party affiliation and classification accuracy
- Investigating what specific linguistic features drive confusion between presidents
- Exploring broader questions about how political discourse has evolved across American history

This project represents a successful application of cutting-edge NLP techniques to a challenging multi-class classification problem, revealing insights into the linguistic patterns that define presidential communication over two centuries.