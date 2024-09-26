1. Sécurité liée aux Cookies
SESSION_COOKIE_SECURE:
Explication : Lorsqu'activé (True), cela force les cookies de session à être envoyés uniquement via HTTPS, ce qui empêche leur interception.
Preuve pour l'équipe de sécurité : Montre que ce paramètre est activé dans l'environnement de production.
CSRF_COOKIE_SECURE:
Explication : Semblable au précédent, mais concerne le cookie CSRF, qui protège contre les attaques de type Cross-Site Request Forgery (CSRF).
Preuve : Affiche que ce paramètre est activé dans l'environnement de production.
2. Protection contre les attaques XSS (Cross-Site Scripting)
SECURE_BROWSER_XSS_FILTER :
Explication : Ce paramètre demande au navigateur d'activer son filtre XSS, empêchant ainsi certaines attaques XSS.
Preuve : Activer ce paramètre en production, et montrer que les entêtes HTTP du navigateur incluent X-XSS-Protection.
X_FRAME_OPTIONS = "SAMEORIGIN" :
Explication : Empêche l'application d'être chargée dans une iframe sur un site externe, réduisant le risque d'attaques de type clickjacking.
Preuve : Analyser les entêtes HTTP pour vérifier la présence de X-Frame-Options: SAMEORIGIN.
3. Sécurisation des en-têtes HTTP
SECURE_CONTENT_TYPE_NOSNIFF :
Explication : Empêche le navigateur de deviner le type de contenu, protégeant contre certaines attaques liées à la manipulation des types MIME.
Preuve : En production, vérifie que l'en-tête HTTP X-Content-Type-Options: nosniff est envoyé.
4. Sécurisation de la connexion via HTTPS
SECURE_SSL_REDIRECT :
Explication : Redirige tout le trafic HTTP vers HTTPS, garantissant que toutes les communications sont chiffrées.
Preuve : Montrer que cette redirection fonctionne en forçant une requête HTTP sur l'application.
SECURE_PROXY_SSL_HEADER :
Explication : Indique à Django qu'il est derrière un proxy SSL, garantissant que les requêtes sont traitées en HTTPS.
Preuve : Vérifie que l'application reçoit bien les requêtes via HTTPS derrière un proxy.
5. Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 31536000 :
Explication : Active la politique HTTP Strict Transport Security (HSTS) pendant 1 an. Cela force les navigateurs à toujours utiliser HTTPS pour accéder à l'application.
Preuve : Analyser les en-têtes HTTP pour vérifier la présence de Strict-Transport-Security: max-age=31536000; includeSubDomains; preload.
SECURE_HSTS_INCLUDE_SUBDOMAINS = True :
Explication : Applique HSTS à tous les sous-domaines.
Preuve : Affiche l'en-tête HSTS dans les réponses HTTP pour les sous-domaines.
SECURE_HSTS_PRELOAD = True :
Explication : Indique aux navigateurs de précharger HSTS, assurant ainsi que les utilisateurs ne visitent jamais le site via HTTP.
Preuve : Montre que l'application figure dans la liste de préchargement HSTS ou prépare son inclusion.
6. Protection CSRF (Cross-Site Request Forgery)
CSRF_COOKIE_SECURE :
Explication : Garantit que les cookies CSRF ne sont envoyés que via HTTPS.
Preuve : Analysez la configuration du CSRF et montrez que l'authentification des requêtes est effectuée correctement.
CSRF_TRUSTED_ORIGINS :
Explication : Limite les origines de confiance pour les requêtes CSRF à celles spécifiées.
Preuve : Montre les domaines configurés dans cette liste.
7. Clés secrètes et variables sensibles
Utilisation de django-environ pour les variables d'environnement :
Explication : Les informations sensibles comme la clé secrète (SECRET_KEY), les informations de base de données, et autres paramètres de sécurité sont stockées dans un fichier .env, qui n'est pas versionné.
Preuve : Montre à l'équipe que ces informations sont bien absentes du dépôt de code source et uniquement accessibles via des environnements sécurisés.
8. Mise en place de Whitenoise
whitenoise.middleware.WhiteNoiseMiddleware :
Explication : Cette middleware sert les fichiers statiques directement, et elle supporte la compression des fichiers pour les servir de manière plus efficace.
Preuve : Montre que les fichiers sont servis de manière sécurisée via cette middleware.
