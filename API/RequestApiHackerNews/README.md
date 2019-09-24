# Python-matplotlib-API-pygal/World-population_import_json/hn_submission"

Projekt wykorzystujący blibliteke pygal do wykreowania wykresu, i 
bilioteke requests do zapytań api.

Celem programu jest wysłanie zapytania API do seriwsu "https://hacker-news.firebaseio.com", z prośbą o informacje o najpoularniejszych postach.
Następnie wypisuje status_code zapytania.
Nastepnie program wysyła oddzielne zapytanie do każdego artykułu, i wypisuje go.
kolejnym krokiem jest utworzenie wykresu, który pokazuje które posty są najpopularniejsze, informacje o iliści komentarzy, i link do posta.
wykres zapisany jest w pliku hn_submissions.svg

do programu "hn_sumbissions.py" został utworzony test, który sprawdza czy status_code zaytania Api ma wartość "200"

