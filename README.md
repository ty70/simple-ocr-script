# EasyOCR Japanese Text Extractor

This repository provides a simple OCR (Optical Character Recognition) script that extracts text from images containing Japanese and outputs it with confidence scores.
It utilizes [EasyOCR](https://github.com/JaidedAI/EasyOCR), and allows users to specify input image files and output destinations via a CLI (Command Line Interface).

## ✅ Features

* OCR support for both English and Japanese
* Save recognized text along with confidence scores to a file
* Real-time output to the console
* Simple Python script, easy to customize

---

## 📦 Installation

Python 3.7 or higher is recommended.

```bash
pip install easyocr
```

---

## 🚀 Usage

Run the script as follows:

```bash
python ocr_script.py --input input.png --output output.txt
```

* `--input`: Input image file for OCR processing
* `--output`: Text file to save the recognition results

---

## 📄 Sample Output

```
こんにちは (Confidence: 0.95)
ようこそ (Confidence: 0.89)
```

---

## 📁 File Structure

```bash
.
├── LICENSE
├── ocr_script.py      # Main script
├── README_ja.md       # Japanese version
├── README.md          # This file
├── requirements.txt
├── sample.png         # Sample input
└── sample.txt         # Sample output
```

---

## ⚖️ License

This repository is released under the MIT [License](./LICENSE).

---

## ⚠️ Notes

OCR accuracy depends on image quality and font types.

If recognition errors occur, you can refine and restructure the extracted text using tools like ChatGPT.

We recommend a final manual check for best results.
