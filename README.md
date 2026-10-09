# ProGen Bénin — démo site

Proposition GUELICHWEB. Contenu sourcé depuis [progenbenin.org](https://progenbenin.org/).

## Déploiement Netlify

Le site est à la **racine** du dépôt (`index.html`).

1. Connecter ce repo à Netlify
2. Build command : *(vide)*
3. Publish directory : `.` (ou laisser Netlify lire `netlify.toml`)

## Pages

| Fichier | Page |
|---------|------|
| `index.html` | Accueil |
| `demo-charity-about.html` | À propos |
| `demo-charity-causes.html` | Projets |
| `demo-charity-gallery.html` | Galerie |
| `demo-charity-volunteer.html` | Équipe |
| `demo-charity-stories.html` | Actualités |
| `demo-charity-contact.html` | Contact + « Comment nous soutenir » (`#don`) |
| `demo-charity-blog-single-simple.html` | Article |
| `merci.html` | Confirmation d'envoi du formulaire |
| `404.html` | Page introuvable |

Aperçu local : ouvrir `index.html` ou servir la racine (`npx serve .`).

Les fichiers de travail / anciennes démos sont dans `_archive/` (non exposés via Netlify).

## Génération des pages

Les pages HTML sont **générées** par `_build_progen.py` : modifier le script, puis lancer `python3 _build_progen.py` (ne pas éditer les HTML à la main, ils seraient écrasés). Les styles propres à ProGen sont à la fin de `demos/charity/charity.css` (préfixe `pg-`).

## Formulaire de contact

Le formulaire utilise **Netlify Forms** (`data-netlify`) : les messages arrivent dans Netlify → Forms (notifications e-mail configurables à cet endroit). Aucun back-end à maintenir.

## Démo non indexée

Les pages portent `<meta name="robots" content="noindex, nofollow">` : la démo ne doit pas concurrencer le site officiel dans les moteurs de recherche. Retirer cette ligne dans `HEAD` (`_build_progen.py`) pour la version de production.
