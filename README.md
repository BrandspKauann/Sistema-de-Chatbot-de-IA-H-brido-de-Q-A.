# Sistema de Chatbot de IA Híbrido de Q&A

## Visão Geral
Este projeto apresenta um sistema de chatbot híbrido de [translate:Perguntas e Respostas (Q&A)] que evoluiu de uma abordagem literal baseada em palavras-chave para um modelo inteligente com compreensão semântica.  
O objetivo principal é criar um assistente capaz de interpretar o significado das perguntas feitas pelo usuário, mesmo quando formuladas de maneiras diferentes, mantendo alta acurácia e relevância nas respostas.

## Estrutura do Cérebro
Inicialmente, o chatbot funcionava como uma busca literal, similar a uma lista telefônica — só retornava resultados quando a entrada era exatamente igual a uma das perguntas conhecidas.  
Atualmente, o sistema opera como um assistente inteligente, capaz de compreender o que o usuário quer dizer, não apenas o que ele digita.

### Exemplo prático:
**PERGUNTA:** "me explique regressão linear"  
**PROCESSAMENTO:**  
- "me explique" → `[0.7, 0.3, 0.6]`  
- "regressão linear" → `[0.8, 0.2, 0.5]`  
- Cálculo de similaridade: 85%  
**RESPOSTA:** Mostra explicação sobre regressão linear

O cérebro do sistema utiliza TF-IDF em conjunto com Cosine Similarity para medir a similaridade semântica entre a pergunta do usuário e o banco de dados de conhecimento.

## Objetivo e Problema
O desafio central foi garantir que o sistema compreendesse o significado real das perguntas, e não apenas correspondências literais.  
Assim, a solução precisava lidar com:

- Variações linguísticas naturais  
- Diferenças semânticas entre termos semelhantes  
- Consistência entre diferentes formulações da mesma pergunta  
- Desempenho adequado para uso em tempo real

## Métricas de Sucesso

| Métrica      | Descrição                             |
|--------------|-------------------------------------|
| Acurácia     | Percentual de respostas corretas    |
| Coverage     | Capacidade de cobrir diferentes formas de perguntar |
| Performance  | Tempo médio de resposta              |
| Robustez    | Consistência das respostas entre variações |

## Evolução do Sistema

| Etapa     | Acurácia     | Resultado                  |
|-----------|--------------|----------------------------|
| Início    | 50% (20/40)  | Base literal               |
| Otimização| 80% (32/40)  | Ajuste de pesos e vetores  |
| Final     | 100% (40/40) | Compreensão semântica consolidada |

## Conquistas Técnicas
O sistema consolidou um modelo híbrido de Q&A com as seguintes capacidades:

- Busca Exata → para perguntas diretas  
- Combinações Exatas → para variações problemáticas  
- Similaridade Semântica → para interpretação inteligente  
- Fallback Controlado → para perguntas desconhecidas  
- 100% de acurácia em 40 perguntas variadas  
- Compreensão de sinônimos e variações linguísticas  
- Respostas específicas e contextualizadas  

## Conclusão
O projeto alcançou o objetivo de criar um chatbot híbrido com interpretação semântica, unindo precisão, velocidade e compreensão contextual.  
Esse modelo serve como base sólida para aplicações futuras em assistentes virtuais, automações inteligentes e sistemas de suporte ao cliente baseados em IA.
