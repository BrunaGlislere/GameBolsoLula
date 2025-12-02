% Fuga do Macaco Mailon

<img width="1330" height="787" alt="image" src="https://github.com/user-attachments/assets/3f48e22a-ce6c-4a99-aad6-efee47170471" />


Jogo 2D em HTML/CSS/JS (Canvas) — controle um macaco Mailon tentando chegar à fronteira sem encostar nos obstáculos. Há uma caixa de "Sonegação" que transforma o macaco em um gorila após ~2 segundos. Fundo com favela (imagem) até metade do mapa e árvores no restante, com transição suave e bandeira de chegada.

## Executar (HTML)
```
Descompacte a pasta para habilitar os assets
Acesse GameBolsoLula-main\GameBolsoLula-main\jogo-fuga-mapa-brasil\index.html
Deleite-se nessa obra de arte
```

## Executar (desktop com pywebview)
```
pip install -r requirements.txt
python run.py****
```

## Estrutura
- `jogo-fuga-mapa-brasil/assets/` — imagens (`lula.png`, `bolsonaro.png`, `favela-back.png`)
- `run.py` — launcher pywebview
- `requirements.txt` — dependências (pywebview)

## Controles
- A/D ou ←/→ — mover
- Espaço ou ↑ — pular
- E — entrar/sair da caixa
- P — pausar/continuar
- Enter/R — reiniciar nas telas de fim

## Observações
- Caso a imagem `favela-back.png` não esteja presente, um fundo procedural desfocado é usado como fallback.
- O projeto evita bibliotecas externas além do pywebview (opcional) para empacotar em .exe.
