# Malicious URL Detection Web Application 🚨🔍

This repository contains code for a FastAPI web application that detects whether a given URL is benign or potentially malicious using a pre-trained model. The application provides a user-friendly web interface powered by Gradio.
## See the Demo 🖥️

To see the demo of the web application in action, visit [this link](https://huggingface.co/spaces/kmack/kmack-malicious-url-detection).

## How to Use 🛠️

1. **Clone the Repository:**  
   ```bash
   git clone https://github.com/sandunlakshan13/malicious-url-detection.git
   cd malicious-url-detection
## Install Dependencies:
2. **Navigate to the project directory and install the required dependencies by running:**
   ```bash
   pip install -r requirements.txt
## Install Dependencies:
3. **Run the Application:**
   ```bash
   uvicorn app:app --reload
## Access the Web Interface:
4. **Once the server is running, open your web browser and go to http://localhost:8000 to access the web interface.**

## Additional Notes 🚀
- This application utilizes a pre-trained model for malicious URL detection. The model is based on the kmack/malicious-url-detection model from the [Hugging Face Transformers library](https://huggingface.co/kmack/malicious-url-detection).
- The application is designed to run locally, but it can be deployed to a server for production use.

## Support 🤝

For any questions or issues regarding the application, feel free to [open an issue](https://github.com/sandunlakshan13/malicious-url-detection/issues) on GitHub.

## Credits 💡

This application was developed using [FastAPI](https://fastapi.tiangolo.com/) and [Gradio](https://gradio.app/).  
The malicious URL detection model is based on [kmack/malicious-url-detection](https://huggingface.co/kmack/malicious-url-detection) from the Hugging Face Transformers library.




