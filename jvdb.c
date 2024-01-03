#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    FILE *archivo;
    archivo = fopen("basededatos.txt", "a");
    char *texto = argv[1];
    strcat(texto, "\n");
    fputs(texto, archivo);
    fclose(archivo);
    return 0;
}

