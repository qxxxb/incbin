#include <stdio.h>

#ifndef LIB_PASSTHROUGH
#ifdef GENERATE_RESOURCES
#include "generated/resources.hpp"
#else
#include "resources.hpp"
#endif
#endif

void show_splash()
{
#ifdef LIB_PASSTHROUGH
    printf("pass\n");
#else
    printf("splash = %p\n", splash);
    printf("splash_size = %i\n", splash_size);

    for (int i = 0; i < 48; ++i) {
        printf("%02x", (unsigned char)splash[i]);
    }
    printf("\n");
#endif
}
