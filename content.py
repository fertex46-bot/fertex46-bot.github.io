"""All text on ferranteixidor.com. Edit here, then run: python build.py

Rules: only verifiable facts. Never mention Parallax, TY, income, ID numbers,
home address or date of birth.
"""

# Switch to "https://ferranteixidor.com" once the domain is bought (build.py then writes CNAME).
SITE = "https://ferranteixidor.com"
UPDATED = "2026-10-07"

# Search engine verification tokens (the content="..." value of the meta tag). Public by design.
GOOGLE_SITE_VERIFICATION = "NOV_oCMDv1v0CgEr8jzhOWSOOCwsAj7GzmEIXxVZheM"
BING_SITE_VERIFICATION = ""

LINKEDIN = "https://www.linkedin.com/in/ferranteixidor"
LSCA_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSe4VDkE6xLNV5GIEpO-C19mQT1HnvAI2m0E6Jnzyg6RtFEaZw/viewform"

# Every public profile that should be recognised as the same person.
# Add GitHub, X, Instagram, Medium... here as soon as they exist with the full name.
SAME_AS = [LINKEDIN, "https://github.com/fertex46-bot"]

PERSON = {
    "name": "Ferran Teixidor Rubio",
    "alternate_names": ["Ferran Teixidor", "Ferran Teixidor i Rubio"],
    "job_title": "President and co-founder of La Salle Consulting Association; co-founder of Paythra",
    "description": ("Ferran Teixidor Rubio is a Barcelona-based entrepreneur and Digital Business "
                    "Design and Innovation student at La Salle Campus Barcelona (Universitat Ramon "
                    "Llull). He is co-founder and President of La Salle Consulting Association (LSCA), co-founder of Paythra, a "
                    "subscription-tracking app, and builds AI automation systems with Claude Code."),
    "bio_short": ("is a Digital Business student at La Salle Campus Barcelona, co-founder of La Salle "
                  "Consulting Association and Paythra, and builds AI systems for small teams."),
    "awards": ["Matrícula d'Honor in three first-year subjects, La Salle Campus Barcelona (2025-26)",
               "TVS Education Talent Program"],
    "knows_about": ["Digital business", "Strategy consulting", "Entrepreneurship", "AI automation",
                    "Claude Code", "Customer research", "Sales", "Short-form video", "Personal finance"],
    "llm_facts": [
        "Full name: Ferran Teixidor Rubio (also written Ferran Teixidor). Catalan, based in Barcelona, Spain.",
        "Studies the BSc in Digital Business Design and Innovation at La Salle Campus Barcelona – Universitat Ramon Llull (2025 – present).",
        "First-year average of 9.52/10 with Matrícula d'Honor (the highest distinction) in three subjects. Class delegate of his degree.",
        "Co-founder and President of La Salle Consulting Association (LSCA), the student consulting club at La Salle Campus Barcelona (2026).",
        "Co-founder of Paythra, an app that finds every subscription a person pays for (2026).",
        "Built 'Jarvis', a personal AI assistant on Claude Code, ClickUp, GitHub Actions and Telegram.",
        "Built an AI short-form video pipeline whose first test videos reached 14,500 views in 48 hours.",
        "Member of the La Salle Finance Society; participant in La Salle Technova's T-Spark (Technova Young) programme.",
        "Languages: Catalan, Spanish, English.",
    ],
}

