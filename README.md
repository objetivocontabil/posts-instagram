# Posts do Instagram – Escritório Contábil Objetivo (@objetivo.contabil)

Repositório público: o Buffer baixa as imagens daqui por link direto
(https://raw.githubusercontent.com/objetivocontabil/posts-instagram/main/PASTA/slide-N.png).
Guarde aqui somente imagens de posts. Nada interno do escritório.

- `AAAA-MM-DD-carrossel.../slide-N.png`: imagens já publicadas ou em rascunho.
- `ferramentas/modelos/modeloN.html`: modelos dos slides (1080x1350). Copie, troque só os textos e renderize.
  - modelo1: fundo degradê roxo→turquesa, título com destaque, dois cartões lado a lado (datas).
  - modelo2: fundo branco, título roxo com destaque, parágrafo e dois cartões numerados.
  - modelo3: fundo turquesa, título escuro, parágrafo e cartão roxo de destaque (logo em cartão branco).
  - modelo4: fundo degradê, título com destaque e três cartões em linha (linha do tempo).
- `ferramentas/render.py`: gera os PNGs. Ex.: `python3 ferramentas/render.py 2026-12-01-carrossel f1.html f2.html`.
- Paleta: roxo #5E0AC0, lilás #8B5CF6, azul #6B8CDB, turquesa #2BBFC4, turquesa claro #4FD6D1, branco, roxo escuro #1E0550.
  Texto branco só sobre roxo/lilás; texto roxo escuro sobre turquesa. Fontes: DM Sans (títulos) e Inter (texto).
- Logo: `ferramentas/logos/` (branco para fundo roxo, original para fundo branco ou cartão branco).
