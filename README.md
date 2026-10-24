# Quiz Chess — Classroom Challenge

Quiz Chess is a two-player, same-screen chess game. A player must answer a question to complete a capture. The current `math01` pack contains math questions; other subjects can be added as new question folders. The game includes question images, four difficulty levels, and CSV answer logs.

## Browser-only demo

Build the GitHub Pages site locally:

```bash
python3 scripts/build_static.py
python3 -m http.server 8000 --directory site
```

Open `http://localhost:8000/`. The static build contains the `math01` question set and its images. Both players share one device. Answer logs are downloaded as CSV files in the browser; no backend, accounts, online multiplayer, or shared leaderboard is provided. The build excludes old player logs and server files.

The static demo is published at **https://pts-style.github.io/quiz-chess/** from the default branch `v3-b` using the GitHub Pages workflow in `.github/workflows/pages.yml`.

## Docker mode

Run `docker compose up --build -d` from the repository root and open `http://localhost:7777/`. The Node.js service saves answer logs through `/api/saveGameLog`; Nginx proxies `/api/` to the service. MongoDB and Socket.IO remain part of the existing Compose stack even though the current chess page does not require them to play.
