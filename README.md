# OCR dla Tablic Rejestracyjnych

Ten skrypt w Pythonie wykorzystuje `EasyOCR` do wykrywania i rozpoznawania tekstu na tablicach rejestracyjnych samochodów. Wyniki są wyświetlane w konsoli oraz na obrazie z zaznaczonymi miejscami wykrytego tekstu.

## Wymagania

Przed uruchomieniem skryptu upewnij się, że masz zainstalowane następujące biblioteki:

- Python 3.6 lub nowszy
- easyocr
- opencv-python
- matplotlib

Możesz zainstalować te zależności, wykonując poniższe polecenie:

```sh
pip install easyocr opencv-python matplotlib
```
## Użycie
Klonowanie repozytorium:

```sh
git clone https://github.com/twoje/repo.git
cd twoje/repo
```
Uruchomienie skryptu:

```sh
python skrypt.py sciezka/do/obrazu
```

Na przykład, jeśli masz obraz w folderze images:

```sh
python skrypt.py images/license_plate.jpg
Sprawdzenie ścieżki do pliku:
```
Upewnij się, że ścieżka do pliku obrazu jest poprawna. Jeśli plik znajduje się w tym samym katalogu co skrypt, wystarczy podać nazwę pliku:

```sh
python skrypt.py license_plate.jpg
```
## Autor
Maksymilian Haas 52686
