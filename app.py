from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-key-mude-em-producao')

# ─── Configuração de E-mail ──────────────────────────────
app.config.update(
    MAIL_SERVER=os.environ.get('MAIL_SERVER', 'smtp.gmail.com'),
    MAIL_PORT=int(os.environ.get('MAIL_PORT', 587)),
    MAIL_USE_TLS=os.environ.get('MAIL_USE_TLS', 'true').lower() == 'true',
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME', ''),
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD', ''),
    MAIL_DEFAULT_SENDER=os.environ.get('MAIL_USERNAME', ''),
)
mail = Mail(app)

# ============================================================
# DADOS DO PORTFÓLIO
# ============================================================

informacoes_pessoais = {
    'nome': 'Wesley Gabriel',
    'titulo': 'ADS Student • Aspiring Developer',
    'bio': (
        'Estudante de Análise e Desenvolvimento de Sistemas, '
        'buscando o primeiro estágio na área de tecnologia. '
        'Atualmente focado em Python, desenvolvimento web e '
        'boas práticas de programação. Acredito que código limpo '
        'e bem estruturado faz toda a diferença.'
    ),
    'objetivo': (
        'Busco uma oportunidade de estágio onde possa aplicar '
        'meus conhecimentos, aprender com profissionais experientes '
        'e contribuir com projetos reais.'
    ),
    'github': 'https://github.com/wesleygabrielrs',
    'linkedin': 'https://www.linkedin.com/in/wesley-gabriel-2810aa277/',
    'email': 'wesleygabrielrs@gmail.com',
    'whatsapp': '5581989337444',
}

projetos = [
    {
        'id': 1,
        'titulo': 'Newmed Equipamentos',
        'descricao': (
            'Site institucional completo para empresa de equipamentos '
            'médico-hospitalares. Catálogo de produtos com filtros, '
            'página de detalhes, área do cliente com login, dashboard '
            'de pedidos e suporte. HTML, CSS e JavaScript puro.'
        ),
        'tags': ['HTML', 'CSS', 'JavaScript', 'Web'],
        'github': 'https://github.com/wesleygabrielrs/Site-NewMed',
        'site': None,
        'status': 'concluido',
    },
    {
        'id': 2,
        'titulo': 'Em breve — App de Tarefas',
        'descricao': (
            'Aplicação web com Flask para gerenciamento de tarefas. '
            'CRUD completo, autenticação de usuários e banco de dados '
            'SQLite. Projeto em desenvolvimento para praticar Python '
            'com backend.'
        ),
        'tags': ['Python', 'Flask', 'SQL', 'Web'],
        'github': None,
        'site': None,
        'status': 'em-breve',
    },
    {
        'id': 3,
        'titulo': 'Em breve — CLI Tools',
        'descricao': (
            'Coleção de ferramentas de linha de comando em Python '
            'para automatizar tarefas do dia a dia. Projeto para '
            'praticar Python puro, manipulação de arquivos e '
            'boas práticas de CLI.'
        ),
        'tags': ['Python'],
        'github': None,
        'site': None,
        'status': 'em-breve',
    },
]

habilidades = [
    {'nome': 'Python',     'nivel': 'Estudando', 'icone': '🐍'},
    {'nome': 'Flask',      'nivel': 'Iniciando', 'icone': '🌶️'},
    {'nome': 'HTML',       'nivel': 'Estudando', 'icone': '📄'},
    {'nome': 'CSS',        'nivel': 'Estudando', 'icone': '🎨'},
    {'nome': 'JavaScript', 'nivel': 'Iniciando', 'icone': '⚡'},
    {'nome': 'Git',        'nivel': 'Iniciando', 'icone': '🔄'},
    {'nome': 'SQL',        'nivel': 'Iniciando', 'icone': '🗄️'},
]

formacao = [
    {
        'tipo': 'graduacao',
        'curso': 'Análise e Desenvolvimento de Sistemas',
        'instituicao': 'Faculdade de Tecnologia',
        'periodo': '2025 — 2027',
        'descricao': 'Cursando o 2º semestre.',
    },
    {
        'tipo': 'curso',
        'curso': 'Python 3 — Mundo 1, 2 e 3',
        'instituicao': 'Curso em Vídeo (Gustavo Guanabara)',
        'periodo': '2025',
        'descricao': 'Fundamentos da linguagem Python.',
    },
]


# ============================================================
# ROTAS
# ============================================================

@app.route('/')
def index():
    tags = sorted(set(
        tag for p in projetos for tag in p['tags']
    ))
    return render_template(
        'index.html',
        info=informacoes_pessoais,
        projetos=projetos,
        tags=tags,
        habilidades=habilidades,
        formacao=formacao,
        ano=datetime.now().year,
    )


@app.route('/contato', methods=['POST'])
def contato():
    nome = request.form.get('nome', '').strip()
    email = request.form.get('email', '').strip()
    assunto = request.form.get('assunto', '').strip() or 'Contato do Portfólio'
    mensagem = request.form.get('mensagem', '').strip()

    if not nome or not email or not mensagem:
        return jsonify({'ok': False, 'erro': 'Preencha nome, email e mensagem.'}), 400

    destino = os.environ.get('MAIL_DESTINO', '')

    if destino and app.config['MAIL_USERNAME'] and app.config['MAIL_PASSWORD']:
        try:
            corpo = f"""<h3>Novo contato do portfólio</h3>
<p><strong>Nome:</strong> {nome}</p>
<p><strong>E-mail:</strong> {email}</p>
<p><strong>Assunto:</strong> {assunto}</p>
<hr><p>{mensagem}</p><hr>
<p style="color:#888;font-size:12px">Enviado por {nome} via portfólio — {datetime.now().strftime('%d/%m/%Y %H:%M')}</p>"""

            msg = Message(
                subject=f'[Portfólio] {assunto}',
                recipients=[destino],
                html=corpo,
                reply_to=email,
            )
            mail.send(msg)
            print(f'\nE-mail enviado para {destino} — assunto: {assunto}')
            return jsonify({
                'ok': True,
                'mensagem': 'Mensagem enviada! Obrigado pelo contato, responderei em breve.'
            })
        except Exception as e:
            print(f'\nErro ao enviar e-mail: {e}')
            # Fallback: log no console

    # Fallback: apenas loga no console
    print(f'\n{"="*50}')
    print(f'NOVO CONTATO (modo dev) — {datetime.now().strftime("%d/%m/%Y %H:%M")}')
    print(f'{"="*50}')
    print(f'Nome:     {nome}')
    print(f'E-mail:   {email}')
    print(f'Assunto:  {assunto}')
    print(f'Mensagem: {mensagem}')
    print(f'{"="*50}\n')

    return jsonify({
        'ok': True,
        'mensagem': 'Mensagem recebida! Obrigado pelo contato, responderei em breve.'
    })


# ============================================================
# INÍCIO
# ============================================================

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)