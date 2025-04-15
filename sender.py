from picamera2 import Picamera2
import time
import requests

# --- Configuration ---
API_ENDPOINT = "http:/http://localhost:8000/upload_image"  # Replace with your FastAPI endpoint
IMAGE_FILENAME = "captured_image.jpg"

def capture_image():
    """Captures an image using the Raspberry Pi camera."""
    picam2 = Picamera2()
    try:
        picam2.start()
        time.sleep(2)  # Allow camera to warm up
        picam2.capture_file(IMAGE_FILENAME)
        print(f"Image captured and saved as: {IMAGE_FILENAME}")
    finally:
        picam2.close()
    return IMAGE_FILENAME

def send_image_to_api(image_path, api_url):
    """Sends the captured image to the specified API endpoint."""
    try:
        with open(image_path, 'rb') as image_file:
            files = {'image': (image_path, image_file, 'image/jpeg')}
            response = requests.post(api_url, files=files)
            response.raise_for_status()  # Raise an exception for bad status codes
            print("Image sent successfully!")
            print(f"API Response: {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending image: {e}")
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")

if __name__ == "__main__":
    captured_file = capture_image()
    if captured_file:
        send_image_to_api(captured_file, API_ENDPOINT)