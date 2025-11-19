# ========================================
# DASHBOARD DE ALOCAÇÃO FGC
# ========================================

# Importando as bibliotecas necessárias
import streamlit as st  # Para criar o dashboard
import pandas as pd  # Para trabalhar com dados
import plotly.express as px  # Para criar gráficos interativos

# Configuração da página - SEMPRE deve ser a primeira coisa
st.set_page_config(
    page_title="Dashboard FGC - Tauari",  # Nome que aparece na aba do navegador
    page_icon="📊",  # Ícone da aba
    layout="wide"  # Usa a tela toda
)

# ========================================
# FUNÇÃO PARA CARREGAR OS DADOS
# ========================================
@st.cache_data  # Isso faz o Streamlit não recarregar os dados toda vez
def carregar_dados():
    """
    Função que carrega os dados do arquivo Excel.
    Retorna um DataFrame (tabela) com os dados processados.
    """
    # Lê a aba 'Filtrados' do arquivo Excel
    df = pd.read_excel('Alocação_FGC_-_Tauari.xlsx', sheet_name='Filtrados')
    
    # Agrupa os dados por Cliente, Emissor e Assessor
    # E soma todos os valores NET de cada grupo
    df_agrupado = df.groupby(['Cliente', 'Emissor', 'Assessor'])['NET'].sum().reset_index()
    
    # Renomeia a coluna NET para ficar mais claro
    df_agrupado.rename(columns={'NET': 'Posição Total'}, inplace=True)
    
    # Filtra apenas posições maiores ou iguais a R$ 250.000
    df_filtrado = df_agrupado[df_agrupado['Posição Total'] >= 250000].copy()
    
    # Ordena do maior para o menor valor
    df_filtrado = df_filtrado.sort_values('Posição Total', ascending=False)
    
    return df_filtrado

# ========================================
# FUNÇÃO PARA FORMATAR VALORES EM REAIS
# ========================================
def formatar_reais(valor):
    """
    Transforma um número em formato brasileiro de reais.
    Exemplo: 1000000 vira R$ 1.000.000,00
    """
    return f"R$ {valor:,.2f}".replace(',', '_').replace('.', ',').replace('_', '.')

# ========================================
# TÍTULO DO DASHBOARD
# ========================================
st.title("📊 Dashboard de Alocação FGC - Tauari")
st.markdown("---")  # Linha divisória

