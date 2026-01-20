import pandas as pd
from pathlib import Path

# Dicionário de "IA": sugestão de método por composto
METODO_POR_COMPOSTO = {
    "proantocianidinas": "Extração com acetona 70% + agitação (25°C, 1h)",
    "fenólicos": "Extração com metanol 80% + refluxo (60°C, 20 min)",
    "carotenoides": "Extração com hexano:acetona (1:1) sob N2",
    "flavonoides": "Extração com etanol 70% + ultrassom (40 kHz, 30 min)",
}

print("🚀 Iniciando pipeline ETL...")

# 1. EXTRACT: ler o CSV
df = pd.read_csv("data/raw/residuos.csv")
print(f"✅ {len(df)} resíduos carregado:")
print(df, "\n")

# 2. TRANSFORM: adicionar sugestão
df["sugestao"] = df["composto_alvo"].map(METODO_POR_COMPOSTO)

# Preencher possíveis valores ausentes (segurança)
df["sugestao"] = df["sugestao"].fillna("Método não cadastrado para este composto.")

print("🧠 Sugestões de extração geradas:")
print(df,"\n")

# 3. LOAD: salvar resultado
Path("output").mkdir(exist_ok=True)
df.to_csv("output/sugestoes_residuos.csv", index=False, encoding="utf-8")
print("💾 Resultado salvo em: output/sugestoes_residuos.csv")
print("\n🎉 Pipeline concluído com sucesso!")