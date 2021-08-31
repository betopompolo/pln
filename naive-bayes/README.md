# Classificador NaiveBayes

Implementação em python do classificador naive-bayes, utilizando a [base de dados bbc](https://www.kaggle.com/shivamkushwaha/bbc-full-text-document-classification).

Em relação ao modelo proposto em aula, duas melhorias foram feitas:
- Remoção de pontuação no início e final de cada palavra ("'", '"', '(', ')')
- Remoção das 50 palavras mais frequentes do vocabulário
- Suporte a mais de duas classes para o classificador

Utilizou-se as notícias das pastas `business`, `entertainment`, `politics` e `tech` - as notícias da pasta `tech` pertencendo a classe `true` e o resto, a classe `false`.

O dataset gerado foi embaralhado e dividido em 70% para treino e 30% para testes. Por fim, obteve-se aproximadamente 97% de acurácia (número de predições corretas divido pelo total de amostras do teste)com o classificador NaiveBayes.