import os
import csv
import io
import re
from google.cloud import vision
from google.oauth2 import service_account
from PIL import Image

# Set credentials environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "vision_key.json"

# Initialize Google Vision client
credentials = service_account.Credentials.from_service_account_file("vision_key.json")
client = vision.ImageAnnotatorClient(credentials=credentials)

# Input/output paths
INPUT_FOLDER = "input_images"
OUTPUT_CSV = "ocr_output.csv"

# Optional: regex patterns to extract specific IDs
BOXID_PATTERN = r"BOXID[:\s]*([A-Z0-9\-]+)"
SKID_PATTERN = r"SKID[:\s]*([A-Z0-9\-]+)"

# Create output CSV
with open(OUTPUT_CSV, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Filename", "Extracted Text", "BOXID", "SKID"])

    for filename in os.listdir(INPUT_FOLDER):
        if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
            continue

        image_path = os.path.join(INPUT_FOLDER, filename)

        with io.open(image_path, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)
        response = client.text_detection(image=image)
        texts = response.text_annotations

        if not texts:
            writer.writerow([filename, "", "", ""])
            continue

        full_text = texts[0].description.strip().replace("\n", " ")

        boxid_match = re.search(BOXID_PATTERN, full_text)
        skid_match = re.search(SKID_PATTERN, full_text)

        boxid = boxid_match.group(1) if boxid_match else ""
        skid = skid_match.group(1) if skid_match else ""

        writer.writerow([filename, full_text, boxid, skid])
