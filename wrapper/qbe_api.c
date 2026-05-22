#include "../qbe/all.h"
#include "../qbe/config.h"
#include <string.h>

extern Target T_amd64_sysv;
extern Target T_amd64_apple;
extern Target T_amd64_win;
extern Target T_arm64;
extern Target T_arm64_apple;
extern Target T_rv64;

static Target *tlist[] = {&T_amd64_sysv,
                          &T_amd64_apple,
                          &T_amd64_win,
                          &T_arm64,
                          &T_arm64_apple,
                          &T_rv64,
                          0};

Target T;

static FILE *outf;

static void data(Dat *d) {
  emitdat(d, outf);
  if (d->type == DEnd)
    freeall();
}

static void func(Fn *fn) {
  T.abi0(fn);
  fillcfg(fn);
  filluse(fn);
  promote(fn);
  filluse(fn);
  ssa(fn);
  filluse(fn);
  ssacheck(fn);
  fillalias(fn);
  loadopt(fn);
  filluse(fn);
  fillalias(fn);
  coalesce(fn);
  filluse(fn);
  filldom(fn);
  ssacheck(fn);
  gvn(fn);
  fillcfg(fn);
  simplcfg(fn);
  filluse(fn);
  filldom(fn);
  gcm(fn);
  filluse(fn);
  ssacheck(fn);
  T.abi1(fn);
  simpl(fn);
  fillcfg(fn);
  filluse(fn);
  T.isel(fn);
  fillcfg(fn);
  filllive(fn);
  fillloop(fn);
  fillcost(fn);
  spill(fn);
  rega(fn);
  fillcfg(fn);
  simpljmp(fn);
  fillcfg(fn);
  T.emitfn(fn, outf);
  freeall();
}

static void dbgfile(char *fn) { emitdbgfile(fn, outf); }

static FILE *string_to_file(const char *s) {
#ifdef _WIN32
  FILE *f = tmpfile();
  fputs(s, f);
  rewind(f);
  return f;
#else
  return fmemopen((void *)s, strlen(s), "r");
#endif
}

int qbe_compile(const char *ir, const char *target,
                char *out_buf, int buf_size) {
  T = Deftgt;
  if (target){
    for (Target **t = tlist; *t; t++) {
      if (strcmp(target, (*t)->name) == 0) {
        T = **t;
        break;
      }
    }
  }

  FILE *inf = string_to_file(ir);
  outf = fmemopen(out_buf, buf_size, "w");

  parse(inf, "<string>", dbgfile, data, func);
  fclose(inf);

  T.emitfin(outf);
  fclose(outf);
  out_buf[buf_size - 1] = '\0';
  return 0;
}