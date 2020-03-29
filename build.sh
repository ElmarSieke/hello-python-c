#!/bin/bash
gcc -c -Wall -Werror -fpic hello.c
gcc -shared -o libhello.so hello.o