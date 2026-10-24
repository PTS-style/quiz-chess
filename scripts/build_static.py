"""Package Quiz Chess for static hosting without backend or player logs."""

from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "web_proxy_nginx"
DEST = ROOT / "site"


def main():
    if DEST.exists():
        shutil.rmtree(DEST)
    DEST.mkdir()
    for name in ("index.html", "board_config.js", "chess_logic.js", "chess_rules.html", "character_abilities.html"):
        shutil.copy2(SOURCE / name, DEST / name)

    html = DEST / "index.html"
    text = html.read_text(encoding="utf-8")
    marker = '<script src="board_config.js"></script>'
    assert text.count(marker) == 1
    html.write_text(text.replace(marker, '<script>window.QUIZ_CHESS_STATIC = true;</script>\n    ' + marker), encoding="utf-8")

    game = SOURCE / "all_game" / "math01"
    target = DEST / "all_game" / "math01"
    target.mkdir(parents=True)
    for folder in ("img_L1", "img_L2", "img_L3", "img_L4", "img_role"):
        shutil.copytree(game / folder, target / folder)
    (DEST / ".nojekyll").touch()
    print(f"Built Quiz Chess site at {DEST}")


if __name__ == "__main__":
    main()
