# FIND THE BUTTON!

Welcome to a playful web challenge where you search for the correct button among many. This project uses a colorful, responsive layout and a simple button game mechanic to create a fun, lighthearted experience.

<strong>Features:</strong>

- <em>Large button grid</em> for a bold visual effect
- <span style="color: #00bfff;">Bright gradient background</span> for a modern look
- <strong><span style="font-size: 1.1em;">Animated hover states</span></strong> on each button

Enjoy the game and feel free to customize the style and button behavior!

<strong>License:</strong>

This project is released under the MIT License. You are free to use, copy, modify, and distribute the source code while keeping the original copyright notice and license terms.

## ENGLISH

<strong>How to use:</strong>

1. Open `index.html` in a browser.
2. Search for the correct button among the grid.
3. Click the winning button to reveal the success page.
4. Use `stylesheet.css` to adjust visual styles and `won.html` as the win screen.
5. For large button generation, update the `buttonGen.py` script and run it with Python.

<strong>Docker instructions:</strong>

1. Make sure Docker is installed and the Docker service is running.
2. Open a terminal in the `FindTheButton` project folder.
3. Build the Docker image with:
   - `docker compose build`
4. Start the container with:
   - `docker compose up -d`
5. Open `http://localhost:8080` in your browser (or the port defined in `compose.yaml`).
6. To stop the container, use:
   - `docker compose down`

If you make changes to the project, run `docker compose up -d --build` to rebuild the image.

## DEUTSCH

<strong>Anleitung:</strong>

1. Öffne `index.html` in einem Browser.
2. Suche den richtigen Button im Raster.
3. Klicke den Gewinner-Button, um die Erfolgsseite anzuzeigen.
4. Nutze `stylesheet.css`, um das Design anzupassen, und `won.html` als Gewinnseite.
5. Für große Button-Generierung bearbeite `buttonGen.py` und führe es mit Python aus.

<strong>Docker Anleitung:</strong>

1. Stelle sicher, dass Docker installiert und der Docker-Dienst gestartet ist.
2. Öffne eine Konsole im Projektordner `FindTheButton`.
3. Baue das Docker-Image mit:
   - `docker compose build`
4. Starte den Container mit:
   - `docker compose up -d`
5. Öffne im Browser `http://localhost:8080` (oder den in `compose.yaml` definierten Port).
6. Um den Container zu stoppen, verwende:
   - `docker compose down`

Wenn du Änderungen am Projekt machst, führe `docker compose up -d --build` aus, damit das Image neu gebaut wird.

Wenn du das Projekt prüfen möchtest, kannst du auch `docker compose ps` verwenden, um den laufenden Dienst zu überprüfen.