# index.py (VERSÃO OTIMIZADA)
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# Base de conhecimento expandida
conhecimento = {
    # TERMOS BÁSICOS
    "fit": "O método fit() é usado para treinar modelos de machine learning. Ele recebe os dados de treino X (features) e y (target) e ajusta os parâmetros do modelo para aprender os padrões dos dados.",
    
    "predict": "O predict() faz previsões usando um modelo já treinado. Ele recebe novos dados de entrada e retorna as previsões baseadas no que o modelo aprendeu durante o treinamento.",
    
    "naive bayes": "Naive Bayes é um algoritmo de classificação rápido e eficiente, especialmente bom para trabalhar com dados de texto como emails e documentos. É baseado no teorema de Bayes e assume que as features são independentes.",
    
    "random forest": "Random Forest é um algoritmo ensemble que combina múltiplas árvores de decisão. Cada árvore é treinada com uma amostra diferente dos dados, e a previsão final é a média ou votação de todas as árvores. É muito preciso mas pode ser mais lento.",
    
    "cross validation": "Cross validation é uma técnica para avaliar a performance de modelos. Divide os dados em várias partes (folds), treina o modelo em algumas partes e testa nas outras. Recomendo usar 10 folds para a maioria dos projetos.",
    
    "feature engineering": "Feature engineering é o processo de criar, selecionar e transformar variáveis para melhorar o desempenho do modelo. Representa cerca de 80% do trabalho de um engenheiro de machine learning.",
    
    # PERGUNTAS PRÁTICAS - COMO FAZER
    "como calcular regressão linear": "Para calcular regressão linear: primeiro importe LinearRegression do sklearn, prepare seus dados separando features e target, divida em treino e teste com train_test_split, crie o modelo, use fit() para treinar com os dados de treino, depois use predict() para fazer previsões nos dados de teste e finalmente avalie com métricas como R² score.",
    
    "como calcular acurácia": "Para calcular acurácia, use a função accuracy_score do sklearn.metrics, passando os valores verdadeiros e as previsões do modelo. A acurácia mostra a porcentagem de previsões corretas. Você também pode usar model.score() diretamente no modelo treinado.",
    
    "como escolher algoritmo": "Para escolher o algoritmo: se for classificação (categorias), use Random Forest ou Naive Bayes; se for regressão (números), use Linear Regression ou Random Forest Regressor; para dados de texto, Naive Bayes é excelente; para máxima precisão com tempo suficiente, Random Forest é ótimo.",
    
    "como lidar com dados faltantes": "Para dados faltantes: você pode remover as linhas com valores faltantes usando dropna(), ou preencher os valores: use a média para números, moda para categorias, ou algoritmos de imputação como SimpleImputer do sklearn.",
    
    "quantos dados preciso para treinar": "O mínimo recomendado é 1000 amostras para problemas simples, mas idealmente 10.000+ para modelos robustos. Para deep learning, são necessários 50.000+ amostras. A qualidade dos dados é mais importante que a quantidade.",
    
    "como saber se meu modelo é bom": "Um modelo é bom quando: tem alta acurácia nos dados de teste (não só treino), generaliza bem para novos dados, as métricas de avaliação são consistentes, e não mostra overfitting (quando performa bem no treino mas mal no teste).",
    
    "o que é overfitting": "OVERFITTING: Ocorre quando um modelo de ML se ajusta excessivamente aos dados de treino, memorizando ruídos em vez de padrões gerais. SINAIS: Alta acurácia no treino (>95%), baixa no teste (<70%). SOLUÇÃO: Mais dados, regularização, cross-validation.",
    
    "como evitar overfitting": "Para evitar overfitting: use mais dados de treino, faça cross-validation, aplique regularização (L1, L2), use técnicas de ensemble como Random Forest, simplifique o modelo, ou use dropout em redes neurais.",
    
    "qual diferença entre ai machine learning e deep learning": "AI é o campo geral, machine learning é subcampo onde máquinas aprendem com dados, e deep learning é um tipo específico de machine learning que usa redes neurais com muitas camadas. Deep learning precisa de mais dados mas pode resolver problemas mais complexos.",
    
    "como começar na área de ia": "Para começar em IA: aprenda Python, estude matemática básica (estatística, álgebra), pratica com projetos simples, aprenda bibliotecas como sklearn e tensorflow, participe de competições no Kaggle, e construa um portfolio com projetos reais.",
    
    "quanto tempo leva para aprender machine learning": "Leva 3-6 meses para aprender o básico e construir projetos simples, 1 ano para se tornar proficiente, e 2+ anos para se tornar especialista. O importante é praticar consistentemente e construir projetos reais.",
    
    "quais bibliotecas devo aprender": "As bibliotecas essenciais são: pandas para manipulação de dados, numpy para computação numérica, matplotlib e seaborn para visualização, scikit-learn para machine learning tradicional, e tensorflow ou pytorch para deep learning.",
    
    "como conseguir emprego na área": "Para conseguir emprego: construa um portfolio com projetos reais no GitHub, participe de competições no Kaggle, faça networking, aprenda a explicar modelos para não-técnicos, e mostre experiência prática resolvendo problemas reais.",

    # 🔧 CONHECIMENTOS SOBRE OVERFITTING
    "overfitting": "OVERFITTING: Ocorre quando um modelo de ML se ajusta excessivamente aos dados de treino, memorizando ruídos em vez de padrões gerais. SINAIS: Alta acurácia no treino (>95%), baixa no teste (<70%). SOLUÇÃO: Mais dados, regularização, cross-validation.",
    
    "underfitting": "Underfitting é o oposto do overfitting. Ocorre quando o modelo é muito simples e não consegue capturar os padrões dos dados. Resulta em performance ruim tanto nos dados de treino quanto teste. Solução: usar modelo mais complexo ou mais features.",
    
    "overfitting e underfitting": "Overfitting é quando o modelo é muito complexo e decora os dados. Underfitting é quando o modelo é muito simples e não aprende os padrões. O ideal é encontrar o equilíbrio onde o modelo generaliza bem para dados novos.",
    
    "regularização": "Regularização é uma técnica para prevenir overfitting adicionando uma penalidade aos parâmetros do modelo. L1 (Lasso) tende a zerar alguns coeficientes, L2 (Ridge) reduz todos os coeficientes. Ambas ajudam o modelo a generalizar melhor.",
    
    "bias e variância": "Bias é o erro por suposições muito simplistas (causa underfitting). Variância é o erro por sensibilidade a pequenas flutuações nos dados (causa overfitting). O tradeoff bias-variância busca equilibrar esses dois erros.",
    
    "validação cruzada": "Cross-validation é uma técnica para avaliar modelos dividindo os dados em k partes (folds). Treina em k-1 partes e testa na parte restante, repetindo k vezes. Isso dá uma estimativa mais confiável da performance e ajuda a detectar overfitting.",
    
    "como detectar overfitting": "Para detectar overfitting: compare a performance nos dados de treino vs teste. Se a acurácia no treino for muito maior que no teste, há overfitting. Cross-validation e curva de aprendizado também ajudam na detecção.",
    
    "early stopping": "Early stopping é uma técnica usada em treinamento iterativo (como redes neurais) onde paramos o treinamento quando a performance no validation set para de melhorar. Isso previne overfitting automaticamente.",
    
    "dropout": "Dropout é uma técnica de regularização para redes neurais onde aleatoriamente 'desligamos' alguns neurônios durante o treinamento. Isso previne que a rede dependa muito de neurônios específicos e melhora a generalização.",
    
    # 🎯 SINÔNIMOS E VARIAÇÕES
    "floresta aleatória": "Random Forest é um algoritmo ensemble que combina múltiplas árvores de decisão. Cada árvore é treinada com uma amostra diferente dos dados, e a previsão final é a média ou votação de todas as árvores.",
    
    "engenharia de features": "Feature engineering é o processo de criar, selecionar e transformar variáveis para melhorar o desempenho do modelo. Representa cerca de 80% do trabalho de um engenheiro de machine learning.",
    
    "sobreajuste": "Sobreajuste (overfitting) ocorre quando um modelo de ML se ajusta excessivamente aos dados de treino, memorizando ruídos em vez de padrões gerais.",
    
    # 🧠 CONHECIMENTOS AVANÇADOS
    "gradient descent": "Gradient Descent é um algoritmo de otimização usado para encontrar os parâmetros que minimizam a função de custo. Ele calcula o gradiente (derivada) e ajusta os parâmetros na direção que reduz o erro.",
    
    "backpropagation": "Backpropagation é o algoritmo usado para treinar redes neurais. Ele calcula o gradiente da função de custo em relação a todos os pesos na rede, propagando o erro das camadas de saída para as camadas de entrada.",
    
    "activation function": "Funções de ativação introduzem não-linearidade nas redes neurais. As principais são: ReLU (mais comum), Sigmoid (para probabilidades), Tanh e Softmax (para multi-classificação).",
    
    "learning rate": "Learning rate é um hiperparâmetro que controla o tamanho dos passos durante o treinamento com Gradient Descent. Muito alto: pode divergir. Muito baixo: treinamento lento.",
}

