#include "include/pyqbe.h"
#include <pybind11/pybind11.h>
#include <string>

namespace py = pybind11;
using namespace std;

string compile(const char *ir, const char *target) {
  QBE_Buffer buf = {0};
  qbe_compile(ir, target, &buf);
  string result(buf.data);
  free(buf.data);
  return result;
}

PYBIND11_MODULE(_pyqbe, m) {
  m.doc() = "Python bindings for QBE compiler backend";
  m.def("compile", &compile,
        R"doc(
Compile QBE IR to target assembly.

Args:
    ir: QBE IR string to compile
    target: Target architecture. One of: amd64_sysv, amd64_apple, amd64_win,
            arm64, arm64_apple, rv64. Defaults to current platform.

Returns:
    Assembly string for the target architecture.
)doc",
        py::arg("ir"), py::arg("target") = nullptr);
}