# ========================================
# CARREGA OS DADOS
# ========================================
try:
    # Tenta carregar os dados
    df = carregar_dados()
    
    # Mostra informações gerais
    col1, col2, col3 = st.columns(3)  # Cria 3 colunas
    with col1:
        st.metric("Total de Clientes", len(df['Cliente'].unique()))
    with col2:
        st.metric("Total de Emissores", len(df['Emissor'].unique()))
    with col3:
        st.metric("Posição Total", formatar_reais(df['Posição Total'].sum()))
    
    st.markdown("---")
    
    # ========================================
    # CRIAÇÃO DAS ABAS
    # ========================================
    tab1, tab2 = st.tabs(["🏦 Por Emissor", "👤 Por Assessor"])
    
    # ========================================
    # ABA 1: VISUALIZAÇÃO POR EMISSOR
    # ========================================
    with tab1:
        st.header("Visualização por Emissor")
        st.markdown("Clientes com posição acima de R$ 250.000,00")
        
        # Filtro para selecionar emissor
        emissores = ['Todos'] + sorted(df['Emissor'].unique().tolist())
        emissor_selecionado = st.selectbox(
            "Selecione um Emissor:",
            emissores,
            key='emissor'
        )
        
        # Filtra os dados baseado na seleção
        if emissor_selecionado == 'Todos':
            df_filtrado = df.copy()
        else:
            df_filtrado = df[df['Emissor'] == emissor_selecionado].copy()
        
        # Mostra estatísticas do filtro
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Clientes Filtrados", len(df_filtrado))
        with col2:
            st.metric("Posição Filtrada", formatar_reais(df_filtrado['Posição Total'].sum()))
        
        # Tabela detalhada - TODOS os clientes
        st.subheader("📋 Todos os Clientes com Posição ≥ R$ 250.000,00")
        
        # Formata a coluna de valores para exibição
        df_exibicao = df_filtrado.copy()
        df_exibicao['Posição Total'] = df_exibicao['Posição Total'].apply(formatar_reais)
        
        # Mostra a tabela
        st.dataframe(
            df_exibicao,
            use_container_width=True,
            hide_index=True
        )
        
        # Resumo por emissor
        st.subheader("📊 Resumo por Emissor")
        resumo_emissor = df_filtrado.groupby('Emissor').agg({
            'Cliente': 'count',  # Conta quantos clientes
            'Posição Total': 'sum'  # Soma as posições
        }).reset_index()
        resumo_emissor.columns = ['Emissor', 'Qtd Clientes', 'Posição Total']
        resumo_emissor['Posição Total'] = resumo_emissor['Posição Total'].apply(formatar_reais)
        resumo_emissor = resumo_emissor.sort_values('Qtd Clientes', ascending=False)
        
        st.dataframe(
            resumo_emissor,
            use_container_width=True,
            hide_index=True
        )
    
    # ========================================
    # ABA 2: VISUALIZAÇÃO POR ASSESSOR
    # ========================================
    with tab2:
        st.header("Visualização por Assessor")
        st.markdown("Clientes com posição acima de R$ 250.000,00")
        
        # Filtro para selecionar assessor
        assessores = sorted(df['Assessor'].unique().tolist())
        assessor_selecionado = st.selectbox(
            "Selecione um Assessor:",
            assessores,
            key='assessor'
        )
        
        # Filtra os dados pelo assessor selecionado
        df_assessor = df[df['Assessor'] == assessor_selecionado].copy()
        
        # Mostra estatísticas
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Clientes do Assessor", len(df_assessor))
        with col2:
            st.metric("Emissores Diferentes", len(df_assessor['Emissor'].unique()))
        with col3:
            st.metric("Posição Total", formatar_reais(df_assessor['Posição Total'].sum()))
        
        # Gráfico de pizza: Distribuição por emissor
        st.subheader("🥧 Distribuição por Emissor")
        
        distribuicao = df_assessor.groupby('Emissor')['Posição Total'].sum().reset_index()
        distribuicao = distribuicao.sort_values('Posição Total', ascending=False)
        
        fig_pizza = px.pie(
            distribuicao,
            values='Posição Total',
            names='Emissor',
            title='Distribuição da Posição por Emissor'
        )
        st.plotly_chart(fig_pizza, use_container_width=True)
        
        # Gráfico de barras: Clientes do assessor
        st.subheader("📊 Posições por Cliente")
        
        fig_barras = px.bar(
            df_assessor.head(15),  # Top 15 clientes
            x='Cliente',
            y='Posição Total',
            color='Emissor',
            title='Top 15 Clientes do Assessor',
            labels={'Posição Total': 'Posição (R$)', 'Cliente': 'Cliente'}
        )
        fig_barras.update_layout(height=500)
        st.plotly_chart(fig_barras, use_container_width=True)
        
        # Tabela detalhada
        st.subheader("📋 Detalhamento Completo")
        
        df_assessor_exibicao = df_assessor.copy()
        df_assessor_exibicao['Posição Total'] = df_assessor_exibicao['Posição Total'].apply(formatar_reais)
        
        st.dataframe(
            df_assessor_exibicao,
            use_container_width=True,
            hide_index=True
        )
        
        # Alerta para posições críticas (próximas ao limite de 250k)
        st.subheader("⚠️ Posições Críticas")
        st.info("Clientes próximos ao limite de R$ 250.000,00 (entre R$ 250k e R$ 280k)")
        
        # Filtra clientes que estão entre 250k e 280k (acabaram de ultrapassar)
        df_critico = df_assessor[
            (df_assessor['Posição Total'] >= 250000) & 
            (df_assessor['Posição Total'] <= 280000)
        ].copy()
        
        if len(df_critico) > 0:
            df_critico['Posição Total'] = df_critico['Posição Total'].apply(formatar_reais)
            st.dataframe(
                df_critico,
                use_container_width=True,
                hide_index=True
            )
        else:
            st.success("Nenhuma posição crítica encontrada!")

except FileNotFoundError:
    # Se o arquivo não for encontrado, mostra esta mensagem
    st.error("❌ Arquivo 'Alocação_FGC_-_Tauari.xlsx' não encontrado!")
    st.info("Por favor, coloque o arquivo Excel na mesma pasta do app.py")
except Exception as e:
    # Se houver qualquer outro erro, mostra a mensagem
    st.error(f"❌ Erro ao carregar os dados: {str(e)}")
    st.info("Verifique se o arquivo Excel está correto e tente novamente.")

# ========================================
# RODAPÉ
# ========================================
st.markdown("---")
st.markdown("Dashboard desenvolvido para análise de Alocação FGC")
