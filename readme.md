# Drone web site
Ce repo contient le code source de la base du siteweb drone-photovideo.fr

Ce site web est fait pour pouvoir être déployé sur des sous-domaines facilemenent en gardant le squelette principal commun, seul le dossier custom contiendra les specificités 

## dossier custom
- un dossier static pour les assets
- un fichier json pour les données
- le fichier .env pour les variables d'environnements

# Installation
Exemple pour le sous domaine paca

Recuperer le projet en `ssl`
```
cd /var/www
git clone https://github.com/nynif/web-site-drone.git
mv web-site-drone web-site-drone-paca
cd web-site-drone-paca
```

```
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt 
```

Importer le dossier custom
**Dans l'exemple on crée le dossier custom mais en réalité il va plus souvent être stocké ailleurs et sera copier en utilisant scp:
sur l'ordinateur de travail** 

```
scp -r custom_paca root@[ip]:/var/www/web-site-drone-paca/custom
```

```
python manage.py compilescss
python manage.py collectstatic
python manage.py migrate
```

# Configurer apache
Ajouter la conf dans `/etc/apache2/sites-available/`
a2ensite 
systemctl reload apache2

# Ajouter le DNS
Type A

# Certiticat ssl
on utilise certbot pour generer les certificats ssl
directement sur le serveur :
```
sudo certbot certonly --manual --preferred-challenges=dns --server https://acme-v02.api.letsencrypt.org/directory --agree-tos -d *.drone-photovideo.fr
```