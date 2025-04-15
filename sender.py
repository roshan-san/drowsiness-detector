import requests
from picamera import PiCamera
import time

# FastAPI server URL
FASTAPI_URL = "http://127.0.0.1:8000:8000/upload_image/"  # Replace with your server's IP

def capture_and_send_image():
    try:
        with PiCamera() as camera:
            camera.resolution = (640, 480)  # Adjust resolution as needed
            time.sleep(2)  # Give the camera some time to warm up
            image_data = io.BytesIO()
            camera.capture(image_data, 'jpeg')
            image_data.seek(0)

            files = {'file': ('image.jpg', image_data, 'image/jpeg')}
            response = requests.post(FASTAPI_URL, files=files)
            response.raise_for_status()  # Raise an exception for bad status codes
            print("Image sent successfully!")
            print(response.json())

    except FileNotFoundError:
        print("Error: PiCamera module not found. Make sure it's enabled.")
    except requests.exceptions.RequestException as e:
        print(f"Error sending image: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    import io
    capture_and_send_image()