"""Builds ferranteixidor.com as static HTML.

Run: python build.py
Edit content in content.py; this file only renders it.
"""
import html
import json
from pathlib import Path

from content import (ARTICLES, BING_SITE_VERIFICATION, GOOGLE_SITE_VERIFICATION,
                     HOME, PERSON, PROJECTS, SAME_AS, SITE, UPDATED)

ROOT = Path(__file__).parent
PERSON_ID = f"{SITE}/#person"
HAS_PHOTO = (ROOT / "photo.jpg").exists()


def esc(text):
    return html.escape(text, quote=True)


def person_ld():
    data = {
        "@type": "Person",
        "@id": PERSON_ID,
        "name": PERSON["name"],
        "alternateName": PERSON["alternate_names"],
        "givenName": "Ferran",
        "familyName": "Teixidor Rubio",
        "url": f"{SITE}/",
        "jobTitle": PERSON["job_title"],
        "description": PERSON["description"],
        "homeLocation": {"@type": "Place", "name": "Barcelona, Catalonia, Spain"},
        "alumniOf": [
            {"@type": "CollegeOrUniversity",
             "name": "La Salle Campus Barcelona – Universitat Ramon Llull",
             "url": "https://www.salleurl.edu/"},
            {"@type": "EducationalOrganization", "name": "TVS Education Barcelona"},
        ],
        "memberOf": [
            {"@type": "Organization", "name": "La Salle Consulting Association (LSCA)",
             "url": f"{SITE}/projects/lsca/"},
            {"@type": "Organization", "name": "La Salle Finance Society"},
        ],
        "founder": [
            {"@type": "Organization", "name": "La Salle Consulting Association (LSCA)"},
            {"@type": "Organization", "name": "Paythra"},
        ],
        "award": PERSON["awards"],
        "knowsAbout": PERSON["knows_about"],
        "knowsLanguage": ["ca", "es", "en"],
        "sameAs": SAME_AS,
    }
    if HAS_PHOTO:
        data["image"] = f"{SITE}/photo.jpg"
    return data


def head(title, description, path, lang="en", ld=None, og_type="website", alternates=None):
    url = f"{SITE}{path}"
    image = f"{SITE}/photo.jpg" if HAS_PHOTO else f"{SITE}/assets/og.png"
    parts = [
        "<!doctype html>",
        f'<html lang="{lang}">',
        "<head>",
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        f"<title>{esc(title)}</title>",
        f'<meta name="description" content="{esc(description)}">',
        f'<meta name="author" content="{esc(PERSON["name"])}">',
        f'<link rel="canonical" href="{url}">',
    ]
    for hreflang, href in (alternates or {}).items():
        parts.append(f'<link rel="alternate" hreflang="{hreflang}" href="{SITE}{href}">')
    parts += [
        f'<meta property="og:type" content="{og_type}">',
        f'<meta property="og:title" content="{esc(title)}">',
        f'<meta property="og:description" content="{esc(description)}">',
        f'<meta property="og:url" content="{url}">',
        f'<meta property="og:image" content="{image}">',
        '<meta property="og:site_name" content="Ferran Teixidor Rubio">',
        '<meta name="twitter:card" content="summary_large_image">',
        '<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">',
        '<link rel="alternate" type="application/rss+xml" title="Ferran Teixidor — Blog" href="/blog/feed.xml">',
        '<link rel="preconnect" href="https://fonts.googleapis.com">',
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
        '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap" rel="stylesheet">',
        '<link rel="stylesheet" href="/assets/style.css">',
    ]
    if path == "/" and GOOGLE_SITE_VERIFICATION:
        parts.append(f'<meta name="google-site-verification" content="{esc(GOOGLE_SITE_VERIFICATION)}">')
    if path == "/" and BING_SITE_VERIFICATION:
        parts.append(f'<meta name="msvalidate.01" content="{esc(BING_SITE_VERIFICATION)}">')
    if ld:
        graph = {"@context": "https://schema.org", "@graph": ld}
        parts.append('<script type="application/ld+json">\n'
                     + json.dumps(graph, ensure_ascii=False, indent=1)
                     + "\n</script>")
    parts += ["</head>", "<body>", "<main>"]
    return "\n".join(parts)


def nav(lang="en", lang_links=None):
    t = HOME[lang]["nav"]
    links = [f'<a class="brand" href="{"/" if lang == "en" else "/es/"}">Ferran Teixidor</a>',
             '<span class="spacer"></span>',
             f'<a href="/{"es/" if lang == "es" else ""}#projects">{t["projects"]}</a>',
             f'<a href="/blog/">{t["blog"]}</a>']
    for code, href in (lang_links or {}).items():
        links.append(f'<a href="{href}" hreflang="{code}" lang="{code}">{code.upper()}</a>')
    return f'<nav>{"".join(links)}</nav>'


