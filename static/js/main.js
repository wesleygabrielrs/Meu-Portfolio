/* ============================================================
   PORTFÓLIO WESLEY GABRIEL — main.js
   Interatividade: tema, filtro, formulário, hamburger, scroll
   ============================================================ */

document.addEventListener('DOMContentLoaded', function () {

    // ============================================================
    // 1. TEMA DARK / LIGHT
    // ============================================================
    const toggle = document.getElementById('themeToggle');
    const html   = document.documentElement;

    function setTheme(theme) {
        html.setAttribute('data-theme', theme);
        try { localStorage.setItem('portfolio-theme', theme); } catch (_) {}
    }

    // Carrega tema salvo (ou respeita preferência do sistema)
    const saved = (() => {
        try { return localStorage.getItem('portfolio-theme'); } catch (_) { return null; }
    })();
    if (saved) {
        setTheme(saved);
    } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches) {
        setTheme('light');
    }

    if (toggle) {
        toggle.addEventListener('click', function () {
            const next = html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
            setTheme(next);
        });
    }

    // ============================================================
    // 2. FILTRO DE PROJETOS
    // ============================================================
    const filterBar = document.getElementById('filterBar');
    const grid      = document.getElementById('projetosGrid');

    if (filterBar && grid) {
        const cards = grid.querySelectorAll('.projeto-card');

        filterBar.addEventListener('click', function (e) {
            const btn = e.target.closest('.filter-btn');
            if (!btn) return;

            // Ativa o botão clicado
            filterBar.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filter = btn.getAttribute('data-filter');

            cards.forEach(card => {
                const tags = card.getAttribute('data-tags') || '';
                if (filter === 'todos' || tags.includes(filter)) {
                    card.style.display = 'flex';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    }

    // ============================================================
    // 3. FORMULÁRIO DE CONTATO (fetch → Flask)
    // ============================================================
    const form       = document.getElementById('contatoForm');
    const feedback   = document.getElementById('formMsgFeedback');

    if (form && feedback) {
        form.addEventListener('submit', async function (e) {
            e.preventDefault();

            const btn = document.getElementById('btnEnviar');
            if (btn) { btn.disabled = true; btn.textContent = 'Enviando…'; }

            const data = new URLSearchParams(new FormData(form));

            try {
                const res = await fetch('/contato', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                    body: data,
                });

                const json = await res.json();

                if (json.ok) {
                    feedback.className = 'form-msg success';
                    feedback.textContent = json.mensagem;
                    form.reset();
                } else {
                    feedback.className = 'form-msg error';
                    feedback.textContent = json.erro || 'Erro ao enviar. Tente novamente.';
                }
            } catch (_) {
                feedback.className = 'form-msg error';
                feedback.textContent = 'Erro de conexão. Verifique sua internet.';
            } finally {
                if (btn) { btn.disabled = false; btn.textContent = 'Enviar Mensagem →'; }
                feedback.style.display = 'block';
                // Esconde a mensagem após 8 segundos
                setTimeout(() => { feedback.style.display = 'none'; }, 8000);
            }
        });
    }

    // ============================================================
    // 4. HAMBURGER MENU (mobile)
    // ============================================================
    const hamburger = document.getElementById('hamburger');
    const navLinks  = document.getElementById('navLinks');

    if (hamburger && navLinks) {
        hamburger.addEventListener('click', function () {
            navLinks.classList.toggle('open');
        });

        // Fecha ao clicar em um link
        navLinks.querySelectorAll('a').forEach(function (link) {
            link.addEventListener('click', function () {
                navLinks.classList.remove('open');
            });
        });

        // Fecha ao clicar fora
        document.addEventListener('click', function (e) {
            if (!navLinks.contains(e.target) && !hamburger.contains(e.target)) {
                navLinks.classList.remove('open');
            }
        });
    }

    // ============================================================
    // 5. ANIMAÇÃO DOS CONTADORES (stats)
    // ============================================================
    const statNumbers = document.querySelectorAll('.stat-number[data-count]');
    if (statNumbers.length && 'IntersectionObserver' in window) {
        const obs = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (!entry.isIntersecting) return;
                const el = entry.target;
                const target = parseInt(el.getAttribute('data-count'), 10);
                if (isNaN(target) || el.classList.contains('animated')) return;
                el.classList.add('animated');

                let current = 0;
                const step = Math.max(1, Math.floor(target / 30));
                const timer = setInterval(function () {
                    current += step;
                    if (current >= target) {
                        current = target;
                        clearInterval(timer);
                    }
                    el.textContent = current;
                }, 40);
                obs.unobserve(el);
            });
        }, { threshold: .5 });
        statNumbers.forEach(function (el) { obs.observe(el); });
    }

    // ============================================================
    // 6. ANIMAÇÃO DAS SKILL BARS (ao scroll)
    // ============================================================
    const skillBars = document.querySelectorAll('.hab-bar-fill');
    if (skillBars.length && 'IntersectionObserver' in window) {
        const obs = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (!entry.isIntersecting) return;
                const bar = entry.target;
                if (bar.classList.contains('animated')) return;
                bar.classList.add('animated');
                // Lê a porcentagem do data-pct definido no template
                const pct = bar.getAttribute('data-pct') || '50';
                bar.style.width = pct + '%';
                obs.unobserve(bar);
            });
        }, { threshold: .3 });
        skillBars.forEach(function (bar) {
            // Começa com 0 para animar
            bar.style.width = '0';
            // Remove inline depois do primeiro render
            requestAnimationFrame(function () {
                bar.style.width = '0';
                obs.observe(bar);
            });
        });
    }

    // ============================================================
    // 7. SCROLL SUAVE (fallback para navegadores sem scroll-behavior)
    // ============================================================
    document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
        anchor.addEventListener('click', function (e) {
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                const offset = 70; // altura da navbar
                const top    = target.getBoundingClientRect().top + window.pageYOffset - offset;
                window.scrollTo({ top: top, behavior: 'smooth' });
            }
        });
    });

}); // DOMContentLoaded