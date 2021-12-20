#include <stdio.h>
#include "resources.hpp"

void show_splash()
{
    printf("splash = %p\n", splash);
    printf("splash_size = %i\n", splash_size);

    for (int i = 0; i < 48; ++i) {
        printf("%02x", (unsigned char)splash[i]);
    }
    printf("\n");
}
