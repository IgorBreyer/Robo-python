<h1 align="left">Excel Data Cleaner</h1>

Este é um simples script em Python para limpeza de dados em arquivos do Excel. Ele lê um arquivo Excel, remove linhas que possuem todos os valores nulos e salva o arquivo limpo em um novo local especificado.

<h2 align="left">Pré-requisitos</h2>
Python 3.x
Biblioteca Pandas

<h2 align="left">Instalação das Dependências</h2>
Certifique-se de que você tenha o Python instalado em sua máquina. Para instalar a biblioteca Pandas, você pode executar o seguinte comando:

```
pip install pandas
```

<h2 align="left">Como Usar</h2>
Faça o download ou clone este repositório em sua máquina local.

Abra o arquivo index.py em um editor de texto de sua escolha ou IDE.

Especifique o local do arquivo Excel original que você deseja limpar no seguinte trecho de código:

```
df = pd.read_excel(r'Especificar o local do arquivo original aqui.')
```

Especifique o local de salvamento do novo arquivo limpo no seguinte trecho de código:

```
escrever = pd.ExcelWriter(r'Especificar o local de salvamento do novo arquivo aqui.')
```

Salve suas alterações.

Abra um terminal e navegue até o diretório onde você salvou o script.

Execute o script Python:

python excel_data_cleaner.py

Aguarde até que o processo de limpeza seja concluído. O script aguardará 10 segundos após a execução antes de fechar.

<h2 align="left">Observações</h2>
Certifique-se de fornecer o caminho correto para o arquivo Excel original e o caminho onde deseja salvar o novo arquivo limpo.
Este script trata exceções básicas. Certifique-se de manipular exceções adequadamente em produção.
