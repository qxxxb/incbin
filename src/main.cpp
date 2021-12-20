#include <stdio.h>
#include "lib.hpp"
#include "resources.hpp"

void main_show_splash() {
    printf("splash = %p\n", splash);
    printf("splash_size = %i\n", splash_size);

    for (int i = 0; i < 48; ++i) {
        printf("%02x", (unsigned char)splash[i]);
    }
    printf("\n");
}

int main() {
    show_splash();
    main_show_splash();
}
