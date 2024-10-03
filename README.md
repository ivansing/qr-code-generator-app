# QR Code Genrator App

A Python script tool to generate QR Code in the browser. It uses `qrcode` a Python library to encode strings and generate a QR Code. For server it uses Flask Python library for online UI in HTML.

## Project Structure

```bash
├── README.md
├── app.py
├── static
└── templates
    └── index.html
```

## Requirements

- Python 3.7+
- `qrcode` Python library
- Flask Python library

## Installation

1. Clone the repository
```bash
git clone https://github.com/ivansing/qr-code-generator-app.git
    cd audio-to-text-app
```

2. Install libraries:
```bash
pip install qrcode Flask
```

## Usage

1. Run the app by typing:
```bash
python3 app.py
```
2. You will see a warning don't pay attention to it, just copy the URL: `127.0.0.1:5000`
3. Open your browser and copy any URL in the input box:
`https://www.example.com/

That will generate QR Code.

## How it works

1. Makes the server using Flask library to show the browser.
2. The `qrcode` converts the data, builds the path, save the path
to return a file ouput.
3. The ouput will be show in the `index.html` document.

## License

This project is licensed under the MIT License.

Acknoledgements

- [Python Language](https://www.python.org/)
- [pypi library qrcode](https://pypi.org/project/qrcode/)

