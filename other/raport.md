# Raport

Największym wyzwaniem było odpowiednie określenie pola odczytu tekstu na obrazie. Spotkałem się z różnymi ciekawymi problemami, takimi jak:
- Wyznaczenie dokładnych współrzędnych prostokąta obejmującego tekst.
- Dostosowanie algorytmu do różnych typów obrazów.
- Maksymalnie skrócony i maksymalnie przejrzysty kod. 
- Optymalizacja działania skryptu w przypadku zmieniających się warunków oświetleniowych i jakości obrazu. Jeśli obraz jest o niskiej rozdzielczości to potrafi podać losowe odczyty albo w ogóle nic. Ten skrypt raczej by na takim odcinku pomiarowym by się często mylił :)

# Plany na przyszłość

Kod jest bardzo podatny na modyfikacje. Można dodać:
- Obługa wykrywania tablic każdego kraju (Teraz też program powinien sobie z tym poradzić lecz do przetestowania)
- Obsługa wykrywania numerów kilku tablic
- Zapis do bazy danych, pierwotny plan obejmował zapis w MongoDB lub PostgreSQL
- Wykrywanie nie tylko numerów tablic ale również ogólnie tekstu np. Napisy z niektórych znaków drogowych
