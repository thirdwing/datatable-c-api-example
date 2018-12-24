#include <pybind11/pybind11.h>

#include "datatable.h"

namespace py = pybind11;

int nrow(py::object& pydt) {
  PyObject* dt = pydt.ptr();

  return DtFrame_NRows(dt);
}

PYBIND11_MODULE(example, m) { m.def("nrow", &nrow, ""); }
