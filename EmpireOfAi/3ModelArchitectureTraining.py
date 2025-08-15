"""
Transformer Model (deep learning architecture)

Attention Mechanism: Helps the model focus on relevant parts of the input sequence.
Self-Attention: Allows each token to attend to every other token in the sequence.
Feedforward Layers: Applies transformations to each token independently after attention.
Layer Normalization: Stabilizes training and improves convergence.

Libraries
TensorFlow: Offers built-in layers for transformers.
PyTorch: Flexible framework for implementing custom architectures.
"""
import tensorflow as tf
from keras.layers import Input, Dense, LayerNormalization, MultiHeadAttention

# Define a single transformer block
def transformer_block(input, num_heads, key_dim):
    # Step 1: Multi-head attention -  computes self-attention for multiple heads
    attention = MultiHeadAttention(num_heads=num_heads, key_dim=key_dim)(input, input)
    # Step 2: Add & Normalize - Residual connection added to attention output and normalized with LayerNormalization.
    attention = LayerNormalization()(attention + input)
    # Step 3: Feedforward network - Dense layer with ReLU activation processes each token independently.
    # ReLU Activation (Rectified Linear Unit): ReLU is a non-linear activation function applied element-wise to the output of the dense layer.
    dense = Dense(128, activation='relu')(attention)
    # Step 4: Add & Normalize
    output = LayerNormalization()(dense + attention)
    return output

# Input layer - Accepts a sequence of features (shape=(None, 128)).
input_layer = Input(shape=(None, 128))  # Sequence length is variable, feature size is 128

# Transformer block
transformer_output = transformer_block(input_layer, num_heads=8, key_dim=64)
# Model definition
model = tf.keras.Model(inputs=input_layer, outputs=transformer_output)

# Model summary - residual connection added again, followed by normalization
model.summary()