project(
    'pyqbe',
    'c',
    'cpp',
    version: '0.1.0',
    default_options: [
        'cpp_std=c++11',
    ],
)

py = import('python').find_installation(pure: false)
pybind11_dep = dependency('pybind11')

# --- START WINDOWS MSVC COMPATIBILITY LAYER ---
cc = meson.get_compiler('c')

if cc.get_id() == 'msvc'
  extra_c_args = [
    '-D__attribute__(x)=', # Nullify GCC attributes for MSVC
    '/wd4146'              # Suppress unary minus unsigned warnings
  ]
  
  # This automatically applies the flags to all C files compiled in this project
  add_project_arguments(extra_c_args, language: 'c')
endif
# --- END WINDOWS MSVC COMPATIBILITY LAYER ---
wrapper_sources = [
    'wrapper/binding.cpp',
    'wrapper/qbe_api.c',
]

qbe_sources = [
    'qbe/util.c',
    'qbe/parse.c',
    'qbe/abi.c',
    'qbe/cfg.c',
    'qbe/mem.c',
    'qbe/ssa.c',
    'qbe/alias.c',
    'qbe/load.c',
    'qbe/copy.c',
    'qbe/fold.c',
    'qbe/gvn.c',
    'qbe/gcm.c',
    'qbe/simpl.c',
    'qbe/ifopt.c',
    'qbe/live.c',
    'qbe/spill.c',
    'qbe/rega.c',
    'qbe/emit.c',
    'qbe/amd64/targ.c',
    'qbe/amd64/sysv.c',
    'qbe/amd64/isel.c',
    'qbe/amd64/emit.c',
    'qbe/amd64/winabi.c',
    'qbe/arm64/targ.c',
    'qbe/arm64/abi.c',
    'qbe/arm64/isel.c',
    'qbe/arm64/emit.c',
    'qbe/rv64/targ.c',
    'qbe/rv64/abi.c',
    'qbe/rv64/isel.c',
    'qbe/rv64/emit.c',
]

combined_sources = wrapper_sources + qbe_sources

py.extension_module('_pyqbe',
    combined_sources,
    install: true,
    dependencies : [pybind11_dep],
    include_directories: 'qbe',
)

# Install pure Python package
py.install_sources(
    'pyqbe/__init__.py',
    'pyqbe/_core.pyi',
    subdir: 'pyqbe',
)

# Generate config.h
run_command('python', 'wrapper/gen_config.py', check: true)