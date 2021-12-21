#include <stdio.h>
#include "lib.hpp"

#ifdef GENERATE_RESOURCES
#include "generated/resources.hpp"
#else
#include "resources.hpp"
#endif

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
