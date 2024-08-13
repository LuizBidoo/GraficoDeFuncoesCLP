# Projeto de Funções Matemáticas

Este projeto implementa uma biblioteca C para funções matemáticas, que é utilizada em um script Python para gerar gráficos de funções quadráticas.

## Estrutura do Projeto

- **mathlib.c**: Contém a implementação da função quadrática em C.
- **app.py**: Script Python que carrega a biblioteca C, calcula os valores da função quadrática e gera um gráfico.
- **Makefile**: Script de automação para compilar a biblioteca C e executar o script Python.

## Compilação e Execução

Para compilar a biblioteca C e executar o script Python, siga os passos abaixo:

1. **Compilar a biblioteca**:
   ```bash
   make
2. **Executar script python**:
   ```bash
   make run
### Extra: Execução manual:

1. **Compilar a biblioteca**:
   ```bash
   gcc -Wall -Wextra -fPIC -shared -o libmathlib.dll mathlib.c
2. **Executar script python**:
   ```bash
   python app.py
## Requisitos:
- GCC: Para compilar o código C e gerar a biblioteca compartilhada.
- Python 3: Para executar o script Python. Com as bibliotecas que serão listadas.
- Make: Para executar o makefile.

## Bibliotecas necessárias e instalação:
1. **ctypes**: Nativa!

2. **os**: Nativa!

3. **tkinter**: Nativa!

4. **numpy**:
   ```bash
   pip install numpy
5. **matplotlib**:
    ```bash
   pip install matplotlib
