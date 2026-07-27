import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

print("Model file loaded")

model = None   # global model

# ✅ Define load_model function
def load_model():
    global model
    if model is None:
        print("Loading MobileNetV2...")
        model = MobileNetV2(weights='imagenet')

# ✅ Food filter (optional but useful)
FOOD_KEYWORDS = [
    "apple", "banana", "orange", "pizza", "burger",
    "milk", "egg", "bread", "cheese", "tomato"
]

def detect_items(img_path):
    load_model()   # ✅ now this works

    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    preds = model.predict(img_array)
    decoded = decode_predictions(preds, top=5)[0]

    items = [item[1] for item in decoded]

    # ✅ Filter food items
    food_items = [i for i in items if i in FOOD_KEYWORDS]

    return food_items if food_items else items