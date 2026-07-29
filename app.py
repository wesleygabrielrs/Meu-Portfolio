from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-key-mude-em-producao')

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
    'github': 'https://github.com/wesleygabriel',
    'linkedin': 'https://linkedin.com/in/wesleygabriel',
    'email': 'wesley@email.com',
    'whatsapp': '5581999999999',
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
        'github': 'https://github.com/wesleygabriel/newmed-improved',
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
    assunto = request.form.get('assunto', '').strip()
    mensagem = request.form.get('mensagem', '').strip()

    if not nome or not email or not mensagem:
        return jsonify({'ok': False, 'erro': 'Preencha nome, email e mensagem.'}), 400

    # Em desenvolvimento: apenas loga no console
    # Em produção: configurar envio de e-mail (ver README)
    print(f'\n{'='*50}')
    print(f'NOVO CONTATO — {datetime.now().strftime("%d/%m/%Y %H:%M")}')
    print(f'{'='*50}')
    print(f'Nome:     {nome}')
    print(f'E-mail:   {email}')
    print(f'Assunto:  {assunto}')
    print(f'Mensagem: {mensagem}')
    print(f'{'='*50}\n')

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