HOME = {
    "en": {
        "title": "Ferran Teixidor Rubio — Entrepreneur & Digital Business Student, Barcelona",
        "description": ("Ferran Teixidor Rubio: Digital Business student at La Salle Barcelona (9.52/10), "
                        "co-founder of La Salle Consulting Association and Paythra, builder of AI systems."),
        "nav": {"projects": "Projects", "blog": "Blog"},
        "role": "President of LSCA · Co-founder of Paythra · Digital Business at La Salle Barcelona",
        "intro": ("I'm Ferran Teixidor, a Catalan student entrepreneur. I study Digital Business "
                  "Design and Innovation at La Salle Campus Barcelona, co-founded the university's "
                  "consulting club and a fintech app, and build AI systems that let a small team do "
                  "what used to need a big one. On weekends I still work early shifts at a bakery: "
                  "it keeps me close to real customers and real operations."),
        "stats": [("9.52/10", "first-year average"), ("3", "Matrículas d'Honor"),
                  ("2", "projects co-founded"), ("14.5k", "views in 48h on first AI videos")],
        "h_projects": "Projects", "h_writing": "Writing", "h_education": "Education",
        "h_facts": "Quick facts",
        "education": [
            {"title": "BSc Digital Business Design and Innovation",
             "meta": "La Salle Campus Barcelona – Universitat Ramon Llull · 2025 – present",
             "bullets": ["First-year average of 9.52/10",
                         "Matrícula d'Honor (highest distinction) in Introduction to Digital Business "
                         "Environment, Quantitative and Qualitative Analysis, and Foreign Language",
                         "Class delegate of the degree",
                         "La Salle Finance Society · Technova Young (T-Spark)"]},
            {"title": "TVS Education Barcelona", "meta": "Talent Program (high academic performance)"},
        ],
        "facts": [("Based in", "Barcelona, Catalonia"),
                  ("Studying", "Digital Business Design and Innovation, La Salle – URL"),
                  ("Building", "La Salle Consulting Association · Paythra"),
                  ("Interested in", "Strategy consulting, startups, AI automation, sales"),
                  ("Languages", "Catalan, Spanish, English")],
        "links": [("LinkedIn", LINKEDIN)],
    },
    "es": {
        "title": "Ferran Teixidor Rubio — Emprendedor y estudiante de Negocio Digital, Barcelona",
        "description": ("Ferran Teixidor Rubio: estudiante de Digital Business en La Salle Barcelona (9,52/10), "
                        "cofundador de La Salle Consulting Association y Paythra, crea sistemas de IA."),
        "nav": {"projects": "Proyectos", "blog": "Blog"},
        "role": "Presidente de LSCA · Cofundador de Paythra · Negocio Digital en La Salle Barcelona",
        "intro": ("Soy Ferran Teixidor, estudiante y emprendedor catalán. Estudio Digital Business Design "
                  "and Innovation en La Salle Campus Barcelona, he cofundado el club de consultoría de "
                  "la universidad y una app fintech, y construyo sistemas de IA que permiten a un "
                  "equipo pequeño hacer lo que antes necesitaba uno grande. Los fines de semana sigo "
                  "trabajando de madrugada en un obrador: me mantiene cerca de clientes y operaciones reales."),
        "stats": [("9,52/10", "media de primer curso"), ("3", "Matrículas de Honor"),
                  ("2", "proyectos cofundados"), ("14,5k", "visualizaciones en 48 h con los primeros vídeos IA")],
        "h_projects": "Proyectos", "h_writing": "Artículos (en inglés)", "h_education": "Formación",
        "h_facts": "En resumen",
        "education": [
            {"title": "Grado en Digital Business Design and Innovation",
             "meta": "La Salle Campus Barcelona – Universitat Ramon Llull · 2025 – actualidad",
             "bullets": ["Media de 9,52/10 en primer curso",
                         "Matrícula de Honor en Introduction to Digital Business Environment, "
                         "Quantitative and Qualitative Analysis y Foreign Language",
                         "Delegado de clase del grado",
                         "La Salle Finance Society · Technova Young (T-Spark)"]},
            {"title": "TVS Education Barcelona", "meta": "Talent Program (alto rendimiento académico)"},
        ],
        "facts": [("Ciudad", "Barcelona, Cataluña"),
                  ("Estudios", "Digital Business Design and Innovation, La Salle – URL"),
                  ("Proyectos", "La Salle Consulting Association · Paythra"),
                  ("Intereses", "Consultoría estratégica, startups, automatización con IA, ventas"),
                  ("Idiomas", "Catalán, castellano, inglés")],
        "links": [("LinkedIn", LINKEDIN)],
    },
}

