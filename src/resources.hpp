#pragma once

#define RESOURCE_EXPORT(name)        \
    extern "C" unsigned char name[]; \
    extern "C" int name##_size;

RESOURCE_EXPORT(splash);

#undef RESOURCE_EXPORT
