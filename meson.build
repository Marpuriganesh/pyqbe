project(
    'pyqbe',
    'cpp',
    version: '0.1.0',
    default_options: [
        'cpp_std=c++11',
    ],
)

py = import('python').find_installation(pure: false)
pybind11_dep = dependency('pybind11')

py.extension_module('pyqbe',
    'pyqbe.cpp',
    install: true,
    dependencies : [pybind11_dep],
)