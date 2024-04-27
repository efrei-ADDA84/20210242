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
# TP 3
Pour ce TP, j'ai travaillé sur le déploiement d'une application sur Azure Container Instances en utilisant Azure Container Registry et en assurant que mon API soit appelée sur le bon port. Tout d'abord, j'ai ajouté quatre étapes supplémentaires à mon pipeline :

Login vers l'ACR : J'ai configuré mon pipeline pour se connecter à Azure Container Registry en utilisant les informations d'identification appropriées.

Build and push de l'image vers l'ACR : J'ai veillé à ce que mon image Docker soit correctement construite et poussée vers Azure Container Registry.

Login vers l'Azure CLI : J'ai ajouté une étape pour me connecter à Azure CLI afin de pouvoir exécuter des commandes Azure dans mon pipeline.

Déploiement vers une ACI : En utilisant Azure CLI, j'ai déployé mon conteneur à partir de l'image stockée dans Azure Container Registry vers Azure Container Instances. J'ai pris soin de spécifier le port correct lors du déploiement pour correspondre à celui exposé dans mon conteneur Docker.

http://devops-20210242.francesouth.azurecontainer.io:8081/?lat=48.873756&lon=2.294946

# TP 4

Ce TP visait à nous familiariser avec l'utilisation de Terraform. Pour ce faire, nous avons élaboré trois fichiers distincts : un pour les fournisseurs, un pour les variables, et un fichier principal pour créer trois ressources différentes. Ces ressources comprenaient la génération d'une clé SSH, la création d'une interface réseau, et enfin la création d'une machine virtuelle. En conclusion, nous nous sommes connectés à Azure en utilisant la commande az login.
