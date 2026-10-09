# -*- coding: utf-8 -*-
"""One-shot builder: adapt Crafto charity pages for ProGen Bénin."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent

HEAD = '''<!doctype html>
<html class="no-js" lang="fr">
    <head>
        <title>{title}</title>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="author" content="ProGen Bénin / GUELICHWEB">
        <meta name="viewport" content="width=device-width,initial-scale=1.0" />
        <meta name="description" content="{description}">
        <link rel="shortcut icon" href="images/favicon.png">
        <link rel="apple-touch-icon" href="images/apple-touch-icon-57x57.png">
        <link rel="apple-touch-icon" sizes="72x72" href="images/apple-touch-icon-72x72.png">
        <link rel="apple-touch-icon" sizes="114x114" href="images/apple-touch-icon-114x114.png">
        <link rel="preconnect" href="https://fonts.googleapis.com" crossorigin>
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link rel="stylesheet" href="css/vendors.min.css"/>
        <link rel="stylesheet" href="css/icon.min.css"/>
        <link rel="stylesheet" href="css/style.css"/>
        <link rel="stylesheet" href="css/responsive.css"/>
        <link rel="stylesheet" href="demos/charity/charity.css" />
    </head>
    <body data-mobile-nav-style="classic">
'''

def header(active=""):
    def cls(key):
        return ' active' if active == key else ''
    return f'''        <!-- start header -->
        <header class="header-with-topbar"> 
            <div class="header-top-bar top-bar-light bg-gradient-corduroy-green-dark-goldenrod disable-fixed">
                <div class="container-fluid">
                    <div class="row h-42px align-items-center justify-content-center">
                        <div class="col-auto text-center">
                            <span class="bg-black-transparent-light ps-15px pe-15px d-inline-block align-middle fs-10 text-uppercase text-white border-radius-4px fw-700 me-15px lh-26">Démo</span>
                            <div class="d-inline-block align-middle fs-12 text-white text-uppercase fw-500">Démo GUELICHWEB — proposition non officielle</div>
                        </div> 
                    </div>
                </div>
            </div>
            <nav class="navbar navbar-expand-lg header-light border-bottom border-color-transparent-dark-very-light disable-fixed background-position-left-top" style="background-image: url('images/demo-charity-home-bg-01.jpg')">
                <div class="container-fluid justify-content-lg-start">
                    <div class="col-auto">
                        <a class="navbar-brand" href="index.html">
                            <img src="images/progen/logo.webp" alt="ProGen Bénin" class="default-logo" style="max-height:52px;">
                            <img src="images/progen/logo.webp" alt="ProGen Bénin" class="alt-logo" style="max-height:52px;">
                            <img src="images/progen/logo.webp" alt="ProGen Bénin" class="mobile-logo" style="max-height:42px;"> 
                        </a>
                    </div>
                    <div class="col-auto menu-order left-nav">
                        <button class="navbar-toggler float-start" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-label="Basculer la navigation">
                            <span class="navbar-toggler-line"></span>
                            <span class="navbar-toggler-line"></span>
                            <span class="navbar-toggler-line"></span>
                            <span class="navbar-toggler-line"></span>
                        </button>
                        <div class="collapse navbar-collapse" id="navbarNav"> 
                            <ul class="navbar-nav"> 
                                <li class="nav-item"><a href="index.html" class="nav-link{cls('home')}">Accueil</a></li>
                                <li class="nav-item"><a href="demo-charity-about.html" class="nav-link{cls('about')}">À propos</a></li>
                                <li class="nav-item"><a href="demo-charity-causes.html" class="nav-link{cls('causes')}">Projets</a></li>
                                <li class="nav-item"><a href="demo-charity-gallery.html" class="nav-link{cls('gallery')}">Galerie</a></li>
                                <li class="nav-item"><a href="demo-charity-volunteer.html" class="nav-link{cls('team')}">Équipe</a></li>
                                <li class="nav-item"><a href="demo-charity-stories.html" class="nav-link{cls('news')}">Actualités</a></li>
                                <li class="nav-item"><a href="demo-charity-contact.html" class="nav-link{cls('contact')}">Contact</a></li>
                            </ul>
                        </div>
                    </div>
                    <div class="col-auto ms-auto d-none d-xl-flex">
                        <div class="header-icon">
                            <div class="d-none d-xxl-inline-block me-25px"><a href="tel:+22969740000" class="widget-text text-dark-gray fs-16 fw-600"><i class="feather icon-feather-phone-outgoing me-10px"></i>+229 69 74 00 00</a></div>
                            <div class="header-button"><a href="demo-charity-contact.html#don" class="btn btn-very-small btn-dark-gray btn-box-shadow btn-round-edge">Faire un don</a></div>
                        </div> 
                    </div>
                </div>
            </nav>
        </header>
        <!-- end header -->
'''

FOOTER = '''        <!-- start footer -->
        <footer class="position-relative cover-background background-position-center-top pb-0" style="background-image: url('images/progen/join.jpg')">
            <div class="position-absolute left-0px top-0px w-100 h-100 opacity-medium bg-dark-gray"></div>
            <div class="border-bottom border-color-transparent-white-light pb-3 lg-pb-5 sm-pb-45px position-relative">
                <div class="container">
                    <div class="row justify-content-center">
                        <div class="col text-center">
                            <h4 class="mb-0 text-white alt-font fw-400">Soutenez la prochaine génération. <a href="demo-charity-contact.html#don" class="text-decoration-line-bottom-medium text-base-color">Faire un don</a></h4>
                        </div>
                    </div>
                </div>
            </div>
            <div class="container position-relative">
                <div class="row justify-content-center pt-5 pb-5 md-pt-45px md-pb-50px text-center text-sm-start">
                    <div class="col-lg-3 col-md-12 col-sm-6 d-flex flex-column flex-md-row flex-lg-column align-items-md-center align-items-lg-start last-paragraph-no-margin md-mb-35px">
                        <a href="index.html" class="footer-logo d-inline-block xs-mb-15px"><img src="images/progen/logo.webp" alt="ProGen Bénin" style="max-height:56px;"></a>
                        <div class="mt-auto ms-md-auto ms-lg-0 ms-0">
                            <span class="fs-14 text-uppercase text-white fw-500 ls-1px">ONG enregistrée</span>
                            <h6 class="alt-font fw-400 text-base-color mb-0">Depuis 2017</h6>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-4 col-sm-6 sm-mb-35px">
                        <span class="d-block text-white mb-5px fs-14 text-uppercase fw-500 ls-1px">Contact</span>
                        <div class="text-white mb-5px"><i class="feather icon-feather-phone-call fs-16 me-10px text-base-color"></i><a href="tel:+22969740000">+229 69 74 00 00</a></div>
                        <div class="text-white mb-10px"><i class="feather icon-feather-phone-call fs-16 me-10px text-base-color"></i><a href="tel:+22994440303">+229 94 44 03 03</a></div>
                        <div><i class="feather icon-feather-mail fs-16 me-10px text-base-color"></i><a href="mailto:contact@progenbenin.org" class="text-white text-decoration-line-bottom">contact@progenbenin.org</a></div>
                    </div>
                    <div class="col-xxl-4 col-lg-3 col-md-4 col-sm-6 last-paragraph-no-margin xs-mb-35px">
                        <span class="d-block text-white mb-5px fs-14 text-uppercase fw-500 ls-1px">À propos</span>
                        <p class="w-90 text-light-conch-green xl-w-100">ProGen Bénin (Prochaine Génération) — ONG à but non lucratif engagée pour l'éducation, la santé et les droits humains des enfants et des femmes.</p> 
                    </div>
                    <div class="col-xxl-2 col-lg-3 col-md-4 col-sm-6 last-paragraph-no-margin">
                        <span class="d-block text-white mb-15px fs-14 text-uppercase fw-500 ls-1px">Navigation</span>
                        <ul class="footer-navbar flex-column align-items-sm-start">
                            <li class="nav-item"><a href="demo-charity-causes.html" class="nav-link p-0 mb-5px">Projets</a></li>
                            <li class="nav-item"><a href="demo-charity-volunteer.html" class="nav-link p-0 mb-5px">Équipe</a></li>
                            <li class="nav-item"><a href="demo-charity-contact.html" class="nav-link p-0">Contact</a></li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="pt-15px pb-15px bg-racing-green position-relative">
                <div class="container">
                    <div class="row align-items-center"> 
                        <div class="col-lg-7 text-center text-lg-start md-mb-5px"> 
                            <ul class="footer-navbar"> 
                                <li class="nav-item"><a href="index.html" class="nav-link">Accueil</a></li>
                                <li class="nav-item"><a href="demo-charity-about.html" class="nav-link">À propos</a></li>
                                <li class="nav-item"><a href="demo-charity-causes.html" class="nav-link">Projets</a></li>
                                <li class="nav-item"><a href="demo-charity-gallery.html" class="nav-link">Galerie</a></li>
                                <li class="nav-item"><a href="demo-charity-volunteer.html" class="nav-link">Équipe</a></li>
                                <li class="nav-item"><a href="demo-charity-stories.html" class="nav-link">Actualités</a></li>
                                <li class="nav-item"><a href="demo-charity-contact.html" class="nav-link">Contact</a></li>
                            </ul>
                        </div> 
                        <div class="col-lg-5 text-center text-lg-end">
                            <span class="fs-15 text-light-conch-green">Copyright © ProGen Bénin | Démo proposée par GUELICHWEB</span>
                        </div> 
                    </div>
                </div>
            </div>
        </footer>
        <!-- end footer -->
        <div class="scroll-progress d-none d-xxl-block">
          <a href="#" class="scroll-top" aria-label="haut de page">
            <span class="scroll-text">Haut</span><span class="scroll-line"><span class="scroll-point"></span></span>
          </a>
        </div>
        <script type="text/javascript" src="js/jquery.js"></script>
        <script type="text/javascript" src="js/vendors.min.js"></script>
        <script type="text/javascript" src="js/main.js"></script>
    </body>
</html>
'''

def page_title(h1, h2, bg="images/progen/about-16-1.jpg"):
    # Bandeau « mosaïque » : texte à gauche, photo à taille native à droite (pas de fond étiré).
    return f'''        <section class="pg-hero pg-banner top-space-padding">
            <div class="container">
                <div class="row align-items-center pg-banner-inner">
                    <div class="col-lg-8 col-12">
                        <div class="pg-eyebrow">ProGen Bénin</div>
                        <h1 class="pg-title pg-title--sm" data-fancy-text='{{ "opacity": [0, 1], "translateY": [30, 0], "filter": ["blur(16px)", "blur(0px)"], "string": ["{h1}"], "duration": 500, "delay": 0, "speed": 50, "easing": "easeOutQuad" }}'>{h1}</h1>
                        <p class="pg-lead mb-0" data-anime='{{ "translateY": [15, 0], "opacity": [0,1], "duration": 600, "delay": 300, "staggervalue": 200, "easing": "easeOutQuad" }}'>{h2}</p>
                    </div>
                    <div class="col-lg-4 d-none d-lg-block">
                        <figure class="pg-card pg-banner-photo"><img src="{bg}" alt="" loading="eager"></figure>
                    </div>
                </div>
            </div>
            <div class="pg-hero-wave" aria-hidden="true"><svg viewBox="0 0 1440 54" preserveAspectRatio="none"><path d="M0 54V30C240 6 480 0 720 12s480 30 720 6v36z" fill="#fff"/></svg></div>
        </section>
'''

def wrap(title, description, active, body):
    return HEAD.format(title=title, description=description) + header(active) + body + FOOTER

# ---------- INDEX ----------
index_body = r'''
        <section class="pg-hero top-space-padding magic-cursor round-cursor" id="pg-hero">
            <div class="container">
                <div class="row align-items-center pg-hero-inner">
                    <div class="col-lg-6 col-12" data-anime='{ "el": "childs", "translateY": [24, 0], "opacity": [0,1], "duration": 700, "delay": 0, "staggervalue": 160, "easing": "easeOutQuad" }'>
                        <div class="pg-eyebrow">ONG · Bénin</div>
                        <h1 class="pg-title">Protéger les <em>droits</em> des enfants et des femmes</h1>
                        <p class="pg-lead">Pour la prochaine génération du Bénin — éducation, santé et droits humains.</p>
                        <a href="demo-charity-causes.html" class="btn btn-large btn-round-edge with-rounded btn-gradient-green-goldenrod-yellow btn-box-shadow">Découvrir nos projets<span class="bg-white"><i class="fa-solid fa-arrow-right text-dark-golden-yellow"></i></span></a>
                        <div class="pg-proof">
                            <span><i class="bi bi-book"></i>Éducation</span>
                            <span><i class="bi bi-heart-pulse"></i>Santé</span>
                            <span><i class="bi bi-people"></i>Droits humains</span>
                        </div>
                    </div>
                    <div class="col-lg-6 col-12">
                        <div class="pg-mosaic" aria-label="Photos des actions de ProGen Bénin">
                            <figure class="pg-card pg-card--a" data-depth="14"><img src="images/progen/ee-15-1.jpg" alt="Équipe et bénéficiaires de ProGen Bénin réunis" width="1422" height="800" fetchpriority="high"></figure>
                            <figure class="pg-card pg-card--b" data-depth="-10"><img src="images/progen/ms-sonri.jpg" alt="Enfants brandissant leurs livres" width="960" height="720"></figure>
                            <figure class="pg-card pg-card--c" data-depth="20"><img src="images/progen/ee-17.jpg" alt="Enfants avec des jouets éducatifs" width="1000" height="563" style="object-position:50% 35%"></figure>
                            <span class="pg-ring" aria-hidden="true"></span>
                            <div class="pg-badge">
                                <span class="pg-badge-icon"><i class="bi bi-patch-check"></i></span>
                                <span><strong>ONG enregistrée depuis 2017</strong><small>Littoral · Atlantique · Borgou · Alibori</small></span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="pg-hero-wave" aria-hidden="true"><svg viewBox="0 0 1440 54" preserveAspectRatio="none"><path d="M0 54V30C240 6 480 0 720 12s480 30 720 6v36z" fill="#fff"/></svg></div>
            <script>
            (function () {
                var hero = document.getElementById('pg-hero');
                if (!hero || window.matchMedia('(prefers-reduced-motion: reduce)').matches || window.innerWidth < 992) return;
                var cards = hero.querySelectorAll('.pg-card');
                hero.addEventListener('mousemove', function (e) {
                    var r = hero.getBoundingClientRect();
                    var x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
                    cards.forEach(function (c) {
                        var d = parseFloat(c.getAttribute('data-depth')) || 0;
                        c.style.setProperty('--px', (x * d).toFixed(1) + 'px'); c.style.setProperty('--py', (y * d).toFixed(1) + 'px');
                    });
                });
                hero.addEventListener('mouseleave', function () { cards.forEach(function (c) { c.style.setProperty('--px', '0px'); c.style.setProperty('--py', '0px'); }); });
            })();
            </script>
        </section>

        <section class="pt-3 lg-pt-50px sm-pt-30px">
            <div class="container">
                <div class="row justify-content-center mb-3 sm-mb-30px">
                    <div class="col-xxl-7 col-xl-8 col-lg-9 text-center" data-anime='{ "el": "childs", "translateY": [30, 0], "opacity": [0,1], "duration": 600, "delay": 0, "staggervalue": 200, "easing": "easeOutQuad" }'>
                        <h3 class="alt-font text-dark-gray">ONG à but non lucratif pour l'éducation, la santé et les droits humains</h3>
                        <p class="w-90 mx-auto">Prochaine Génération Bénin (ProGen Bénin) agit auprès des enfants, des femmes et des associations de parents d'élèves dans les départements du Littoral, de l'Atlantique, du Borgou et de l'Alibori.</p>
                    </div>
                </div>
                <div class="row row-cols-1 row-cols-lg-4 row-cols-sm-2 justify-content-center mb-5 md-mb-8 sm-mb-40px" data-anime='{ "el": "childs", "translateY": [0, 0], "opacity": [0,1], "duration": 1500, "delay": 100, "staggervalue": 200, "easing": "easeOutQuad" }'>
                    <div class="col custom-icon-with-text-style-02 border-end border-color-extra-medium-gray md-mb-40px">
                        <div class="feature-box ps-40px pe-40px xl-ps-20px xl-pe-20px">
                            <div class="feature-box-icon position-relative">
                                <img class="custom-image-icon mt-30px mb-20px border-radius-6px" src="images/progen/gas-9-1.jpg" alt="Éducation" />
                                <div class="w-80px h-80px bg-white box-shadow-double-large rounded-circle d-flex align-items-center justify-content-center position-absolute top-0px right-0px">
                                    <i class="bi bi-book icon-medium text-gradient-corduroy-green-dark-goldenrod"></i>
                                </div>
                            </div>
                            <div class="feature-box-content last-paragraph-no-margin">
                                <span class="d-block fs-19 fw-500 mb-5px text-dark-gray">Éducation formelle</span>
                                <p>Accompagner enfants et adolescents dans un cadre positif.</p>
                            </div>
                        </div>
                    </div>
                    <div class="col custom-icon-with-text-style-02 border-end border-color-extra-medium-gray md-border-end-0 md-mb-40px">
                        <div class="feature-box ps-40px pe-40px xl-ps-20px xl-pe-20px">
                            <div class="feature-box-icon position-relative">
                                <img class="custom-image-icon mt-30px mb-20px border-radius-6px" src="images/progen/ozg-7-2.jpg" alt="Santé" />
                                <div class="w-80px h-80px bg-white box-shadow-double-large rounded-circle d-flex align-items-center justify-content-center position-absolute top-0px right-0px">
                                    <i class="bi bi-heart-pulse icon-medium text-gradient-corduroy-green-dark-goldenrod"></i>
                                </div>
                            </div>
                            <div class="feature-box-content last-paragraph-no-margin">
                                <span class="d-block fs-19 fw-500 mb-5px text-dark-gray">Santé sexuelle</span>
                                <p>Sensibilisation à la santé sexuelle et de la reproduction en milieu scolaire.</p>
                            </div>
                        </div>
                    </div>
                    <div class="col custom-icon-with-text-style-02 border-end border-color-extra-medium-gray xs-mb-40px">
                        <div class="feature-box ps-40px pe-40px xl-ps-20px xl-pe-20px">
                            <div class="feature-box-icon position-relative">
                                <img class="custom-image-icon mt-30px mb-20px border-radius-6px" src="images/progen/ef-13.jpg" alt="Formation" />
                                <div class="w-80px h-80px bg-white box-shadow-double-large rounded-circle d-flex align-items-center justify-content-center position-absolute top-0px right-0px">
                                    <i class="bi bi-mortarboard icon-medium text-gradient-corduroy-green-dark-goldenrod"></i>
                                </div>
                            </div>
                            <div class="feature-box-content last-paragraph-no-margin">
                                <span class="d-block fs-19 fw-500 mb-5px text-dark-gray">Formation professionnelle</span>
                                <p>Appui aux filles déscolarisées pour un avenir digne.</p>
                            </div>
                        </div>
                    </div>
                    <div class="col custom-icon-with-text-style-02">
                        <div class="feature-box ps-40px pe-40px xl-ps-20px xl-pe-20px">
                            <div class="feature-box-icon position-relative">
                                <img class="custom-image-icon mt-30px mb-20px border-radius-6px" src="images/progen/about-2.jpg" alt="Femmes" />
                                <div class="w-80px h-80px bg-white box-shadow-double-large rounded-circle d-flex align-items-center justify-content-center position-absolute top-0px right-0px">
                                    <i class="bi bi-people icon-medium text-gradient-corduroy-green-dark-goldenrod"></i>
                                </div>
                            </div>
                            <div class="feature-box-content last-paragraph-no-margin">
                                <span class="d-block fs-19 fw-500 mb-5px text-dark-gray">Renforcement des femmes</span>
                                <p>Appui et renforcement des capacités des femmes.</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-12 text-center" data-anime='{ "el": "childs", "translateY": [30, 0], "opacity": [0,1], "duration": 600, "delay": 100, "staggervalue": 200, "easing": "easeOutQuad" }'>
                        <h6 class="mb-0 alt-font text-dark-gray d-inline-block align-middle">Enregistrée en 2017 · 5 projets · 4 départements d'intervention</h6>
                    </div>
                </div>
            </div>
        </section>

        <section class="background-position-left-top position-relative" style="background-image: url('images/demo-charity-home-bg-01.jpg')">
            <div class="position-absolute left-0px top-minus-50px lg-top-minus-40px md-top-minus-25px sm-top-minus-20px xs-top-minus-15px background-position-left-top w-100 h-100px lg-h-60px md-h-50px background-size-100 background-no-repeat" style="background-image: url('images/demo-charity-home-bg-02.jpg')"></div>
            <div class="container">
                <div class="row justify-content-center mb-5 sm-mb-30px">
                    <div class="col-xxl-6 col-xl-7 col-lg-8 text-center last-paragraph-no-margin" data-anime='{ "el": "childs", "translateY": [30, 0], "opacity": [0,1], "duration": 600, "delay": 100, "staggervalue": 200, "easing": "easeOutQuad" }'>
                        <h3 class="alt-font text-dark-gray mb-10px">Nos projets</h3>
                        <p class="w-80 mx-auto sm-w-100">Cinq programmes pour l'éducation, la santé et l'épanouissement des enfants et des filles.</p>
                    </div>
                </div> 
                <div class="row row-cols-1 row-cols-lg-3 row-cols-md-2 justify-content-center mb-4" data-anime='{ "el": "childs", "translateY": [30, 0], "opacity": [0,1], "duration": 600, "delay": 100, "staggervalue": 200, "easing": "easeOutQuad" }'>
'''

projects_home = [
    ("ozg", "images/progen/ozg-8.jpg", "Santé", "Objectif Zéro Grossesse", "Campagnes de sensibilisation des adolescentes en milieu scolaire."),
    ("ef", "images/progen/ef-14.jpg", "Éducation", "Excellence Féminine", "Bourses pour les élèves filles excellentes au primaire."),
    ("gas", "images/progen/gas-11.jpg", "Parrainage", "Give a Smile", "Parrainage scolaire des enfants en situations difficiles."),
    ("ms", "images/progen/ms-sonri.jpg", "Écoles", "Millennium School", "Kits scolaires, matériels et puits d'eau pour les écoles."),
    ("ee", "images/progen/ee-15-1.jpg", "Enfance", "Enfance Épanouie", "Jeux éducatifs et aires de jeux pour les maternelles rurales."),
]

for slug, img, tag, title, desc in projects_home:
    index_body += f'''
                    <div class="col md-mb-30px" id="projet-{slug}">
                        <div class="box-shadow-quadruple-large box-shadow-quadruple-large-hover services-box-style-03 last-paragraph-no-margin border-radius-4px overflow-hidden">
                            <div class="position-relative">
                                <a href="demo-charity-causes.html#{slug}"><img src="{img}" alt="{title}"></a>
                                <span class="btn btn-small btn-rounded btn-base-color text-dark-gray btn-box-shadow ps-15px pe-15px pt-5px pb-5px lh-16 ls-0px fw-700 position-absolute right-25px top-25px">{tag}</span>
                            </div>
                            <div class="bg-white">
                                <div class="ps-40px pe-40px pt-25px pb-25px xl-ps-20px xl-pe-20px text-center">
                                    <a href="demo-charity-causes.html#{slug}" class="d-inline-block fs-20 fw-500 text-dark-gray text-dark-gray-hover mb-5px ls-minus-05px">{title}</a>
                                    <p>{desc}</p>
                                </div> 
                                <div class="border-top border-color-extra-medium-gray pt-15px pb-20px text-center">
                                    <a href="demo-charity-causes.html#{slug}" class="btn btn-link btn-hover-animation-switch btn-large text-dark-gray">
                                        <span>
                                            <span class="btn-text">En savoir plus</span>
                                            <span class="btn-icon"><i class="fa-solid fa-arrow-right"></i></span>
                                            <span class="btn-icon"><i class="fa-solid fa-arrow-right"></i></span>
                                        </span> 
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
'''

index_body += r'''
                </div>
                <div class="row">
                    <div class="col-12 text-center">
                        <div class="fs-15 text-uppercase text-dark-gray fw-600">Tous nos projets en détail. <a href="demo-charity-causes.html" class="text-decoration-line-bottom text-dark-gray text-dark-gray-hover fw-700">Voir les projets</a></div>
                    </div>
                </div>
            </div>
        </section>

        <section class="background-position-left-top position-relative" style="background-image: url('images/demo-charity-home-bg-05.jpg')">
            <div class="position-absolute left-0px top-minus-50px lg-top-minus-25px sm-top-minus-20px xs-top-minus-15px background-position-left-top w-100 h-100px lg-h-60px md-h-50px background-size-100 background-no-repeat" style="background-image: url('images/demo-charity-home-bg-03.jpg')"></div>
            <div class="position-absolute left-0px bottom-minus-50px lg-bottom-minus-50px md-bottom-minus-60px sm-bottom-minus-40px background-position-left-top w-100 h-100px lg-h-70px sm-h-50px background-size-100 background-no-repeat" style="background-image: url('images/demo-charity-home-bg-04.jpg')"></div>
            <div class="container">
                <div class="row justify-content-center mb-5 sm-mb-30px">
                    <div class="col-xxl-6 col-xl-7 text-center" data-anime='{ "el": "childs", "translateY": [30, 0], "opacity": [0,1], "duration": 600, "delay": 100, "staggervalue": 200, "easing": "easeOutQuad" }'>
                        <h3 class="alt-font text-white mb-0">Nos valeurs</h3>
                    </div>
                </div> 
                <div class="row row-cols-1 row-cols-lg-3 row-cols-sm-1 mb-4 ms-2 me-2" data-anime='{ "el": "childs", "translateY": [0, 0], "translateX": [-30, 0], "opacity": [0,1], "duration": 600, "delay": 100, "staggervalue": 200, "easing": "easeOutQuad" }'>
                    <div class="col text-center last-paragraph-no-margin hover-box process-step-style-09 md-mb-50px">
                        <div class="process-step-icon-box position-relative mb-25px"> 
                            <div class="process-step-icon d-flex justify-content-center align-items-center mx-auto rounded-circle h-90px w-90px fs-28 bg-base-color text-dark-gray alt-font">
                                <span class="number position-relative z-index-1">01</span>
                                <div class="box-overlay bg-white rounded-circle"></div>
                            </div>
                        </div>
                        <span class="d-inline-block fw-500 text-white fs-18">Dévouement et Égalité</span>
                        <p class="w-85 d-inline-block text-white opacity-4">Servir sans distinction d'âge, de sexe, de religion ou d'origine.</p>
                    </div>
                    <div class="col text-center last-paragraph-no-margin hover-box process-step-style-09 md-mb-50px">
                        <div class="process-step-icon-box position-relative mb-25px"> 
                            <div class="process-step-icon d-flex justify-content-center align-items-center mx-auto rounded-circle h-90px w-90px fs-28 bg-base-color text-dark-gray alt-font">
                                <span class="number position-relative z-index-1">02</span>
                                <div class="box-overlay bg-white rounded-circle"></div>
                            </div>
                        </div>
                        <span class="d-inline-block fw-500 text-white fs-18">Lutte pour l'Excellence</span>
                        <p class="w-85 d-inline-block text-white opacity-4">Projets bien planifiés, suivis, avec des partenaires engagés.</p>
                    </div>
                    <div class="col text-center last-paragraph-no-margin hover-box process-step-style-09">
                        <div class="process-step-icon-box position-relative mb-25px"> 
                            <div class="process-step-icon d-flex justify-content-center align-items-center mx-auto rounded-circle h-90px w-90px fs-28 bg-base-color text-dark-gray alt-font">
                                <span class="number position-relative z-index-1">03</span>
                                <div class="box-overlay bg-white rounded-circle"></div>
                            </div> 
                        </div>
                        <span class="d-inline-block fw-500 text-white fs-18">Intégrité et Transparence</span>
                        <p class="w-85 d-inline-block text-white opacity-4">Respect, transparence des fonds, rejet des pratiques illicites.</p>
                    </div>
                </div>
            </div>
        </section>

        <section class="position-relative overlap-height">
            <div class="container overlap-gap-section">
                <div class="row g-0 border-radius-4px mb-7 overflow-hidden sm-mb-60px">
                    <div class="col-lg-6 col-md-7 p-8 lg-p-4 sm-p-25px background-position-left-top position-relative text-center text-md-start" style="background-image: url('images/demo-charity-home-bg-06.jpg')">
                        <h3 class="alt-font text-dark-gray w-95 xl-w-100 mb-20px">Rejoins-nous</h3>
                        <p class="text-dark-gray opacity-8 w-95 lg-w-100 mb-30px">Contactez ProGen Bénin pour soutenir nos projets, vous engager ou en savoir plus sur nos actions.</p>
                        <a href="demo-charity-contact.html" class="btn btn-large btn-round-edge with-rounded btn-gradient-green-goldenrod-yellow">Nous contacter<span class="bg-white"><i class="fa-solid fa-arrow-right text-dark-golden-yellow"></i></span></a>
                    </div>
                    <div class="col-lg-6 col-md-5 cover-background position-relative sm-h-350px" style="background-image: url('images/progen/join.jpg')"> 
                    </div>
                </div>
                <div class="row justify-content-center mb-3 sm-mb-30px">
                    <div class="col-xxl-6 col-xl-7 text-center last-paragraph-no-margin" data-anime='{ "el": "childs", "translateY": [30, 0], "opacity": [0,1], "duration": 600, "delay": 0, "staggervalue": 200, "easing": "easeOutQuad" }'>
                        <h3 class="alt-font text-dark-gray mb-10px">Actualités</h3>
                        <p class="w-80 mx-auto sm-w-100">Les dernières actions de ProGen Bénin sur le terrain.</p>
                    </div>
                </div>
                <div class="row justify-content-center mb-5">
                    <div class="col-lg-10">
                        <div class="blog-box d-sm-flex d-block flex-row h-100 border-radius-6px overflow-hidden box-shadow-extra-large">
                            <div class="blog-image w-50 xs-w-100 cover-background" style="background-image: url('images/progen/blog-1.jpg')">
                                <a href="demo-charity-blog-single-simple.html" class="blog-post-image-overlay"></a>
                            </div>
                            <div class="blog-content w-50 xs-w-100 pt-50px pb-40px ps-40px pe-40px bg-white d-flex flex-column justify-content-center align-items-start last-paragraph-no-margin">
                                <span class="btn btn-very-small btn-rounded btn-gradient-green-goldenrod-yellow ls-0px mb-30px">26/01/2020 · Santé</span>
                                <a href="demo-charity-blog-single-simple.html" class="card-title text-dark-gray text-dark-gray-hover fw-500 mb-10px fs-22 alt-font">Sensibilisation à l'hygiène menstruelle</a>
                                <p>Contact avec les élèves ressortissants de Sonri (commune de Nikki) pour partager des informations sur l'hygiène menstruelle en milieu scolaire.</p>
                                <a href="demo-charity-stories.html" class="btn btn-link btn-hover-animation-switch btn-large text-dark-gray mt-20px">
                                    <span><span class="btn-text">Toutes les actualités</span><span class="btn-icon"><i class="fa-solid fa-arrow-right"></i></span><span class="btn-icon"><i class="fa-solid fa-arrow-right"></i></span></span>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
'''

# ---------- ABOUT ----------
about_body = page_title("À propos", "Prochaine Génération Bénin", "images/progen/about-16-1.jpg") + r'''
        <section class="lg-pt-20px xs-pt-0">
            <div class="container">
                <div class="row align-items-center justify-content-center"> 
                    <div class="col-xl-7 col-lg-6 position-relative md-mb-12 xs-mb-30px">
                        <div class="row align-items-center position-relative" data-anime='{ "el": "childs", "translateY": [0, 0], "opacity": [0,1], "duration": 1500, "delay": 100, "staggervalue": 200, "easing": "easeOutQuad" }'>
                            <div class="col-sm-5 text-end xs-mb-30px">
                                <img class="xs-w-100 border-radius-6px" src="images/progen/about-2.jpg" alt="ProGen Bénin" />
                            </div>
                            <div class="col-sm-7 xs-mb-30px">
                                <img src="images/progen/about-16-1.jpg" alt="Actions ProGen" class="w-95 border-radius-6px md-w-100 bottom-30px xs-bottom-0px position-relative" />
                            </div>
                            <div class="w-40 xs-w-100 overflow-hidden position-absolute xs-position-relative left-150px lg-left-110px bottom-minus-10px lg-bottom-minus-40px xs-bottom-0px xs-left-0px">
                                <img src="images/progen/ozg-6-1.jpg" alt="Sensibilisation" class="border-radius-6px sm-w-100" />
                            </div>
                        </div> 
                    </div> 
                    <div class="col-xl-5 col-lg-6 ps-6 xl-ps-3 md-ps-15px" data-anime='{ "el": "childs", "translateY": [50, 0], "opacity": [0,1], "duration": 600, "delay": 0, "staggervalue": 200, "easing": "easeOutQuad" }'>
                        <h3 class="alt-font text-dark-gray">Qui sommes-nous ?</h3> 
                        <p class="mb-20px">Prochaine Génération Bénin (ProGen Bénin) est une ONG à but non lucratif enregistrée sous le n°2017|1909|DEP-LIT/SG/SAG-Assoc du 12 avril 2017, publiée au Journal officiel du 15 juin 2017.</p>
                        <p class="mb-20px">Elle intervient dans les domaines de l'<strong>éducation</strong>, de la <strong>santé</strong> et des <strong>droits humains</strong>, auprès des enfants, des femmes et des associations de parents d'élèves.</p>
                        <div class="pt-15px pb-15px ps-30px pe-30px xs-p-15px bg-white box-shadow-quadruple-large border-radius-6px border border-color-extra-medium-gray mb-20px icon-with-text-style-08">
                            <div class="feature-box feature-box-left-icon-middle">
                                <div class="feature-box-icon me-10px">
                                    <i class="bi bi-geo-alt fs-22 text-dark-golden-yellow"></i>
                                </div>
                                <div class="feature-box-content">
                                    <span class="alt-font text-dark-gray">Littoral, Atlantique, Borgou, Alibori</span>
                                </div>
                            </div>
                        </div>
                    </div> 
                </div> 
            </div>
        </section>

        <section class="background-position-left-top position-relative" style="background-image: url('images/demo-charity-home-bg-01.jpg')">
            <div class="position-absolute left-0px top-minus-50px md-top-minus-40px sm-top-minus-20px xs-top-minus-19px background-position-left-top w-100 h-100px lg-h-50px background-size-100 background-no-repeat" style="background-image: url('images/demo-charity-home-bg-02.jpg')"></div>
            <div class="container">
                <div class="row justify-content-center mb-5">
                    <div class="col-lg-10 text-center last-paragraph-no-margin">
                        <h3 class="alt-font text-dark-gray mb-15px">Mission</h3>
                        <p class="fs-18">Protéger les droits des enfants et des femmes ; procurer aux enfants démunis une éducation de qualité dans un cadre positif.</p>
                    </div>
                </div>
                <div class="row row-cols-1 row-cols-md-2 g-4 mb-5">
                    <div class="col">
                        <div class="bg-white p-40px border-radius-6px box-shadow-quadruple-large h-100">
                            <h5 class="alt-font text-dark-gray">Axes d'intervention</h5>
                            <ul class="list-style-02 ps-0">
                                <li class="pb-10px">Éducation formelle des enfants et adolescents</li>
                                <li class="pb-10px">Santé sexuelle et de la reproduction en milieu scolaire</li>
                                <li class="pb-10px">Formation professionnelle des filles déscolarisées</li>
                                <li>Appui et renforcement des capacités des femmes</li>
                            </ul>
                        </div>
                    </div>
                    <div class="col">
                        <div class="bg-white p-40px border-radius-6px box-shadow-quadruple-large h-100">
                            <h5 class="alt-font text-dark-gray">Objectifs en éducation</h5>
                            <ul class="list-style-02 ps-0">
                                <li class="pb-10px">Améliorer les conditions d'études</li>
                                <li class="pb-10px">Mobiliser les ressources des communautés et des écoles</li>
                                <li>Garantir un accès équitable sans distinction de religion, d'ethnie ou de genre</li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="row justify-content-center mb-3">
                    <div class="col-lg-8 text-center">
                        <h3 class="alt-font text-dark-gray mb-30px">Nos valeurs</h3>
                    </div>
                </div>
                <div class="row row-cols-1 row-cols-lg-3 justify-content-center mb-5">
                    <div class="col mb-30px">
                        <div class="border border-color-extra-medium-gray border-radius-6px p-35px h-100 text-center">
                            <h6 class="alt-font text-dark-gray">Dévouement et Égalité</h6>
                            <p class="mb-0">Servir sans distinction d'âge, de sexe, de religion ou d'origine.</p>
                        </div>
                    </div>
                    <div class="col mb-30px">
                        <div class="border border-color-extra-medium-gray border-radius-6px p-35px h-100 text-center">
                            <h6 class="alt-font text-dark-gray">Lutte pour l'Excellence</h6>
                            <p class="mb-0">Projets bien planifiés, suivi rigoureux et partenariats solides.</p>
                        </div>
                    </div>
                    <div class="col mb-30px">
                        <div class="border border-color-extra-medium-gray border-radius-6px p-35px h-100 text-center">
                            <h6 class="alt-font text-dark-gray">Intégrité et Transparence</h6>
                            <p class="mb-0">Respect, transparence des fonds et rejet des pratiques illicites.</p>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-12 text-center">
                        <div class="fs-15 text-uppercase text-dark-gray fw-600">Découvrez nos actions. <a href="demo-charity-causes.html" class="text-decoration-line-bottom text-dark-gray fw-700">Voir les projets</a></div>
                    </div>
                </div>
            </div>
        </section>
'''

# ---------- CAUSES ----------
causes_projects = [
    ("ozg", "Objectif Zéro Grossesse", "Santé scolaire", "images/progen/ozg-8.jpg",
     "Campagnes de sensibilisation des adolescentes en milieu scolaire sur les causes, risques, conséquences et la prévention des grossesses précoces.",
     "Selon le Ministère de l'Enseignement, 2&nbsp;732 cas de grossesses ont été recensés durant l'année scolaire 2016-2017. Le projet vise une extension aux départements les plus touchés."),
    ("ef", "Excellence Féminine", "Bourses", "images/progen/ef-14.jpg",
     "Bourses destinées aux élèves filles excellentes des écoles primaires du Borgou, de l'Alibori et de l'Atacora.",
     "Chaque bourse couvre une année scolaire complète (fournitures et scolarité) pour soutenir la poursuite des études."),
    ("gas", "Give a Smile", "Parrainage", "images/progen/gas-11.jpg",
     "Parrainage des besoins scolaires (fournitures, scolarité, maîtres d'études) pour les enfants en situations difficiles — orphelins, enfants placés, etc.",
     "Interventions dans les écoles du Borgou, de l'Alibori et de l'Atacora."),
    ("ms", "Millennium School", "Infrastructures scolaires", "images/progen/ms-sonri.jpg",
     "Améliorer les conditions de vie des élèves en mobilisant livres, manuels, tableaux et lampes solaires.",
     "1<sup>re</sup> édition du 11 octobre 2019 : kits et matériels pour l'EPP SONRI (à 5 km de Nikki), ainsi que la construction d'un puits d'eau pour le village."),
    ("ee", "Enfance Épanouie", "Éveil", "images/progen/ee-15-1.jpg",
     "« Enfance Épanouie » permet aux enfants de développer leurs compétences sociales, intellectuelles et linguistiques à travers les jeux. Les enfants découvrent le monde, le plaisir et l'échange, indispensables à leur épanouissement.",
     "Le projet met à disposition des écoles maternelles publiques des milieux ruraux des jouets via des dons en nature ou financiers. Édition 2018 : don d'une aire de jeux à la maternelle de l'EPP de Savi Djègo (commune de Ouidah). Édition 2019 : don de jouets éducatifs (puzzles, jeux de lettres et chiffres, constructions, ballons, cahiers et crayons de coloriage, voitures, poupées, etc.) pour stimuler la créativité et l'interaction."),
]

causes_body = page_title("Nos projets", "Éducation, santé et épanouissement des enfants", "images/progen/ozg-8.jpg")
causes_body += '''
        <section class="background-position-left-top background-no-repeat-y background-size-auto-100 pt-5 md-pt-0" style="background-image: url('images/demo-charity-causes-bg.jpg')">
            <div class="container">
'''
for slug, title, tag, img, p1, p2 in causes_projects:
    causes_body += f'''
                <div class="row align-items-center mb-7 sm-mb-50px" id="{slug}">
                    <div class="col-lg-5 md-mb-30px">
                        <img src="{img}" alt="{title}" class="border-radius-6px w-100 box-shadow-quadruple-large">
                    </div>
                    <div class="col-lg-6 offset-lg-1">
                        <span class="btn btn-very-small btn-rounded btn-base-color text-dark-gray btn-box-shadow mb-20px">{tag}</span>
                        <h3 class="alt-font text-dark-gray mb-20px">{title}</h3>
                        <p>{p1}</p>
                        <p class="mb-0">{p2}</p>
                    </div>
                </div>
'''
causes_body += '''
                <div class="row mb-5">
                    <div class="col-12 text-center">
                        <a href="demo-charity-contact.html#don" class="btn btn-large btn-round-edge with-rounded btn-gradient-green-goldenrod-yellow btn-box-shadow">Soutenir un projet<span class="bg-white"><i class="fa-solid fa-arrow-right text-dark-golden-yellow"></i></span></a>
                    </div>
                </div>
            </div>
        </section>
'''

# ---------- TEAM ----------
team_body = page_title("Notre équipe", "Les personnes derrière ProGen Bénin", "images/progen/team-ghislaine.jpg") + r'''
        <section class="background-position-left-top position-relative" style="background-image: url('images/demo-charity-home-bg-01.jpg')">
            <div class="position-absolute left-0px top-minus-70px xl-top-minus-50px lg-top-minus-30px sm-top-minus-20px xs-top-minus-15px background-position-left-top w-100 h-100px lg-h-50px background-size-100 background-no-repeat" style="background-image: url('images/demo-charity-home-bg-02.jpg')"></div>
            <div class="container">
                <div class="row justify-content-center mb-5">
                    <div class="col-lg-8 text-center">
                        <h3 class="alt-font text-dark-gray mb-10px">Direction</h3>
                        <p>L'équipe engagée pour la prochaine génération du Bénin.</p>
                    </div>
                </div>
                <div class="row justify-content-center mb-6">
                    <div class="col-lg-10">
                        <div class="row align-items-center g-0 border-radius-6px overflow-hidden box-shadow-quadruple-large bg-white">
                            <div class="col-md-5">
                                <img src="images/progen/team-ghislaine.jpg" alt="Ghislaine Akakpo" class="w-100">
                            </div>
                            <div class="col-md-7 p-50px lg-p-30px">
                                <h4 class="alt-font text-dark-gray mb-5px">Ghislaine Akakpo</h4>
                                <span class="d-block text-dark-golden-yellow fw-600 mb-20px">Présidente et fondatrice</span>
                                <p>Née à Parakou, dans une famille polygame pauvre. Titulaire du Bac G2, d'une Maîtrise en Droit des Affaires (Université de Parakou) et d'une Attestation de Leadership Civique (CESAG Dakar).</p>
                                <p class="mb-0">Fondatrice de ProGen Bénin. Passionnée par les questions sociales, les voyages, les cultures et la musique.</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row justify-content-center mb-5">
                    <div class="col-md-5 col-sm-8 text-center">
                        <div class="border border-color-extra-medium-gray border-radius-6px p-40px box-shadow-quadruple-large bg-white">
                            <div class="w-100px h-100px rounded-circle bg-gradient-corduroy-green-dark-goldenrod d-flex align-items-center justify-content-center mx-auto mb-25px">
                                <i class="bi bi-person fs-40 text-white"></i>
                            </div>
                            <div class="fs-20 lh-26 fw-500 text-dark-gray alt-font">Lucien Kploca</div>
                            <span class="fs-17">Trésorier</span>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-12 text-center">
                        <p class="mb-20px">Vous souhaitez collaborer avec ProGen Bénin ?</p>
                        <a href="demo-charity-contact.html" class="btn btn-large btn-round-edge with-rounded btn-gradient-green-goldenrod-yellow">Nous contacter<span class="bg-white"><i class="fa-solid fa-arrow-right text-dark-golden-yellow"></i></span></a>
                    </div>
                </div>
            </div>
        </section>
'''

# ---------- STORIES ----------
stories_body = page_title("Actualités", "Les actions de ProGen Bénin", "images/progen/blog-2.jpg") + r'''
        <section class="background-position-left-top background-no-repeat-y background-size-auto-100 pt-50px lg-pt-30px md-pt-0" style="background-image: url('images/demo-charity-causes-bg.jpg')">
            <div class="container">   
                <div class="row mb-5 justify-content-center">
                    <div class="col-lg-10">
                        <div class="blog-box d-md-flex d-block flex-row h-100 border-radius-4px overflow-hidden box-shadow-extra-large">
                            <div class="blog-image w-50 sm-w-100 cover-background" style="background-image: url('images/progen/blog-1.jpg')">
                                <a href="demo-charity-blog-single-simple.html" class="blog-post-image-overlay"></a>
                            </div>
                            <div class="blog-content w-50 sm-w-100 pt-50px pb-40px ps-40px pe-40px xl-p-30px bg-white d-flex flex-column justify-content-center align-items-start last-paragraph-no-margin">
                                <span class="btn btn-very-small btn-rounded btn-gradient-green-goldenrod-yellow ls-0px mb-30px">26/01/2020 · Santé</span>
                                <a href="demo-charity-blog-single-simple.html" class="card-title text-dark-gray text-dark-gray-hover fw-500 mb-10px fs-22 alt-font">Sensibilisation à l'hygiène menstruelle</a>
                                <p>Contact avec les élèves ressortissants de Sonri (commune de Nikki). Partage d'informations sur l'hygiène menstruelle en milieu scolaire.</p>
                                <a href="demo-charity-blog-single-simple.html" class="btn btn-link btn-hover-animation-switch btn-large text-dark-gray mt-15px">
                                    <span><span class="btn-text">Lire l'article</span><span class="btn-icon"><i class="fa-solid fa-arrow-right"></i></span><span class="btn-icon"><i class="fa-solid fa-arrow-right"></i></span></span>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row row-cols-1 row-cols-md-3 g-4 mb-5">
                    <div class="col">
                        <div class="border-radius-4px overflow-hidden box-shadow-extra-large bg-white h-100">
                            <img src="images/progen/blog-2.jpg" alt="Hygiène menstruelle" class="w-100">
                            <div class="p-25px last-paragraph-no-margin">
                                <span class="fs-14 text-dark-golden-yellow fw-600">26/01/2020</span>
                                <p class="text-dark-gray fw-500 mt-5px mb-0">Sensibilisation — session à Sonri</p>
                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="border-radius-4px overflow-hidden box-shadow-extra-large bg-white h-100">
                            <img src="images/progen/blog-3.jpg" alt="Milieu scolaire" class="w-100">
                            <div class="p-25px last-paragraph-no-margin">
                                <span class="fs-14 text-dark-golden-yellow fw-600">26/01/2020</span>
                                <p class="text-dark-gray fw-500 mt-5px mb-0">Échanges avec les élèves</p>
                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="border-radius-4px overflow-hidden box-shadow-extra-large bg-white h-100">
                            <img src="images/progen/blog-4.jpg" alt="Nikki" class="w-100">
                            <div class="p-25px last-paragraph-no-margin">
                                <span class="fs-14 text-dark-golden-yellow fw-600">26/01/2020</span>
                                <p class="text-dark-gray fw-500 mt-5px mb-0">Commune de Nikki</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
'''

# ---------- GALLERY ----------
gallery_images = [
    ("images/progen/ozg-7-2.jpg", "Objectif Zéro Grossesse"),
    ("images/progen/ozg-6-1.jpg", "Sensibilisation scolaire"),
    ("images/progen/ozg-8.jpg", "Campagne OZG"),
    ("images/progen/ef-13.jpg", "Excellence Féminine"),
    ("images/progen/ef-14.jpg", "Bourses filles"),
    ("images/progen/ef-12-1.jpg", "Élèves boursières"),
    ("images/progen/gas-11.jpg", "Give a Smile"),
    ("images/progen/gas-9-1.jpg", "Parrainage scolaire"),
    ("images/progen/gas-9-2.jpg", "Fournitures scolaires"),
    ("images/progen/ms-sonri.jpg", "Millennium School — SONRI"),
    ("images/progen/ee-15-1.jpg", "Enfance Épanouie"),
    ("images/progen/ee-16.jpg", "Aire de jeux"),
    ("images/progen/ee-17.jpg", "Jouets éducatifs"),
    ("images/progen/about-16-1.jpg", "Actions ProGen"),
    ("images/progen/about-2.jpg", "Terrain"),
    ("images/progen/join.jpg", "Engagement"),
    ("images/progen/blog-1.jpg", "Hygiène menstruelle"),
    ("images/progen/blog-2.jpg", "Actualité Sonri"),
]

gallery_body = page_title("Galerie", "Moments de nos projets sur le terrain", "images/progen/gas-9-2.jpg")
gallery_body += '''
        <section class="background-position-left-top background-no-repeat-y background-size-auto-100 pt-5 md-pt-0" style="background-image: url('images/demo-charity-causes-bg.jpg')">
            <div class="container">  
                <div class="row mb-60px md-mb-40px">
                    <div class="col">
                        <ul class="image-gallery-style-02 gallery-wrapper grid-loading grid grid-3col xxl-grid-3col xl-grid-3col lg-grid-3col md-grid-2col sm-grid-2col xs-grid-1col gutter-extra-large" data-anime='{ "el": "childs", "translateY": [30, 0], "opacity": [0,1], "duration": 600, "delay":0, "staggervalue": 200, "easing": "easeOutQuad" }'>
                            <li class="grid-sizer"></li>
'''
for src, title in gallery_images:
    gallery_body += f'''
                            <li class="grid-item transition-inner-all z-index-1">
                                <div class="atropos" data-atropos data-atropos-perspective="1150">
                                    <div class="atropos-scale">
                                        <div class="atropos-rotate">
                                            <div class="atropos-inner" data-atropos-offset="3"> 
                                                <div class="gallery-box">
                                                    <a href="{src}" data-group="lightbox-group-gallery-item-2" title="{title}">
                                                        <div class="position-relative gallery-image bg-dark-gray border-radius-6px overflow-hidden">
                                                            <img src="{src}" alt="{title}" />
                                                            <div class="d-flex align-items-center justify-content-center position-absolute top-0px left-0px w-100 h-100 gallery-hover move-bottom-top">
                                                                <i class="bi bi-camera icon-medium text-white"></i>
                                                            </div>
                                                        </div>
                                                    </a>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </li>
'''
gallery_body += '''
                        </ul>
                    </div>
                </div>
            </div>
        </section>
'''

# ---------- CONTACT ----------
contact_body = page_title("Contact", "Écrivons-nous ou appelons-nous", "images/progen/join.jpg") + r'''
        <section class="position-relative z-index-1 pt-50px lg-pt-30px md-pt-0 pb-0" id="don">
            <div class="container">
                <div class="row justify-content-center"> 
                    <div class="col-lg-5 pb-5 sm-pb-50px" data-anime='{"el": "childs", "translateY": [50, 0], "opacity": [0,1], "duration": 600, "delay": 0, "staggervalue": 200, "easing": "easeOutQuad" }'> 
                        <span class="fs-15 fw-600 ls-05px text-uppercase text-dark-golden-yellow d-block mb-10px">Restons en contact</span>
                        <h3 class="alt-font text-dark-gray">Une question, un don, un partenariat ?</h3>
                        <p class="mb-30px">Cette page est une démonstration. Pour joindre ProGen Bénin, utilisez les coordonnées ci-dessous.</p>
                        <div class="mt-4 w-90 lg-w-100" data-anime='{"el": "childs", "translateY": [50, 0], "opacity": [0,1], "duration": 600, "delay": 0, "staggervalue": 200, "easing": "easeOutQuad" }'>
                            <div class="col icon-with-text-style-08 mb-25px">
                                <div class="feature-box feature-box-left-icon-middle border-bottom pb-25px border-color-extra-medium-gray">
                                    <div class="feature-box-icon me-20px">
                                        <i class="bi bi-telephone-outbound icon-medium text-dark-gray"></i> 
                                    </div>
                                    <div class="feature-box-content">
                                        <span>Téléphones</span>
                                        <span class="d-block fw-500 fs-18"><a href="tel:+22969740000" class="text-dark-gray text-dark-gray-hover">+229 69 74 00 00</a></span>
                                        <span class="d-block fw-500 fs-18"><a href="tel:+22994440303" class="text-dark-gray text-dark-gray-hover">+229 94 44 03 03</a></span>
                                    </div>
                                </div>
                            </div>
                            <div class="col icon-with-text-style-08">
                                <div class="feature-box feature-box-left-icon-middle">
                                    <div class="feature-box-icon me-20px">
                                        <i class="bi bi-envelope icon-medium text-dark-gray"></i> 
                                    </div>
                                    <div class="feature-box-content">
                                        <span>E-mail</span>
                                        <span class="d-block fw-500 fs-19"><a href="mailto:contact@progenbenin.org" class="text-dark-gray text-dark-gray-hover">contact@progenbenin.org</a></span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-6 offset-lg-1 align-self-end contact-form-style-03" data-anime='{ "opacity": [0,1], "duration": 600, "delay": 0, "staggervalue": 200, "easing": "easeOutQuad" }'> 
                        <div class="bg-dark-gray box-shadow-double-large p-14 lg-p-10 border-radius-10px position-relative overflow-hidden">
                            <h3 class="alt-font text-white">Envoyez un message</h3>
                            <p class="text-white opacity-6 mb-30px">Formulaire démo — sans envoi backend.</p>
                            <form action="email-templates/contact-form.php" method="post">
                                <div class="position-relative form-group mb-20px">
                                    <span class="form-icon text-white opacity-7"><i class="bi bi-emoji-smile"></i></span>
                                    <input class="ps-0 border-radius-0px bg-transparent placeholder-light border-color-transparent-white-light fs-17 form-control required" type="text" name="name" placeholder="Votre nom*" />
                                </div>
                                <div class="position-relative form-group mb-20px">
                                    <span class="form-icon text-white opacity-7"><i class="bi bi-envelope"></i></span>
                                    <input class="ps-0 border-radius-0px bg-transparent placeholder-light border-color-transparent-white-light fs-17 form-control required" type="email" name="email" placeholder="Votre e-mail*" />
                                </div>
                                <div class="position-relative form-group mb-20px">
                                    <span class="form-icon text-white opacity-7"><i class="bi bi-telephone"></i></span>
                                    <input class="ps-0 border-radius-0px bg-transparent placeholder-light border-color-transparent-white-light fs-17 form-control" type="tel" name="phone" placeholder="Votre téléphone" />
                                </div>
                                <div class="position-relative form-group form-textarea mt-15px mb-0"> 
                                    <textarea class="ps-0 border-radius-0px bg-transparent placeholder-light border-color-transparent-white-light fs-17 form-control" name="comment" placeholder="Votre message" rows="4"></textarea>
                                    <span class="form-icon text-white opacity-7"><i class="bi bi-chat-square-dots"></i></span>
                                    <input type="hidden" name="redirect" value="">
                                    <button class="btn btn-base-color btn-medium btn-box-shadow btn-round-edge w-100 mt-30px submit" type="submit">Envoyer</button>
                                    <div class="form-results mt-20px d-none"></div>
                                </div>
                            </form> 
                        </div>
                    </div>
                </div> 
            </div>
        </section>
        <section class="pt-0 pb-0">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-12"><div class="separator-line-1px bg-extra-medium-gray mt-0 mb-0"></div></div>
                </div>
            </div>
        </section>
'''

# ---------- BLOG SINGLE ----------
blog_body = page_title("Actualité", "26 janvier 2020", "images/progen/blog-1.jpg") + r'''
        <section>
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-lg-8 last-paragraph-no-margin" data-anime='{ "el": "childs", "translateY": [30, 0], "opacity": [0,1], "duration": 600, "delay": 0, "staggervalue": 200, "easing": "easeOutQuad" }'>
                        <span class="btn btn-very-small btn-rounded btn-gradient-green-goldenrod-yellow ls-0px mb-25px">Santé · Nikki</span>
                        <h3 class="alt-font text-dark-gray mb-20px">Sensibilisation à l'hygiène menstruelle</h3>
                        <p class="fs-18 mb-30px">Le 26 janvier 2020, ProGen Bénin a organisé un contact avec les élèves ressortissants de Sonri, dans la commune de Nikki, afin de partager des informations sur l'hygiène menstruelle en milieu scolaire.</p>
                        <img src="images/progen/blog-1.jpg" alt="Sensibilisation hygiène menstruelle" class="w-100 border-radius-6px mb-30px">
                        <p class="mb-30px">Cette action s'inscrit dans l'engagement de l'ONG pour la santé des adolescentes et la prévention en milieu scolaire, en lien avec ses axes d'intervention en santé sexuelle et de la reproduction.</p>
                        <div class="row g-3 mb-40px">
                            <div class="col-sm-4"><img src="images/progen/blog-2.jpg" alt="" class="w-100 border-radius-4px"></div>
                            <div class="col-sm-4"><img src="images/progen/blog-3.jpg" alt="" class="w-100 border-radius-4px"></div>
                            <div class="col-sm-4"><img src="images/progen/blog-4.jpg" alt="" class="w-100 border-radius-4px"></div>
                        </div>
                        <a href="demo-charity-stories.html" class="btn btn-link btn-hover-animation-switch btn-large text-dark-gray">
                            <span><span class="btn-text">Retour aux actualités</span><span class="btn-icon"><i class="fa-solid fa-arrow-right"></i></span><span class="btn-icon"><i class="fa-solid fa-arrow-right"></i></span></span>
                        </a>
                    </div>
                </div>
            </div>
        </section>
'''

pages = {
    "index.html": wrap(
        "ProGen Bénin — Prochaine Génération",
        "ProGen Bénin (Prochaine Génération) — ONG pour l'éducation, la santé et les droits humains des enfants et des femmes au Bénin.",
        "home", index_body),
    "demo-charity-about.html": wrap(
        "À propos — ProGen Bénin",
        "Qui sommes-nous : mission, valeurs et axes d'intervention de ProGen Bénin.",
        "about", about_body),
    "demo-charity-causes.html": wrap(
        "Projets — ProGen Bénin",
        "Les 5 projets de ProGen Bénin : Objectif Zéro Grossesse, Excellence Féminine, Give a Smile, Millennium School, Enfance Épanouie.",
        "causes", causes_body),
    "demo-charity-volunteer.html": wrap(
        "Équipe — ProGen Bénin",
        "L'équipe de ProGen Bénin : Ghislaine Akakpo, présidente et fondatrice ; Lucien Kploca, trésorier.",
        "team", team_body),
    "demo-charity-stories.html": wrap(
        "Actualités — ProGen Bénin",
        "Actualités et actions de ProGen Bénin sur le terrain.",
        "news", stories_body),
    "demo-charity-gallery.html": wrap(
        "Galerie — ProGen Bénin",
        "Galerie photo des projets ProGen Bénin.",
        "gallery", gallery_body),
    "demo-charity-contact.html": wrap(
        "Contact — ProGen Bénin",
        "Contacter ProGen Bénin : contact@progenbenin.org, +229 69 74 00 00, +229 94 44 03 03.",
        "contact", contact_body),
    "demo-charity-blog-single-simple.html": wrap(
        "Sensibilisation hygiène menstruelle — ProGen Bénin",
        "Sensibilisation à l'hygiène menstruelle — 26/01/2020 — Sonri, commune de Nikki.",
        "news", blog_body),
}

for name, html in pages.items():
    path = ROOT / name
    path.write_text(html, encoding="utf-8")
    print(f"Wrote {name} ({len(html)} chars)")

print("Done.")
