# 🌱 Pipeline ETL: Resíduos Agroindustriais

Projeto prático de Ciência de Dados aplicado à Ciência de Alimentos.  
Demonstra um fluxo completo de **Extração, Transformação e Carregamento (ETL)** usando dados de resíduos agroalimentares.

## 🎯 Objetivo
Sugerir métodos de extração adequados para compostos bioativos em resíduos agroindustriais (ex.: cascas, bagaços, caroços), com base em regras de domínio (simulando IA).

## 📂 Estrutura
- `data/raw/residuos.csv`: dados de entrada (resíduos e compostos-alvo)
- `src/main.py`: pipeline ETL (extrai, transforma, carrega)
- `output/sugestoes_residuos.csv`: resultado com sugestões de métodos

## ▶️ Como executar
```bash
pip install pandas
python src/main.py