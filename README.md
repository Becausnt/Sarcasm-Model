# HugVincentLB-259
### NOTE:
Jeglicher code wurde in Python 3.12.9 geschrieben.
Falls Sie eine andere Version nutzen kann es sein, dass die Libraries inkompatibel sind. (Ex. SpaCy funktioniert nicht mit python versionen über 3.12 oder unter 3.9)

## Dataset
Das Datenset besteht aus etwa 28'000 Einträgen, welche aus jeweils 3 Attributen bestehen:
- is_sarcastic: 1 falls der Titel sarkastisch ist, ansonsten 0
- headline: Titel des Artikels
- article_link: link zum Artikel

Im bereinigten Datenset habe ich `article_link` entfernt, da ich mich mehr auf den Sarkasmus selbst und weniger auf sarkastische Quellen konzentrieren möchte.

### Example entry
Ein Beispieleintrag des bereinigten Datensets sieht so aus:
```json
{"is_sarcastic": 1, "headline": "inclement weather prevents liar from getting to work"}
```

### Credits
Das Datenset wurde von Misra Rishabh erstellt.
- Publikationen: [Rishabh Misra – ML Engineer | Book Author](https://rishabhmisra.github.io/publications/)
- Datenset: [News Headlines Dataset For Sarcasm Detection](https://www.kaggle.com/datasets/rmisra/news-headlines-dataset-for-sarcasm-detection)

```
1. Misra, Rishabh and Prahal Arora. "Sarcasm Detection using News Headlines Dataset." AI Open (2023).
2. Misra, Rishabh and Jigyasa Grover. "Sculpting Data for ML: The first act of Machine Learning." ISBN 978-0-578-83125-1 (2021).
```
### Dataset License
Das Datenset ist unter [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) lizensiert.
Welche die Bedingung `Attribution` stellt, aber ansonsten freie Hand lässt.