# Projet de Validation
Réalisé par Berkia Youssef et Mansour Chaouki.

# code
Les divers configuration alice et bob:
- AliceBob/AliceBobV0: alice et bob progresse sans garde, donc possibilité de rencontre en Section critique
- AliceBobV1: alice et bob progresse avec garde, pas de rencontre en section critique, mais il y'a deadlock
- AliceBobV2: alice et bob progresse avec garde, et sans deadlock. Bob donne la priorité à alice
- AliceBobPeterson: alice et bob avec algorithme de peterson

Versions avec et sans langage soup pour V0 et V1 
Version uniquement avec langage soup pour V2 et peterson

Version avec et sans langage soup pour Hanoi

- les fichiers Test*.py contiennent les exécutions.

# limites

- detection de cycle: la détection de cycle avec bfs n'as pas été entièrement implémenté

- vérification de propriété avec automate de bucchi: potentielle erreur dans les gardes et les actions de l'automate de bucchi, l'automate testé est le suivant:
<br>
<br>
![image](https://github.com/chaouki11/Validation/assets/82370973/94c06c3b-314f-41ec-8b4f-5bc483149542)



# objectif 
L'objectif principal de ce projet est de fournir un ensemble d'outils et de fonctionnalités pour étudier et valider des solutions liées aux graphes et à la synchronisation. Il permet également de comprendre et d'expérimenter différents algorithmes et concepts abordés dans le cadre du cours de validation.

# Utilisation
Pour utiliser ce projet, assurez-vous d'avoir Python installé sur votre système. Ensuite, vous pouvez explorer les différents modules en important les classes et les fonctions pertinentes dans vos propres scripts Python. Vous pouvez également exécuter les exemples de simulation fournis pour tester les fonctionnalités des différents modules.
