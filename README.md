🎮 Space Invaders

Prosta gra stworzona w Pythonie z użyciem Pygame.

🚀 Wymagania
Python 3.x
Pygame

Instalacja Pygame:

pip install pygame

▶️ Uruchomienie
python main.py

🎯 Sterowanie (przykład)
← → — ruch gracza
Spacja — strzał

🧠 Jak działa gra
Gra działa w pętli
Ekran jest czyszczony co klatkę
Obiekty są rysowane od nowa
Wynik rośnie za trafienia
Przeciwnicy i power-upy pojawiają się dynamicznie

💥 System pocisków
Pociski są przechowywane w listach (bulletX, bulletY)
Każdy pocisk porusza się co klatkę
Kolizje sprawdzane są między każdym pociskiem a przeciwnikiem

📈 System punktów
score_value zwiększa się za trafienia
Co 10 punktów zmienia się poziom lub pojawiają się nowe elementy