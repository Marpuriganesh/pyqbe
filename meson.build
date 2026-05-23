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

# Add your static linking flags specifically for Windows environments
extra_link_args = []
if host_machine.system() == 'windows'
    extra_link_args += [
        '-static',
        '-static-libgcc',
        '-static-libstdc++',
    ]
endif

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
    link_args: extra_link_args, # Apply the static linking here
)

# Install pure Python package
py.install_sources(
    'pyqbe/__init__.py',
    'pyqbe/_core.pyi',
    subdir: 'pyqbe',
)

# Generate config.h
run_command('python', 'wrapper/gen_config.py', check: true)