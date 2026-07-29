# Wesley Gabriel — Portfólio

Meu portfólio pra buscar estágio em dev. Feito com Flask porque queria aprender backend na prática.

🔗 **Live:** *em breve*

## O que tem

- Tema escuro/claro porque eu não aguento site sem dark mode
- Filtro de projetos por tecnologia
- Formulário de contato que manda email (quando configurado)
- Responsivo — abre no celular de boa

## Stack

Python + Flask no backend, HTML/CSS/JS na frente. Nada de framework JS, queria entender o básico primeiro.

## Rodar

```bash
pip install -r requirements.txt
python app.py
# → http://localhost:5000
```

Precisa de um arquivo `.env` com `SECRET_KEY` (e `MAIL_*` se quiser email de verdade).

## Deploy

Tá preparado pra Render — é só conectar o repositório, build `pip install -r requirements.txt`, start `gunicorn app:app`.

---

Feito por mim, Wesley Gabriel, 2026.