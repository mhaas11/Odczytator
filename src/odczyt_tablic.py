import argparse
import easyocr
import cv2
import matplotlib.pyplot as plt

def detect_license_plate_text(image_path):

    image = cv2.imread(image_path)
    if image is None:
        print(f"Nie można wczytać obrazu z podanej ścieżki: {image_path}")
        return

    reader = easyocr.Reader(['en'])
    
    results = reader.readtext(image)

    for (bbox, text, prob) in results:
        print(f"Znaleziony tekst: {text} (pewność: {prob})")

        (top_left, top_right, bottom_right, bottom_left) = bbox
        top_left = tuple([int(val) for val in top_left])
        bottom_right = tuple([int(val) for val in bottom_right])
        image = cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)

    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

def main():
    parser = argparse.ArgumentParser(description="OCR dla tablic rejestracyjnych")
    parser.add_argument("image_path", type=str, help="Ścieżka do obrazu")
    args = parser.parse_args()

    detect_license_plate_text(args.image_path)

if __name__ == "__main__":
    main()
