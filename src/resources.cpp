#define RESOURCE(name, path)              \
    __asm__(                              \
        ".section .rodata\n"              \
        ".global " #name                  \
        "\n"                              \
        ".global " #name "_size\n" #name  \
        ":\n"                             \
        ".incbin \"" path                 \
        "\"\n"                            \
        ".byte 0\n"                       \
        ".type " #name                    \
        ", @object\n"                     \
        ".size " #name "_size, 1\n" #name \
        "_size:\n"                        \
        ".int " #name "_size - " #name    \
        "\n"                              \
        ".align 8\n")

RESOURCE(splash, "./src/splash.png");
