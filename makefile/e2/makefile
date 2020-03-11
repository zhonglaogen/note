CC=gcc

test:test.c tool.o
	$(CC) test.c tool.o -o test

tool.o:tool.c
	$(CC) -c tool.c

clean:
	rm *.o main

