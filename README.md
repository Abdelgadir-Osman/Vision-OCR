# Google Vision OCR — Label Reader
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

This script automates the extraction of printed SKID and BOXID labels from packaging images in a warehouse/receiving environment.

## 📦 Features

- Google Vision OCR for printed label text
- Extracts BOXID and SKID via regex
- Outputs structured CSV with file name and parsed results
- Drop-in compatible with SAP or inventory tracking automation

## 🛠 Requirements

- Python 3.8+
- Google Cloud Vision API enabled
- Service Account JSON key (`vision_key.json`)
- Pillow (`pip install pillow`)
- `google-cloud-vision` (`pip install google-cloud-vision`)

## 📂 Folder Structure