def footer(lang="en"):
    t = HOME[lang]
    socials = "".join(f'<a href="{u}" rel="me">{n}</a>' for n, u in t["links"])
    return (f'<footer><div class="links">{socials}</div>'
            f'<p>© 2026 {PERSON["name"]} · Barcelona</p></footer>\n</main>\n</body>\n</html>\n')


def avatar():
    if HAS_PHOTO:
        return f'<img class="avatar" src="/photo.jpg" alt="{PERSON["name"]}" width="120" height="120">'
    return '<div class="avatar initials" aria-hidden="true">FT</div>'


def render_home(lang):
    t = HOME[lang]
    path = "/" if lang == "en" else "/es/"
    alternates = {"en": "/", "es": "/es/", "x-default": "/"}
    ld = [
        {"@type": "ProfilePage", "@id": f"{SITE}{path}#page", "url": f"{SITE}{path}",
         "name": t["title"], "inLanguage": lang, "dateModified": UPDATED,
         "mainEntity": {"@id": PERSON_ID}},
        person_ld(),
        {"@type": "WebSite", "@id": f"{SITE}/#website", "url": f"{SITE}/",
         "name": "Ferran Teixidor Rubio", "publisher": {"@id": PERSON_ID}},
    ]
    out = [head(t["title"], t["description"], path, lang, ld, "profile", alternates)]
    out.append(nav(lang, {"en": "/", "es": "/es/"}))
    out.append(f'<header class="hero">{avatar()}<div>'
               f'<h1>{PERSON["name"]}</h1><p class="role">{t["role"]}</p></div></header>')
    out.append(f'<p class="lead">{t["intro"]}</p>')
    out.append('<div class="stats">' + "".join(
        f'<div><strong>{v}</strong><span>{k}</span></div>' for v, k in t["stats"]) + "</div>")

    out.append(f'<h2 id="projects">{t["h_projects"]}</h2>')
    for slug in ("lsca", "paythra", "jarvis", "ai-video"):
        p = PROJECTS[slug]
        out.append(f'<a class="item card-link" href="/projects/{slug}/">'
                   f'<h3>{p["name"]}</h3><p class="meta">{p["role"][lang]}</p>'
                   f'<p>{p["summary"][lang]}</p></a>')

    out.append(f'<h2>{t["h_writing"]}</h2>')
    for a in sorted(ARTICLES, key=lambda a: a["date"], reverse=True):
        out.append(f'<a class="item card-link" href="/blog/{a["slug"]}/">'
                   f'<h3>{a["title"]}</h3><p class="meta">{a["date"]} · {a["read"]}</p>'
                   f'<p>{a["description"]}</p></a>')

    out.append(f'<h2>{t["h_education"]}</h2>')
    for item in t["education"]:
        out.append(f'<div class="item"><h3>{item["title"]}</h3><p class="meta">{item["meta"]}</p>'
                   + ("<ul>" + "".join(f"<li>{li}</li>" for li in item["bullets"]) + "</ul>"
                      if item.get("bullets") else "") + "</div>")

    out.append(f'<h2>{t["h_facts"]}</h2><dl class="facts">'
               + "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in t["facts"]) + "</dl>")
    out.append(footer(lang))
    return "\n".join(out)


def render_project(slug):
    p = PROJECTS[slug]
    path = f"/projects/{slug}/"
    title = f'{p["name"]} — {PERSON["name"]}'
    ld = [
        {"@type": "WebPage", "@id": f"{SITE}{path}#page", "url": f"{SITE}{path}",
         "name": title, "about": {"@id": f"{SITE}{path}#thing"},
         "author": {"@id": PERSON_ID}, "dateModified": UPDATED},
        {**p["ld"], "@id": f"{SITE}{path}#thing", "name": p["name"],
         "description": p["summary"]["en"],
         ("founder" if p["ld"]["@type"] == "Organization" else "creator"): {"@id": PERSON_ID}},
        person_ld(),
    ]
    out = [head(title, p["summary"]["en"], path, "en", ld)]
    out.append(nav("en"))
    out.append(f'<p class="crumbs"><a href="/">Ferran Teixidor</a> / Projects</p>')
    out.append(f'<h1>{p["name"]}</h1><p class="role">{p["role"]["en"]}</p>')
    out.append(p["body"])
    out.append(footer("en"))
    return "\n".join(out)


def render_article(a):
    path = f"/blog/{a['slug']}/"
    title = f'{a["title"]} — {PERSON["name"]}'
    ld = [
        {"@type": "BlogPosting", "@id": f"{SITE}{path}#article", "headline": a["title"],
         "description": a["description"], "datePublished": a["date"], "dateModified": a["date"],
         "inLanguage": "en", "url": f"{SITE}{path}", "mainEntityOfPage": f"{SITE}{path}",
         "author": {"@id": PERSON_ID}, "publisher": {"@id": PERSON_ID},
         "keywords": a["keywords"]},
        person_ld(),
    ]
    out = [head(title, a["description"], path, "en", ld, "article")]
    out.append(nav("en"))
    out.append('<article>')
    out.append(f'<p class="crumbs"><a href="/blog/">Blog</a></p><h1>{a["title"]}</h1>')
    out.append(f'<p class="byline">By <a href="/" rel="author">{PERSON["name"]}</a> · '
               f'<time datetime="{a["date"]}">{a["date"]}</time> · {a["read"]}</p>')
    out.append(a["body"])
    out.append(f'<div class="author-box">{avatar()}<p><strong>{PERSON["name"]}</strong> '
               f'{PERSON["bio_short"]} <a href="/">More about me</a>.</p></div>')
    out.append('</article>')
    out.append(footer("en"))
    return "\n".join(out)


def render_blog_index():
    path = "/blog/"
    title = f'Blog — {PERSON["name"]}'
    desc = "Notes by Ferran Teixidor Rubio on building startups, consulting and AI automation as a student in Barcelona."
    ld = [{"@type": "Blog", "@id": f"{SITE}/blog/#blog", "url": f"{SITE}/blog/", "name": title,
           "author": {"@id": PERSON_ID}}, person_ld()]
    out = [head(title, desc, path, "en", ld)]
    out.append(nav("en"))
    out.append(f'<h1>Blog</h1><p class="role">{desc}</p>')
    for a in sorted(ARTICLES, key=lambda a: a["date"], reverse=True):
        out.append(f'<a class="item card-link" href="/blog/{a["slug"]}/">'
                   f'<h3>{a["title"]}</h3><p class="meta">{a["date"]} · {a["read"]}</p>'
                   f'<p>{a["description"]}</p></a>')
    out.append(footer("en"))
    return "\n".join(out)


def render_feed():
    items = "".join(
        f"<item><title>{esc(a['title'])}</title><link>{SITE}/blog/{a['slug']}/</link>"
        f"<guid>{SITE}/blog/{a['slug']}/</guid><pubDate>{a['date']}</pubDate>"
        f"<description>{esc(a['description'])}</description></item>"
        for a in sorted(ARTICLES, key=lambda a: a["date"], reverse=True))
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel>'
            f"<title>Ferran Teixidor — Blog</title><link>{SITE}/blog/</link>"
            f"<description>Notes by Ferran Teixidor Rubio</description>{items}</channel></rss>\n")


