# TP 2
L’objectif de ce tp est de configurer un workflow Github Action, de transformer un wrapper en API,
de créer un github action qui build et push l’image à chaque nouveau commit, 
de publier automatiquement et de mettre à disposition son image sur DockerHub. 

Dans un premier temps, j'ai créé mon github action. Pour ce faire, j'ai créé un workflow yml. 
Dans le processus, j'inclus le lien du dockerfile, le login vers mon dockerhub avec identitfiant
et password dans secret, je build and push mon image docker. Pour finir, je transforme le 
wrapper en API directement sur le main.py avec FastAPI.

Je run les etapes ci-dessous dans mon terminal: 

docker build -t weatherapp . pour recréer l'image


API qui renvoie la météo en utilisant la commande suivante en utilisant votre image :
docker run --network host -p 8081 --env API_KEY=**** angele745/meteocheck
