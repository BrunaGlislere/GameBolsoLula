import sys
from pathlib import Path

import webview


def resource_path(*parts: str) -> Path:
    """Resolve caminhos para recursos (dev e executável PyInstaller)."""
    if hasattr(sys, "_MEIPASS"):
        base = Path(sys._MEIPASS)
    else:
        base = Path(__file__).resolve().parent
    return base.joinpath(*parts)


def main():
    # Caminho do index.html dentro da pasta do jogo
    index_path = resource_path("jogo-fuga-mapa-brasil", "index.html").resolve()
    if not index_path.exists():
        raise FileNotFoundError(
            f"index.html não encontrado em {index_path}. Certifique-se de que a pasta 'jogo-fuga-mapa-brasil' existe."
        )

    # Abre a janela carregando o arquivo local
    window = webview.create_window(
        title="Fuga do Mapa do Brasil",
        url=index_path.as_uri(),
        width=1100,
        height=700,
        resizable=True,
        confirm_close=False,
    )
    # Força o backend Edge/Chromium quando disponível (melhor compatibilidade de JS)
    try:
        webview.start(gui='edgechromium')
    except Exception:
        webview.start()


if __name__ == "__main__":
    main()