# Função OTIMIZADA com múltiplas camadas
def responder_pergunta(pergunta):
    pergunta = pergunta.lower().strip()
    
    # 🚀 PRIMEIRO: COMBINAÇÕES EXATAS (antes da busca exata)
    combinacoes_exatas = {
        # Overfitting
        "explique overfitting": conhecimento["overfitting"],
        "o que é overfitting": conhecimento["overfitting"],
        "como evitar overfitting": conhecimento["como evitar overfitting"],
        "fale sobre overfitting": conhecimento["overfitting"],
        "defina overfitting": conhecimento["overfitting"],
        "o que significa overfitting": conhecimento["overfitting"],
        "conceito de overfitting": conhecimento["overfitting"],
        "overfitting em machine learning": conhecimento["overfitting"],
        
        # Regressão Linear
        "me explique regressão linear": conhecimento["como calcular regressão linear"],
        "o que é regressão linear": conhecimento["como calcular regressão linear"],
        "como implementar regressão linear": conhecimento["como calcular regressão linear"],
        "regressão linear em python": conhecimento["como calcular regressão linear"],
        "passos para regressão linear": conhecimento["como calcular regressão linear"],
        "modelo de regressão linear": conhecimento["como calcular regressão linear"],
        "aplicações de regressão linear": conhecimento["como calcular regressão linear"],
        
        # Feature Engineering
        "engenharia de features": conhecimento["feature engineering"],
        "como criar features": conhecimento["feature engineering"],
        "técnicas de feature engineering": conhecimento["feature engineering"],
        "importância da engenharia de features": conhecimento["feature engineering"],
        "feature engineering para ml": conhecimento["feature engineering"],
        
        # Random Forest
        "floresta aleatória": conhecimento["random forest"],
        "explique floresta aleatória": conhecimento["random forest"],
    }
    
    if pergunta in combinacoes_exatas:
        return combinacoes_exatas[pergunta]
    
    # 🚀 DEPOIS: Busca EXATA tradicional
    for palavra_chave, resposta in conhecimento.items():
        if palavra_chave in pergunta:
            return resposta
    
    # 🚀 FINALMENTE: Busca por SIMILARIDADE
    perguntas_lista = list(conhecimento.keys())
    respostas_lista = list(conhecimento.values())
    
    # Adiciona a pergunta do usuário à lista
    todas_perguntas = perguntas_lista + [pergunta]
    
    # Calcula similaridade
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(todas_perguntas)
    
    # Similaridade entre a pergunta e todas as outras
    similaridades = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    
    # Encontra a mais similar
    indice_mais_similar = similaridades.argmax()
    similaridade_maxima = similaridades.max()
    
    # Se for suficientemente similar, retorna a resposta
    if similaridade_maxima > 0.5:
        return respostas_lista[indice_mais_similar]
    else:
        return "🤔 Não tenho certeza sobre isso. Você pode reformular a pergunta ou me ensinar sobre esse tópico?"

# Interface
def main():
    st.set_page_config(
        page_title="Meu Cérebro IA", 
        page_icon="🧠",
        layout="centered"
    )
    
    st.title("🧠 Meu Assistente Pessoal de IA")
    st.markdown("---")
    
    st.write("**Pergunte anything sobre Machine Learning!**")
    
    # Input da pergunta
    pergunta = st.text_input(
        "Digite sua pergunta:",
        placeholder="Ex: Como calcular regressão linear? O que é overfitting?"
    )
    
    # Botão de enviar
    if st.button("Perguntar") or pergunta:
        if pergunta.strip():
            with st.spinner("🧠 Pensando..."):
                resposta = responder_pergunta(pergunta)
                
                st.success("**Resposta:**")
                st.info(resposta)
        else:
            st.warning("⚠️ Digite uma pergunta!")

if __name__ == "__main__":
    main()