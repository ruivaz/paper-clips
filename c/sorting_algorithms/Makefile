CC=gcc
CFLAGS=-I.
DEPS = sort.h
OBJ = main.o sort.o

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

main: $(OBJ)
	gcc -o $@ $^ $(CFLAGS)