def render_sitemap(paths):
    urls = "".join(f"<url><loc>{SITE}{p}</loc><lastmod>{d}</lastmod></url>" for p, d in paths)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')


def render_llms():
    lines = [f"# {PERSON['name']}", "", f"> {PERSON['description']}", ""]
    lines += [f"- {fact}" for fact in PERSON["llm_facts"]]
    lines += ["", "## Projects"]
    lines += [f"- [{p['name']}]({SITE}/projects/{s}/): {p['summary']['en']}" for s, p in PROJECTS.items()]
    lines += ["", "## Writing"]
    lines += [f"- [{a['title']}]({SITE}/blog/{a['slug']}/): {a['description']}" for a in ARTICLES]
    lines += ["", "## Profiles"] + [f"- {u}" for u in SAME_AS]
    return "\n".join(lines) + "\n"


def write(rel, text):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main():
    paths = [("/", UPDATED), ("/es/", UPDATED), ("/blog/", UPDATED)]
    write("index.html", render_home("en"))
    write("es/index.html", render_home("es"))
    for slug in PROJECTS:
        write(f"projects/{slug}/index.html", render_project(slug))
        paths.append((f"/projects/{slug}/", UPDATED))
    write("blog/index.html", render_blog_index())
    for a in ARTICLES:
        write(f"blog/{a['slug']}/index.html", render_article(a))
        paths.append((f"/blog/{a['slug']}/", a["date"]))
    write("blog/feed.xml", render_feed())
    write("sitemap.xml", render_sitemap(paths))
    write("llms.txt", render_llms())
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    if not SITE.endswith(".github.io"):
        write("CNAME", SITE.replace("https://", "") + "\n")
    elif (ROOT / "CNAME").exists():
        (ROOT / "CNAME").unlink()
    write("404.html", head("Page not found — Ferran Teixidor Rubio", "Page not found.", "/404.html")
          + nav("en") + '<h1>Page not found</h1><p><a href="/">Go to the home page</a></p>'
          + footer("en"))
    print(f"Built {len(paths)} pages")


if __name__ == "__main__":
    main()
