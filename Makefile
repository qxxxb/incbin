all: main lib.so

CC=g++-10
# CC=clang++-10

lib.so: src/* Makefile
	$(CC) -shared -o lib.so -fPIC src/lib.cpp src/resources.cpp

main: lib.so src/* Makefile
	$(CC) -L. -Wl,-rpath=. -o main src/main.cpp -l:lib.so
