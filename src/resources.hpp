#pragma once

#ifdef ATTRIBUTE_WEAK
#ifdef CONST
#define RESOURCE_EXPORT(name)                                    \
    extern "C" const unsigned char __attribute__((weak)) name[]; \
    extern "C" const int __attribute__((weak)) name##_size;
#else
#define RESOURCE_EXPORT(name)                              \
    extern "C" unsigned char __attribute__((weak)) name[]; \
    extern "C" int __attribute__((weak)) name##_size;
#endif
#else
#ifdef CONST
#define RESOURCE_EXPORT(name)              \
    extern "C" const unsigned char name[]; \
    extern "C" const int name##_size;
#else
#define RESOURCE_EXPORT(name)        \
    extern "C" unsigned char name[]; \
    extern "C" int name##_size;
#endif
#endif

RESOURCE_EXPORT(splash)

#undef RESOURCE_EXPORT
