 Magic Wand Gesture Recognition using Edge Impulse
📌 Project Overview
This project demonstrates how to use an accelerometer sensor and Edge Impulse to recognize simple motion gestures—Up-Down and Left-Right—in real-time. Using a Nano BLE Sense board or a mobile phone, accelerometer data is collected and used to train a machine learning model capable of classifying these gestures.

🎯 Objective
Detect and classify gestures using accelerometer sensor data.

Train and deploy a machine learning model on an edge device.

Recognize Up-Down and Left-Right gestures with real-time inference.

🧰 Materials Required
Arduino Nano 33 BLE Sense board or compatible mobile device

USB Cable (for Nano BLE Sense)

Edge Impulse Account

Edge Impulse CLI (if using a development board)

Smartphone (optional, as a sensor)

🧠 Tools & Technologies
Edge Impulse

Arduino IDE (optional)

Python (optional for custom scripts)

BLE Sense / Mobile device accelerometer

🛠️ Setup Instructions
Step 1: Create Edge Impulse Account & Project
Sign up at Edge Impulse.

Create a new project (e.g., "Magic Wand Gestures").

Step 2: Connect Your Device
For Nano BLE Sense: Install Edge Impulse CLI and connect your board.

For Mobile: Install the Edge Impulse mobile app.

Step 3: Data Collection
Record multiple samples of the gestures:

Up-Down: Move the device vertically.

Left-Right: Move the device horizontally.

Label the data correctly during recording.

Step 4: Create an Impulse
Add:

Input block: Time series data (Accelerometer).

Processing block: Spectral Analysis.

Learning block: Classification (Neural Network).

Step 5: Train Your Model
Use the collected and labeled data.

Train a neural network using Edge Impulse Studio.

Check accuracy and performance in the training results.

Step 6: Model Testing
Use the Model Testing tab with new test data to verify classification accuracy.

Step 7: Deployment
Go to the Deployment tab.

Choose output format:

Arduino Library (for Nano BLE Sense)

WebAssembly (for browser-based testing)

Mobile Application (for smartphone use)

Step 8: Run Real-Time Inference
Use your device to perform gestures.

See real-time classification in the Edge Impulse Studio or through serial output (Arduino).

✅ Results & Conclusion
The model successfully identifies simple motion gestures with high accuracy. This project demonstrates how edge AI and embedded ML can be applied to real-world problems like gesture recognition, opening possibilities in smart control, accessibility devices, and more.

📷 Screenshots (Optional)
Add images of:

Data collection

Model training results

Live classification

📚 References
Edge Impulse Documentation

Arduino Nano 33 BLE Sense
