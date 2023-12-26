import tensorflow as tf
from keras.models import load_model
from PIL import Image
import numpy as np

# Load the trained model (replace 'my_model.h5' with your model file)
model = load_model('my_model.keras')

# Load your image
image_path = 'my_digit.png'
image = Image.open(image_path).convert('L') # Convert to grayscale
image = image.resize((28, 28)) # Resize to 28x28

# Preprocess the image
image_array = np.array(image)
image_array = image_array.astype('float32') / 255
image_array = image_array.reshape(1, 28, 28, 1)

# Predict
prediction = model.predict(image_array)

# Interpret the output
digit = np.argmax(prediction)

print(f"The model predicts this digit as: {digit}")