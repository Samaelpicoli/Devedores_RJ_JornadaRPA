import pandas as pd

def concatenar_e_filtrar_dados(df, df_2):

    #Essa função faz a união dos 2 dataframes gerados durante a extração
    #das tabelas web, após fazer a união ele irá realizar o filtro de 
    #pagamentos pendentes de clientes do Rio de Janeiro, e assim gerar
    #o arquivo csv que ficará salvo na pasta do projeto.
    try:
        df_uniao = pd.concat([df, df_2], axis=1)
        df_final = df_uniao.loc[(df_uniao['cidade']=='Rio de Janeiro') & (df_uniao['pago']=='N')]
        df_final.to_csv('clientes_devedores_rj.csv', sep=',', encoding='utf-8', index=False)
    
    except Exception as error:
        print(f'Erro durante a união e filtro dos dados gerados: {error}')
        raise Exception('Erro durante a união e filtro dos dados gerados.')