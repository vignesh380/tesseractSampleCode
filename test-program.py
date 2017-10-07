import sys

try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

def setup():
    print "setting up tesseract"
    # pytesseract.pytesseract.tesseract_cmd = sys.argv[1]
    tesseract_dir_config = '--tessdata-dir "path"'
    # pytesseract.image_to_string(Image.open('sample.jpg'),lang="eng",config=tesseract_dir_config)

print(pytesseract.image_to_string(Image.open('sample.jpg')));