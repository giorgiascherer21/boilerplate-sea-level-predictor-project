import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
   
    # Resumo: Lê os dados do nível do mar, cria um gráfico de dispersão e plota duas linhas de regressão para prever o aumento do nível do mar até 2050.
    # A primeira linha usa todos os dados e a segunda usa dados a partir do ano 2000.
   
    # 1. Leitura dos Dados
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Criação do Gráfico Inicial
    # Configura a figura e os eixos para o gráfico. `figsize` melhora a visualização.
    fig, ax = plt.subplots(figsize=(12, 6))
    # Plota os dados originais como um gráfico de dispersão (scatter plot).
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # 3. Primeira Linha de Regressão (Dados Completos)
    # Calcula a inclinação (slope) e o intercepto para todos os dados.
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    # Cria uma série de anos de 1880 a 2050 para traçar a linha de previsão.
    x_pred = pd.Series(range(1880, 2051))
    # Calcula os valores de Y (nível do mar) para a linha de previsão.
    y_pred = res.slope * x_pred + res.intercept
    # Plota a linha de regressão em vermelho.
    ax.plot(x_pred, y_pred, 'r')

    # 4. Segunda Linha de Regressão (Dados Recentes)
    # Filtra o DataFrame para obter dados a partir do ano 2000.
    df_recent = df[df['Year'] >= 2000]
    # Calcula a regressão linear apenas para os dados recentes.
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    # Cria uma série de anos de 2000 a 2050 para a nova linha.
    x_pred_recent = pd.Series(range(2000, 2051))
    # Calcula os valores de Y para a segunda linha de previsão.
    y_pred_recent = res_recent.slope * x_pred_recent + res_recent.intercept
    # Plota a segunda linha de regressão em verde.
    ax.plot(x_pred_recent, y_pred_recent, 'green')

    # 5. Configuração de Rótulos e Título
    # Define os rótulos dos eixos e o título para tornar o gráfico compreensível.
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.set_xticks(range(1850, 2100, 25))

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

# Para visualização 
if __name__ == "__main__":
    draw_plot()
    plt.show()