# Binary Image Classifier

A web application that automatically distinguishes between a **photograph** and a **signature** from two uploaded images, using a trained Convolutional Neural Network (CNN). Instead of requiring the user to label which image is which, the app identifies them itself and displays each one correctly tagged.

## Overview

This project demonstrates a simple end-to-end binary image classification pipeline:

- A CNN model is trained to distinguish between two classes of images — photographs and signatures.
- A Flask web interface allows a user to upload two images at once.
- The backend runs both images through the trained model, determines which one is the photo and which is the signature (even if uploaded in the wrong order), and displays the corrected result.

## How It Works

1. **Upload** — The user selects and uploads two image files through the web form.
2. **Preprocessing** — Each image is resized to 200x200 pixels and converted into the numerical format the model expects.
3. **Prediction** — The CNN model (`res.json` for architecture, `res.h5` for trained weights) predicts the class of each image.
4. **Correction & Display** — If both images were uploaded in the expected order, they're shown as-is. If they were swapped, the app automatically detects this and displays them in the correct order — photo labeled as photo, signature labeled as signature.

## Model

| Detail | Description |
|---|---|
| Type | Convolutional Neural Network (CNN) |
| Input size | 200 x 200 x 3 (RGB images) |
| Output classes | 2 (Photograph, Signature) |
| Architecture file | `res.json` |
| Trained weights | `res.h5` |
| Framework | TensorFlow / Keras |

## Tech Stack

- **Backend:** Python, Flask
- **Machine Learning:** TensorFlow, Keras
- **Image Processing:** OpenCV, Pillow (PIL)
- **Frontend:** HTML, Jinja2 templates


## Features

- Accepts two image uploads at once (PNG, JPG, JPEG)
- Automatically identifies which image is the photo and which is the signature
- Self-corrects the order if the images were uploaded swapped
- Clean, minimal web interface for uploading and viewing results

## Possible Improvements

- Add validation/feedback when an unsupported file type is uploaded
- Improve UI styling and responsiveness
- Add a confidence score alongside each prediction
- Deploy as a publicly accessible web service
