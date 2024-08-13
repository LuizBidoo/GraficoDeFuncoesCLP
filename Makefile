# Nome do compilador
CC = gcc

# Flags de compilação
CFLAGS = -Wall -Wextra -fPIC

# Nome da biblioteca
LIBNAME = libmathlib.so

# Arquivo C a ser compilado
SRC = mathlib.c

# Diretórios
BUILD_DIR = build

# Cria a biblioteca compartilhada
$(LIBNAME): $(SRC)
	$(CC) $(CFLAGS) -shared -o $(LIBNAME) $(SRC)

# Executa o script Python
run: $(LIBNAME)
	python app.py
