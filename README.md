# Hybrid AI Q&A Chatbot System — English & Chinese Combined Version

## Overview / 概述  
This project presents a hybrid [translate:问答系统（Q&A）] chatbot system evolving from a literal keyword-based approach to an intelligent model with semantic understanding.  
本项目展示了一个混合型的[translate:Question and Answer (Q&A)]聊天机器人，能够理解即使以不同方式提出的问题含义并提供准确回答。

## Brain Structure / 系统核心结构  
Initially, the chatbot worked like a phone book, returning answers only for exact matches.  
起初，聊天机器人只会针对完全匹配的问题返回结果。  
Now it acts as an intelligent assistant, understanding user intention beyond exact words.  
现阶段，它是个智能助手，能理解用户意图而非文字本身。

### Example / 示例:  
**QUESTION / 问题:** "explain linear regression / 请解释线性回归"  
**PROCESSING / 处理:**  
- "explain / 请解释" → `[0.7, 0.3, 0.6]`  
- "linear regression / 线性回归" → `[0.8, 0.2, 0.5]`  
Similarity / 相似度: 85%  
**ANSWER / 回答:** Shows explanation about linear regression / 显示线性回归的解释

## Goals and Challenges / 目标与挑战  
Ensure true understanding instead of literal match.  
确保系统真正理解问题含义。  
Handle language variations and real-time performance.  
处理语言变体与实时响应。

## Success Metrics / 成功指标

| Metric / 指标  | Description / 描述                  |
|---------------|-----------------------------------|
| Accuracy / 准确率 | Percentage of correct answers / 正确回答比例  |
| Coverage / 覆盖率 | Different ways to ask questions / 不同提问形式覆盖率 |
| Performance / 性能 | Average response time / 平均响应速度            |
| Robustness / 鲁棒性 | Consistency across variations / 回答一致性          |

## Conclusion / 结论  
The project created a hybrid chatbot with semantic understanding, precision, speed, and context comprehension, laying a strong foundation for intelligent assistants and AI customer support.  
该项目打造了语义理解精准又快速的混合型聊天机器人，为智能助手和AI客户支持奠定坚实基础。
