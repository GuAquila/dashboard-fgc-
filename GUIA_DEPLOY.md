# 🚀 GUIA RÁPIDO - COMO COLOCAR NO AR

## Passo 1️⃣: Criar conta no GitHub
1. Acesse: https://github.com
2. Clique em "Sign up" e crie sua conta

## Passo 2️⃣: Criar novo repositório
1. No GitHub, clique no "+" no canto superior direito
2. Selecione "New repository"
3. Preencha:
   - Repository name: `dashboard-fgc` (ou outro nome)
   - Deixe em "Public"
   - ✅ Marque "Add a README file"
4. Clique em "Create repository"

## Passo 3️⃣: Fazer upload dos arquivos
1. No seu repositório, clique em "Add file" → "Upload files"
2. Arraste TODOS os arquivos baixados:
   - app.py
   - requirements.txt
   - README.md
   - .gitignore (se não aparecer, não tem problema)
   - Alocação_FGC_-_Tauari.xlsx
3. Clique em "Commit changes"

## Passo 4️⃣: Deploy no Streamlit Cloud
1. Acesse: https://streamlit.io/cloud
2. Clique em "Sign in" e faça login com sua conta GitHub
3. Clique em "New app"
4. Preencha:
   - Repository: selecione `seu-usuario/dashboard-fgc`
   - Branch: `main`
   - Main file path: `app.py`
5. Clique em "Deploy!"

## ⏰ Aguarde
- O deploy leva de 1 a 3 minutos
- Você receberá uma URL do tipo: `seu-app.streamlit.app`

## ✅ Pronto!
Seu dashboard está no ar! Compartilhe a URL com quem precisar.

## 🔄 Para atualizar os dados no futuro:
1. Vá no seu repositório no GitHub
2. Clique no arquivo `Alocação_FGC_-_Tauari.xlsx`
3. Clique no ícone de lápis (Edit)
4. Delete e faça upload do novo arquivo
5. Commit changes
6. O Streamlit atualizará automaticamente!

---

### ❓ Problemas comuns:

**"App não carrega"**
- Aguarde 2-3 minutos após o deploy
- Verifique se todos os arquivos foram enviados

**"Erro ao ler arquivo Excel"**
- Confirme que o arquivo .xlsx está no repositório
- Verifique se o nome está exato: `Alocação_FGC_-_Tauari.xlsx`

**"Erro de dependências"**
- Verifique se o arquivo `requirements.txt` está no repositório
