


## Análise de Dados e Machine Learning para Predição de Valores de Imóveis para Aluguel

### Descrição do Projeto

#### Visão Geral
Este projeto tem como objetivo desenvolver um sistema de análise de dados e machine learning para prever os valores de diárias de imóveis para aluguel em uma plataforma imobiliária. A ideia é auxiliar novos proprietários a colocar seus imóveis disponíveis para aluguel com um preço competitivo no mercado, utilizando como base uma extensa coleção de dados do Airbnb entre abril de 2018 e abril de 2020. Para realizar essa previsão, a variável que será estimada é a 'price' (preço) dos imóveis. O uso de algoritmos de regressão em machine learning, que utilizarão as características do imóvel, localização e outras informações relevantes disponíveis.


### Dados
Os dados utilizados neste projeto são provenientes da plataforma [Airbnb](http://insideairbnb.com/explore/) e contêm informações sobre diversos imóveis, como localização geográfica, características do imóvel, avaliações de hóspedes e preços de diárias. O conjunto de dados abrange um período de dois anos, de abril de 2018 a abril de 2020.

#### Documentação dos Dados
Para acessar a documentação detalhada dos dados, incluindo o dicionário dos dados que fornece informações sobre todas as variáveis, você pode consultar o seguinte link:

[Airbnb](http://insideairbnb.com/explore/)

[Dicionário de Dados](https://docs.google.com/spreadsheets/d/1iWCNJcSutYqpULSQHlNyGInUvHg2BoUGoNRIGa6Szc4/edit#gid=1322284596)




### Etapas do Projeto

1. **Análise Exploratória de Dados**: Realizar uma exploração completa dos dados coletados do Airbnb, incluindo análise univariada, distribuição, correlação entre algumas variáveis e análise qualitativa e quantitativa de forma geral. Além disso, a análise identificará possíveis outliers, que serão tratados na etapa de pré-processamento de dados.

2. **Pré-processamento de Dados**: Realizar limpeza, tratamento e transformação dos dados para prepará-los para alimentar os modelos de machine learning. Isso inclui o tratamento de outliers identificados na etapa de análise exploratória.

3. **Engenharia de Recursos**: Criar novas variáveis ou recursos a partir dos dados existentes para melhorar o desempenho dos modelos preditivos.

4. **Modelagem de Machine Learning**: Utilizar algoritmos de machine learning para construir modelos de regressão capazes de prever os valores de diárias dos imóveis. Foram testados quatro modelos diferentes de machine learning, e o melhor modelo foi selecionado após avaliação.

5. **Avaliação e Otimização do Modelo**: O modelo selecionado foi avaliado e otimizado para obter a melhor precisão. Durante esse processo, foram feitos ajustes e melhorias no modelo, levando em consideração métricas de desempenho adequadas.

6. **Implementação da Interface de Usuário**: Implementar uma interface amigável usando o ***Streamlit***, onde os novos proprietários podem inserir informações de seus imóveis e receber uma estimativa do valor ideal para a diária.



### Tecnologias Utilizadas

- **Linguagem de Programação**: Python
- **Bibliotecas Python**: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
- **Jupyter Notebook**: Para análise exploratória e desenvolvimento dos modelos
- **Streamlit**: Para criar a interface de usuário (front-end)
- **JobLib**: Utilizado para salvar e carregar modelos treinados.


### Considerações Finais

Este projeto visa criar uma ferramenta útil e eficaz para auxiliar novos proprietários que desejam alugar seus imóveis pela primeira vez a chegar a um preço padrão de mercado. O projeto está em fase final de acabamento, e aprimoramentos contínuos estão sendo feitos para aprimorar a precisão e a usabilidade da ferramenta.

**Observação**: O projeto pode ser expandido e aprimorado no futuro, adicionando mais recursos, usando outras fontes de dados ou implementando técnicas avançadas de machine learning, dependendo dos resultados iniciais e das necessidades específicas do público-alvo.




