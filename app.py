from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd

app = Flask(__name__)

# Configurar a chave secreta da sessão(indicado pela IA)
app.secret_key = '1234'

def carregar_planilha(nome_arquivo, header=None):
    try:
        df = pd.read_excel(nome_arquivo, header=header)
        return df
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    df = None
    resultados = []
    
    
    if request.method == 'POST':
        arquivo = request.files['planilha']
        if arquivo and arquivo.filename.endswith('.xlsx'):
            df = carregar_planilha(arquivo, header=None)

            if df is not None:
                    # Restante do seu código para buscar os nomes procurados e processar os resultados
                    #nomes_procurados = ['Francisca', 'Michel', 'Marcos' ]  # Lista de nomes a serem procurados
                   
                    nomes_procurados = df.iloc[1, 17].split(',')
                    #print(nomes_procurados)

                    # Obtenha o nome da coluna da linha 2
                    nomes_colunas = df.iloc[1]

                    resultados_por_nome = {}

                    for index, row in df.iterrows():
                        if index < 2:
                            continue
                        for coluna in df.columns:
                            for nome_procurado in nomes_procurados:
                                if nome_procurado in str(row[coluna]):
                                    #print(f"Nome encontrado: {nome_procurado}")
                                    dia_do_mes = row[df.columns[0]]  
                                    dia_da_semana = row[df.columns[1]]  
                                    nome_coluna = nomes_colunas[coluna]
                                    resultados.append((dia_do_mes, dia_da_semana, nome_coluna))

                                    if nome_procurado not in resultados_por_nome:
                                        resultados_por_nome[nome_procurado] = []
                                    resultados_por_nome[nome_procurado].append((dia_do_mes, dia_da_semana, nome_coluna))

                    session['nomes_procurados'] = nomes_procurados
                    session['resultados_por_nome'] = resultados_por_nome
                    session['resultados'] = resultados
                    
                    print(resultados_por_nome)

            return redirect(url_for('exibir_resultados'))

    return render_template('index.html', df=df)


@app.route('/resultados', methods=['GET'])
def exibir_resultados():

    resultados = session.get('resultados', [])

    #print(resultados)

    nomes_procurados = session.get('nomes_procurados', '')

    #print(nomes_procurados)

    resultados_por_nome = session.get('resultados_por_nome', {})

    #print(resultados_por_nome)

    return render_template('results.html', nomes_procurados=nomes_procurados, resultados_por_nome=resultados_por_nome, resultados=resultados)



if __name__ == '__main__':
    app.run(debug=True)