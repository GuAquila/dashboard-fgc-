# Dashboard de Alocação FGC

Dashboard interativo para visualização de alocações FGC por Emissor e Assessor.

## 📋 Como usar no seu computador

### 1. Instalar Python
- Baixe Python em: https://www.python.org/downloads/
- Durante a instalação, marque "Add Python to PATH"

### 2. Baixar o projeto
- Baixe todos os arquivos deste repositório
- Coloque o arquivo `Alocação_FGC_-_Tauari.xlsx` na mesma pasta

### 3. Instalar as dependências
Abra o terminal/prompt de comando na pasta do projeto e rode:
```bash
pip install -r requirements.txt
```

### 4. Rodar o dashboard
No terminal, rode:
```bash
streamlit run app.py
```

O dashboard abrirá automaticamente no seu navegador!

## 🚀 Como colocar no GitHub e Streamlit Cloud

### Passo 1: Criar repositório no GitHub
1. Acesse https://github.com e faça login
2. Clique em "New repository"
3. Dê um nome (ex: dashboard-fgc)
4. Marque "Public"
5. Clique em "Create repository"

### Passo 2: Subir os arquivos
1. Baixe GitHub Desktop: https://desktop.github.com/
2. Clone seu repositório
3. Copie os arquivos para a pasta do repositório:
   - `app.py`
   - `requirements.txt`
   - `README.md`
   - `Alocação_FGC_-_Tauari.xlsx`
4. Commit e push no GitHub Desktop

### Passo 3: Deploy no Streamlit Cloud
1. Acesse https://streamlit.io/cloud
2. Faça login com sua conta GitHub
3. Clique em "New app"
4. Selecione seu repositório
5. Configure:
   - Branch: main
   - Main file path: app.py
6. Clique em "Deploy"

Pronto! Seu dashboard estará online!

## 📊 Funcionalidades

### Tela Emissor
- Visualização de todos os clientes com posição acima de R$ 250.000
- Filtro por emissor específico
- Gráfico top 10 maiores posições
- Tabela completa de clientes
- Resumo por emissor

### Tela Assessor
- Visualização por assessor específico
- Gráfico de distribuição por emissor
- Top 15 clientes do assessor
- Alertas de posições críticas (próximas do limite)

## 🔧 Estrutura do projeto

```
dashboard-fgc/
├── app.py                          # Código principal do dashboard
├── requirements.txt                # Dependências do projeto
├── README.md                       # Este arquivo
└── Alocação_FGC_-_Tauari.xlsx     # Arquivo de dados
```

## ⚠️ Importante

- O arquivo Excel deve estar na mesma pasta do app.py
- O arquivo deve ter a aba "Filtrados" com as colunas corretas
- Para atualizar os dados, basta substituir o arquivo Excel e reiniciar o app

## 📝 Observações

Este dashboard filtra automaticamente posições iguais ou superiores a R$ 250.000,00 por cliente e emissor.