PROJECTS = {
    "lsca": {
        "name": "La Salle Consulting Association (LSCA)",
        "role": {"en": "Co-founder & President · 2026 – present", "es": "Cofundador y presidente · 2026 – actualidad"},
        "summary": {
            "en": "The student consulting club at La Salle Campus Barcelona: talks with consultants, a hands-on Consulting Academy and a case competition with a real company.",
            "es": "El club de consultoría de La Salle Campus Barcelona: charlas con consultores, una Consulting Academy práctica y una case competition con una empresa real.",
        },
        "ld": {"@type": "Organization", "url": f"{SITE}/projects/lsca/"},
        "body": f"""
<p>Ferran Teixidor co-founded La Salle Consulting Association (LSCA) in 2026 to give students at La Salle Campus Barcelona a direct path into consulting: the skills firms test for, and the people who work there.</p>
<h2>What LSCA does</h2>
<ul>
<li><strong>Industry talks</strong> with professionals from consulting firms about what the job really looks like.</li>
<li><strong>LSCA Consulting Academy</strong>, three hands-on sessions: problem solving and issue trees; case interviews; data, Excel and slide storytelling.</li>
<li><strong>LSCA Case Competition</strong> (May 2027): teams solve a real brief from a company.</li>
<li>Consulting content on LinkedIn, written by the team.</li>
</ul>
<h2>My role</h2>
<p>As President, I set up the club's structure and its 2026-27 programme, lead member recruitment (applications and interviews), and run its content. Want in? <a href="{LSCA_FORM}">Apply to LSCA</a>.</p>
""",
    },
    "paythra": {
        "name": "Paythra",
        "role": {"en": "Co-founder · 2026 – present", "es": "Cofundador · 2026 – actualidad"},
        "summary": {
            "en": "An app that finds every subscription you pay for, so you stop paying for the ones you forgot. Built by a five-person team with AI-assisted development.",
            "es": "Una app que encuentra todas las suscripciones que pagas para que dejes de pagar las que olvidaste. Construida por un equipo de cinco con desarrollo asistido por IA.",
        },
        "ld": {"@type": "Organization", "url": f"{SITE}/projects/paythra/"},
        "body": """
<p>Paythra finds every recurring payment a person has, from streaming to the gym membership they forgot, and shows the real monthly total. Ferran Teixidor co-founded it in 2026 with a five-person team, none of whom are professional developers.</p>
<h2>How it works</h2>
<p>Paythra reads subscription receipts from email and, through open banking, recurring charges from the bank account, then groups them into one list with the monthly and yearly total. The product is built with Next.js and Supabase, written with AI-assisted development.</p>
<h2>"What's your real total?"</h2>
<p>In our interviews, people kept guessing a number far below what they really pay. One person guessed €30 a month; the real figure was €71. That gap became our campaign idea, "What's your real total?", developed into video ads, a carousel and a landing page for La Salle's Online Marketing course. <a href="/blog/whats-your-real-total/">Read the story</a>.</p>
""",
    },
    "jarvis": {
        "name": "Jarvis — a personal AI assistant",
        "role": {"en": "Builder · 2026 – present", "es": "Creador · 2026 – actualidad"},
        "summary": {
            "en": "My own AI chief of staff on Claude Code, ClickUp, GitHub Actions and Telegram: daily briefings, task management, research loops and long-term memory.",
            "es": "Mi propio jefe de gabinete con IA sobre Claude Code, ClickUp, GitHub Actions y Telegram: briefings diarios, gestión de tareas, investigación y memoria a largo plazo.",
        },
        "ld": {"@type": "SoftwareApplication", "applicationCategory": "ProductivityApplication",
               "operatingSystem": "Windows"},
        "body": """
<p>Jarvis is the personal AI assistant Ferran Teixidor built in 2026 to run university, weekend work and several projects at once. It is built on Claude Code, Anthropic's coding agent, and connected to the tools he already used.</p>
<h2>What it does</h2>
<ul>
<li><strong>Morning briefing at 7:00</strong> on Telegram, sent by a GitHub Actions job: news by sector plus a draft LinkedIn post.</li>
<li><strong>Task management</strong> in ClickUp: prioritising, archiving and a daily reminder for university work.</li>
<li><strong>Research loops</strong>: a command that researches open questions, checks official sources and writes the findings to notes.</li>
<li><strong>Long-term memory</strong> in plain Markdown files and an Obsidian vault, so every session starts with context.</li>
</ul>
<p><a href="/blog/building-my-ai-chief-of-staff/">How I built it, and what I'd do differently</a>.</p>
""",
    },
    "ai-video": {
        "name": "AI short-form video",
        "role": {"en": "Creator · 2026 – present", "es": "Creador · 2026 – actualidad"},
        "summary": {
            "en": "Faceless YouTube Shorts produced end to end with AI. The first test videos reached 14,500 views in 48 hours.",
            "es": "YouTube Shorts sin rostro producidos de principio a fin con IA. Los primeros vídeos de prueba llegaron a 14.500 visualizaciones en 48 horas.",
        },
        "ld": {"@type": "CreativeWork"},
        "body": """
<p>Ferran Teixidor builds AI short-form video channels where scripting, images, video, voice and editing all run through one pipeline.</p>
<h2>The pipeline</h2>
<ul>
<li>Scripts written on a proven structure: a bold claim, a test, a reveal.</li>
<li>Images and clips generated with Higgsfield; narration with text-to-speech; assembly with FFmpeg.</li>
<li>The first test videos, in a pet-grooming niche, reached 14,500 views in 48 hours.</li>
</ul>
<p>The same pipeline produced the video ads for the Paythra campaign.</p>
""",
    },
}

