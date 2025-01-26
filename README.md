# Mushrooms classifier

**SEGERIE Reynalde / VITON Antoine**

**Lien du Github** : https://github.com/reynaldesgr/zz3-deep-learning-project/tree/feat-models


**N.B. : L'entraînement du modèle peut générer des warnings du aux formatages des images récupérés par notre script.**

## Données : répertoires

### Ensemble d'entraînement / validation
Les données d'entraînement (80%) et de validation (20%) se trouvent dans le répertoire ```/dataset/mushrooms``` et sont classés en trois catégories/sous-répertoires :
1. ``amanita``
2. ``crimini``
3. ``oyster``

### Ensemble de tests
Les données de tests se trouvent dans le répertoire ```/tests``` et sont classés en trois catégories/sous-répertoires :
1. ``amanita``
2. ``crimini``
3. ``oyster``


### Modèles
Nous testons ici trois modèles 
- ``ResNet50`` (*) 
- ``EfficientNetB0`` couplé avec KerasTuner pour le fine-tuning (pour tester) 
- ``DenseNet121`` 

```
- ResNet50 - Loss: 0.4345, Accuracy: 87.88%
- KerasTuner - Loss: 0.3650, Accuracy: 81.82%
- DenseNet121 - Loss: 0.7291, Accuracy: 75.76%
```
### Requirements


```
Package                   Version
------------------------- --------------
jupyter_client            8.6.3
jupyter_core              5.7.2
jupyter-events            0.11.0
jupyter-lsp               2.2.5
jupyter_server            2.15.0
jupyter_server_terminals  0.5.3
jupyterlab                4.3.4
jupyterlab_pygments       0.3.0
jupyterlab_server         2.27.3
keras                     3.8.0
keras-tuner               1.4.7
matplotlib                3.10.0
pandas                    2.2.3
tensorboard               2.18.0
tensorboard-data-server   0.7.2
tensorflow                2.18.0
```

ChatGPT a été utilisé ici à des fins de compréhension des implémentations des différents modèles et d'optimisation des couches.