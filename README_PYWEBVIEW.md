Executar o jogo com Python + pywebview
======================================

Pré-requisitos
- Python 3.9+ no Windows

Instalação e execução (dev)
1) Crie e ative um ambiente virtual (opcional, mas recomendado):
   - PowerShell: `python -m venv .venv; .\.venv\Scripts\Activate.ps1`
2) Instale dependências: `pip install -r requirements.txt`
3) Execute: `python run.py`

Empacotar em .exe (PyInstaller)
1) Instale o PyInstaller: `pip install pyinstaller`
2) Gere o executável (mantendo a pasta do jogo):
   - `pyinstaller --noconsole --onefile --add-data "jogo-fuga-mapa-brasil;jogo-fuga-mapa-brasil" run.py`
3) O arquivo final ficará em `dist/run.exe`. Copie a pasta de assets junto se usar modo onedir.

Sobre os obstáculos (PNG)
- O Obstáculo 1 usa `jogo-fuga-mapa-brasil/assets/lula.png`.
- O Obstáculo 2 usa `jogo-fuga-mapa-brasil/assets/bolsonaro.png`.
- Se os PNGs não estiverem presentes, o jogo usa um fallback desenhado.

Observação
- O HTML está em `jogo-fuga-mapa-brasil/index.html`. Os caminhos de assets são relativos, então funcionarão tanto no dev quanto no executável PyInstaller.

