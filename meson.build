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

# 1. Native cross-platform config.h generation
cdata = configuration_data()

# Detect host architecture to choose the correct target backend string
host_cpu = host_machine.cpu_family()
if host_cpu == 'x86_64'
    cdata.set_quoted('Deftarg', 'amd64')
elif host_cpu == 'aarch64'
    cdata.set_quoted('Deftarg', 'arm64')
elif host_cpu == 'riscv64'
    cdata.set_quoted('Deftarg', 'rv64')
else
    error('Unsupported architecture: ' + host_cpu)
endif

# Dynamically generate config.h in the build directory
configure_file(
    output: 'config.h',
    configuration: cdata
)


py.extension_module('_pyqbe',
    'wrapper/binding.cpp',
    'wrapper/qbe_api.c',
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
run_command('make', '-C', 'qbe', 'config.h', check: true)