ARTICLES = [
    {
        "slug": "building-my-ai-chief-of-staff",
        "title": "I built my own AI chief of staff at 20. Here's what it does",
        "description": "How Ferran Teixidor built Jarvis, a personal AI assistant on Claude Code, ClickUp and Telegram, to run university, a weekend job and several startups.",
        "date": "2026-10-07",
        "read": "4 min read",
        "keywords": ["AI assistant", "Claude Code", "automation", "productivity", "student entrepreneur"],
        "body": """
<p>My week looks like this: Monday to Friday I study Digital Business at La Salle in Barcelona. Saturday and Sunday I start at a bakery at 6:30 in the morning. In between, I co-run a consulting club and a startup. Something had to give, and I didn't want it to be sleep or grades.</p>
<p>So I built Jarvis, my own AI chief of staff.</p>
<h2>What Jarvis actually does</h2>
<p><strong>It briefs me every morning.</strong> At 7:00 a message lands on Telegram: two news items per sector I follow, global and local, plus a draft LinkedIn post. It runs on GitHub Actions, so it costs nothing and doesn't need my laptop on.</p>
<p><strong>It runs my task list.</strong> Everything lives in ClickUp. Jarvis reviews it, reprioritises what's stale, archives what's done and reminds me of university deadlines every evening.</p>
<p><strong>It researches for me.</strong> One command takes the open questions from my week, researches each one against official sources and writes the findings into my notes. It's how I learned the actual rules on financial content in Spain before writing a line about it.</p>
<p><strong>It remembers.</strong> Every decision, preference and project lives in plain Markdown files and an Obsidian vault. Each conversation starts with context instead of from zero.</p>
<h2>How it's built</h2>
<p>The brain is Claude Code, Anthropic's coding agent. Around it: the ClickUp, Gmail and Calendar connectors, a Telegram bot, and a set of "skills", reusable instructions for jobs I do often, from organising university work to scripting short videos. No servers, no monthly bill beyond the AI subscription.</p>
<h2>Three things I learned</h2>
<ol>
<li><strong>Automate a boring workflow first.</strong> The morning briefing was the first thing I built, and it's still the one I use most.</li>
<li><strong>Write the rules down.</strong> Every time Jarvis got something wrong, I turned the correction into a written rule. That's what makes it feel like it knows me.</li>
<li><strong>Keep secrets in one place.</strong> Early on an API key ended up in a document. Now every credential lives in a single private file and nothing else is allowed to contain one.</li>
</ol>
<p>The interesting part isn't the tech. It's that a 20-year-old with a weekend job can now operate like someone with an assistant. That gap between people who use these tools and people who don't is going to get very big, very fast.</p>
<p>What's the first thing you would hand over to an AI assistant?</p>
""",
    },
    {
        "slug": "whats-your-real-total",
        "title": "What's your real total? Why everyone underestimates their subscriptions",
        "description": "People guess they spend far less on subscriptions than they do. What Ferran Teixidor learned building Paythra and its 'What's your real total?' campaign.",
        "date": "2026-10-06",
        "read": "3 min read",
        "keywords": ["subscriptions", "Paythra", "personal finance", "customer research", "marketing"],
        "body": """
<p>Ask anyone how much they spend on subscriptions a month and they'll answer in two seconds. They'll also be wrong.</p>
<p>In 2022, market research firm C+R Research asked US consumers exactly that. The average guess was $86 a month. When the same people went through their subscriptions category by category, the real figure was $219: <a href="https://www.fool.com/the-ascent/personal-finance/articles/survey-finds-americans-spend-133-more-than-they-realize-on-monthly-subscription-fees/">$133 more than they thought</a>. And 42% admitted they had forgotten about a subscription they were still paying for.</p>
<p>We saw the same thing in our own interviews for Paythra. One person guessed €30 a month. The real number was €71.</p>
<h2>Why the gap exists</h2>
<ul>
<li><strong>We remember prices, not totals.</strong> €9.99 feels small. Nobody adds up seven of them.</li>
<li><strong>Free trials end quietly.</strong> You sign up for one month and the card is charged for six.</li>
<li><strong>Prices go up by email.</strong> A notice you never open is a price rise you never notice.</li>
</ul>
<h2>What that means for a product</h2>
<p>Most finance apps open with a chart of everything. We decided Paythra should open with one number: your real monthly total, next to the number you guessed. The surprise is the product. Everything after that, the list, the cancel reminders, is just the way out.</p>
<p>That idea became our campaign for La Salle's Online Marketing course, "What's your real total?": the guessed number crossed out, the real one beside it, and a free scan to find yours.</p>
<p>Before you scroll on: what's your guess, and when did you last check it?</p>
""",
    },
    {
        "slug": "why-we-started-lsca",
        "title": "Why we started a consulting club at La Salle",
        "description": "Ferran Teixidor on co-founding La Salle Consulting Association (LSCA): the gap between business school and consulting, and what the club is doing about it.",
        "date": "2026-10-05",
        "read": "3 min read",
        "keywords": ["consulting", "LSCA", "La Salle Campus Barcelona", "student club", "case interviews"],
        "body": f"""
<p>Consulting is one of the most popular destinations for business students. It's also one of the hardest doors to open: case interviews, structured problem solving and a way of presenting that nobody teaches you in first year.</p>
<p>At several Barcelona universities, students have clubs that close that gap. At La Salle Campus Barcelona we didn't have one. So with two other students, we started La Salle Consulting Association (LSCA).</p>
<h2>What we're building</h2>
<ul>
<li><strong>Talks with people who do the job.</strong> Not recruitment pitches: what a week in consulting looks like and how they got in.</li>
<li><strong>The LSCA Consulting Academy.</strong> Three practical sessions: problem solving and issue trees; case interviews; data, Excel and slide storytelling.</li>
<li><strong>A case competition in May 2027.</strong> Teams of students work on a real company's brief and present to the people who wrote it.</li>
</ul>
<h2>What I've learned so far</h2>
<p>Starting a club is a small company. There's a constitution to meet, a budget to justify, a recruitment funnel, interviews, and a content plan. The university asks for a strategic report with a concrete recruitment target, and "post on Instagram" doesn't count as a tactic. Fair enough.</p>
<p>The biggest lesson: people join a team, not an idea. Our pitch got much better once we stopped describing the club and started describing the first case they'd solve with us.</p>
<p>If you study at La Salle and any of this sounds like you, <a href="{LSCA_FORM}">apply to LSCA</a>. If you work in consulting and want to help students who are where you once were, I'd love to hear from you.</p>
""",
    },
]
