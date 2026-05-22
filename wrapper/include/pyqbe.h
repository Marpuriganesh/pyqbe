#ifndef PYQBE_H
#define PYQBE_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef struct {
  char *data;
  size_t len;
  size_t cap;
} QBE_Buffer;

// void qbe_buffer_init(QBE_Buffer *buf);

// void qbe_buffer_free(QBE_Buffer *buf);

int qbe_compile(const char *ir, const char *target, QBE_Buffer *buf);

#ifdef __cplusplus
}
#endif

#endif