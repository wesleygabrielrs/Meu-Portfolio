# Portfolio Wesley Gabriel

> Portfólio interativo desenvolvido com Flask — criado para buscar o primeiro estágio em tecnologia.

**🌐 Live demo:** *em breve*

---

## Funcionalidades

| Funcionalidade | Descrição |
|---|---|
| 🌗 **Tema Dark/Light** | Alterna entre temas com salvamento no navegador |
| 🔍 **Filtro de projetos** | Filtra cards por tecnologia (Python, Web, HTML, etc.) |
| 📬 **Formulário de contato** | Envia mensagem via POST para o backend Flask |
| 📱 **Responsivo** | Adaptado para mobile, tablet e desktop |
| ⚡ **Terminal interativo** | Hero com visual de terminal Python |
| 📄 **Currículo** | Botão para download do PDF (adicione seu arquivo) |

## Tecnologias

- **Python** + **Flask** (backend)
- **HTML5** + **CSS3** (estrutura e estilo)
- **JavaScript** (interatividade)
- **Jinja2** (template engine)
- **dotenv** (variáveis de ambiente)

## Estrutura de Pastas

```
portfolio-wesley/
├── app.py                   # Flask: rotas e dados do portfólio
├── requirements.txt         # Dependências
├── .env                     # Configurações (não comitar)
├── README.md                # Este arquivo
├── static/
│   ├── css/
│   │   └── style.css        # Todos os estilos
│   └── js/
│       └── main.js          # Interatividade
└── templates/
    └── index.html           # Página única
```

## Como Rodar Localmente

### 1. Clone ou copie os arquivos

```bash
cd portfolio-wesley
```

### 2. Crie um ambiente virtual (recomendado)

```bash
python -m venv venv
```

- **Windows:** `venv\Scripts\activate`
- **Linux/Mac:** `source venv/bin/activate`

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o arquivo `.env`

```env
SECRET_KEY=sua-chave-secreta-aqui
```

### 5. Rode o servidor

```bash
python app.py
```

Acesse em: **http://localhost:5000**

---

## Como Adicionar Projetos

Abra `app.py` e edite a lista `projetos`:

```python
projetos = [
    {
        'id': 1,
        'titulo': 'Seu Projeto',
        'descricao': 'Descrição curta do que faz.',
        'tags': ['Python', 'Flask', 'SQL'],
        'github': 'https://github.com/seuusuario/seurepo',
        'site': 'https://seusite.com',
        'status': 'concluido',   # ou 'em-breve'
    },
    # ...
]
```

## Como Adicionar Habilidades

Edite a lista `habilidades` no `app.py`:

```python
habilidades = [
    {'nome': 'Python', 'nivel': 'Estudando', 'icone': '🐍'},
    # 'nivel' pode ser: 'Estudando' ou 'Iniciando'
]
```

## Como Adicionar Formação

Edite a lista `formacao` no `app.py`:

```python
formacao = [
    {
        'tipo': 'graduacao',   # ou 'curso'
        'curso': 'Nome do curso',
        'instituicao': 'Nome da instituição',
        'periodo': '2025 — 2027',
        'descricao': 'Detalhes.',
    },
]
```

## Deploy

### Render (recomendado — gratuito)

1. Crie uma conta em [render.com](https://render.com)
2. Conecte seu repositório GitHub
3. Escolha **Web Service**
4. Build command: `pip install -r requirements.txt`
5. Start command: `gunicorn app:app`
6. Adicione variável de ambiente: `SECRET_KEY`

### Railway

1. Crie conta em [railway.com](https://railway.com)
2. Conecte o repositório
3. O Railway detecta Python automaticamente

---

## Melhorias Futuras

- [ ] Adicionar blog (artigos sobre aprendizado)
- [ ] Integrar envio real de e-mails (SMTP)
- [ ] Página de certificados
- [ ] Modo "console" com comandos
- [ ] SEO e meta tags para LinkedIn/Google

---

## Licença

Este projeto é livre para uso educacional. Sinta-se à vontade para modificar e usar como base para seu próprio portfólio.

---

Feito com ☕ e Flask — Wesley Gabriel, 2026