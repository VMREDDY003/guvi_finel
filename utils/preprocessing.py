# utils/preprocessing.py

import tensorflow as tf

IMG_SIZE = (224, 224)

def load_and_prepare_image(image_path):
    """
    Loads an image file, resizes it to IMG_SIZE, and normalizes pixel values.

    Args:
        image_path (str): Path to the image file.

    Returns:
        tf.Tensor: Preprocessed image tensor ready for model prediction with shape (1, 224, 224, 3).
    """
    img = tf.io.read_file(image_path)
    img = tf.image.decode_jpeg(img, channels=3)  # Ensure 3 channels RGB
    img = tf.image.resize(img, IMG_SIZE)
    img = img / 255.0  # Normalize to [0,1]
    img = tf.expand_dims(img, axis=0)  # Add batch dimension
    return img
