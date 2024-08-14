# C compiler
CC = gcc

# compiling flags
CFLAGS = -Wall -Wextra -fPIC

# library name
LIBNAME = libmathlib.so

# c archive to be compiled to library
SRC = mathlib.c

# compiles shared library
$(LIBNAME): $(SRC)
	$(CC) $(CFLAGS) -shared -o $(LIBNAME) $(SRC)

# run script python
run: $(LIBNAME)
	python app.py
