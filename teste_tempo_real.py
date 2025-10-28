import time
from index import responder_pergunta  # Importa seu bot

# Mapeamento de qual resposta ESPERADA para cada pergunta
respostas_esperadas = {
    # PERGUNTAS ORIGINAIS (20)
    "como calcular regressão linear": "regressão linear",
    "me explique regressão linear": "regressão linear", 
    "o que é regressão linear": "regressão linear",
    "como funciona random forest": "random forest",
    "me fale sobre random forest": "random forest",
    "o que é random forest": "random forest",
    "explique overfitting": "overfitting",
    "o que é overfitting": "overfitting", 
    "como evitar overfitting": "overfitting",
    "o que é naive bayes": "naive bayes",
    "como funciona naive bayes": "naive bayes",
    "me explique naive bayes": "naive bayes",
    "o que é fit": "fit",
    "como usar fit": "fit",
    "o que é predict": "predict",
    "como usar predict": "predict",
    "o que é cross validation": "cross validation",
    "como fazer cross validation": "cross validation",
    "o que é feature engineering": "feature engineering",
    "como fazer feature engineering": "feature engineering",
    
    # 🔥 PERGUNTAS ADICIONAIS SOBRE OS MESMOS TÓPICOS (20 novas)
    # Overfitting (5 variações)
    "fale sobre overfitting": "overfitting",
    "defina overfitting": "overfitting",
    "o que significa overfitting": "overfitting", 
    "conceito de overfitting": "overfitting",
    "overfitting em machine learning": "overfitting",
    
    # Random Forest (5 variações)
    "o que é floresta aleatória": "random forest",
    "como random forest funciona": "random forest",
    "vantagens do random forest": "random forest",
    "random forest para classificação": "random forest", 
    "explique floresta aleatória": "random forest",
    
    # Regressão Linear (5 variações)
    "como implementar regressão linear": "regressão linear",
    "regressão linear em python": "regressão linear",
    "passos para regressão linear": "regressão linear",
    "modelo de regressão linear": "regressão linear",
    "aplicações de regressão linear": "regressão linear",
    
    # Feature Engineering (5 variações)
    "engenharia de features": "feature engineering",
    "como criar features": "feature engineering",
    "técnicas de feature engineering": "feature engineering",
    "importância da engenharia de features": "feature engineering",
    "feature engineering para ml": "feature engineering"
}

print("🧠 INICIANDO TESTE DO CÉREBRO IA - ESTRATÉGIA EXPANDIDA")
print("=" * 50)
print(f"📊 Total de perguntas: {len(respostas_esperadas)}")
print(f"🎯 Foco: Testar variações dos mesmos tópicos")

acertos_reais = 0
total = len(respostas_esperadas)
acertos_por_topico = {}

for i, (frase, topico_esperado) in enumerate(respostas_esperadas.items(), 1):
    print(f"\n[{i}/{total}] 🔍 Pergunta: {frase}")
    print(f"   🎯 Esperado: {topico_esperado}")
    
    # Mede o tempo de resposta
    inicio = time.time()
    resposta = responder_pergunta(frase)
    tempo = time.time() - inicio
    
    # VERIFICAÇÃO REAL: Resposta contém o tópico esperado?
    resposta_minuscula = resposta.lower()
    
    if topico_esperado in resposta_minuscula:
        acertos_reais += 1
        status = "✅ ACERTO REAL"
        # Contabiliza acertos por tópico
        if topico_esperado in acertos_por_topico:
            acertos_por_topico[topico_esperado] += 1
        else:
            acertos_por_topico[topico_esperado] = 1
    elif "não sei" in resposta_minuscula or "🤔" in resposta:
        status = "❌ NÃO SABE"
    else:
        status = "❌ RESPOSTA ERRADA"
    
    print(f"⏱️  Tempo: {tempo:.2f}s | {status}")
    print(f"💡 Resposta: {resposta[:100]}...")

# Resultado final
print("\n" + "=" * 50)
print(f"🎯 RESULTADO FINAL - ESTRATÉGIA EXPANDIDA:")
print(f"📊 Acertos Reais: {acertos_reais}/{total}")
print(f"📈 Porcentagem Real: {(acertos_reais/total)*100:.1f}%")

# Análise por tópico
print(f"\n📋 ANÁLISE POR TÓPICO:")
for topico in set(respostas_esperadas.values()):
    total_topico = list(respostas_esperadas.values()).count(topico)
    acertos_topico = acertos_por_topico.get(topico, 0)
    porcentagem = (acertos_topico/total_topico)*100 if total_topico > 0 else 0
    print(f"   {topico}: {acertos_topico}/{total_topico} ({porcentagem:.1f}%)")

if acertos_reais/total >= 0.8:
    print("🚀 PERFORMANCE: EXCELENTE!")
elif acertos_reais/total >= 0.6:
    print("⚠️  PERFORMANCE: RAZOÁVEL") 
elif acertos_reais/total >= 0.4:
    print("🔴 PERFORMANCE: RUIM")
else:
    print("💀 PERFORMANCE: PÉSSIMA")

    # 🔍 DEBUG 1: Mostra a pergunta recebida
    print(f"🎯 DEBUG: Pergunta recebida: '{pergunta}'")