# py-tree-sitter-builds

The [py-tree-sitter](https://pypi.org/project/tree-sitter/) project
(not to be confused with tree-sitter-python)
provides Python bindings for the awesome [tree-sitter](https://tree-sitter.github.io/) parsing library.
The documentation of py-tree-sitter says that you need to have a C compiler installed to use it,
but installing a C compiler can be highly non-trivial depending on which operating system you have.
It's also a huge dependency for what is otherwise a small and simple parsing library.

To use tree-sitter without a C compiler, you need to install two projects instead of `pip install tree-sitter`:
- py-tree-sitter-builds (this project)
- [tree-sitter-languages](https://pypi.org/project/tree-sitter-languages/)

These two projects provide binary wheels, i.e. platform-specific `.whl` files that don't require a C compiler to be installed with pip.


## Installation

This project is currently not published to PyPI, so installation is a bit of a mess:
1. Download the correct wheel file from [the releases page](https://github.com/Akuli/py-tree-sitter-builds/releases).
    For example, if you have:
    - Python 3.9 installation (`cp39`)
    - A typical Linux distribution (`manylinux`)
    - 64-bit Intel CPU (`x86_64`, if you are not sure try `import platform; print(platform.machine())`)

    you would choose `tree_sitter-0.20.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl`.

2. Run `pip install path/to/downloaded/file.whl`, for example `pip install Downloads/tree_sitter-0.20.0-cp39-cp39-musllinux_1_1_x86_64.whl`.

For a more permanent solution, I will probably publish this project on PyPI
unless the py-tree-sitter maintainers are interested in making this a part of the official `py-tree-sitter` repository.

If you want to use this project in a `requirements.txt`,
you should realistically just wait until something is properly published on PyPI.

<details>
<summary>A mess you can put to your requirements.txt if you don't want to wait</summary>

```
# Install py-tree-sitter 0.20.0 from github.com/Akuli/py-tree-sitter-builds.
# 32-bit linux
tree-sitter @ https://github.com/Akuli/py-tree-sitter-builds/releases/download/v2022-08-24/tree_sitter-0.20.0-cp36-cp36m-manylinux_2_17_i686.manylinux2014_i686.whl ; python_version == '3.6' and sys_platform == 'linux' and platform_machine == 'i686'
tree-sitter @ https://github.com/Akuli/py-tree-sitter-builds/releases/download/v2022-08-24/tree_sitter-0.20.0-cp37-cp37m-manylinux_2_17_i686.manylinux2014_i686.whl ; python_version == '3.7' and sys_platform == 'linux' and platform_machine == 'i686'
tree-sitter @ https://github.com/Akuli/py-tree-sitter-builds/releases/download/v2022-08-24/tree_sitter-0.20.0-cp38-cp38-manylinux_2_17_i686.manylinux2014_i686.whl ; python_version == '3.8' and sys_platform == 'linux' and platform_machine == 'i686'
tree-sitter @ https://github.com/Akuli/py-tree-sitter-builds/releases/download/v2022-08-24/tree_sitter-0.20.0-cp39-cp39-manylinux_2_17_i686.manylinux2014_i686.whl ; python_version == '3.9' and sys_platform == 'linux' and platform_machine == 'i686'
tree-sitter @ https://github.com/Akuli/py-tree-sitter-builds/releases/download/v2022-08-24/tree_sitter-0.20.0-cp310-cp310-manylinux_2_17_i686.manylinux2014_i686.whl ; python_version == '3.10' and sys_platform == 'linux' and platform_machine == 'i686'
tree-sitter @ https://github.com/Akuli/py-tree-sitter-builds/releases/download/v2022-08-24/tree_sitter-0.20.0-cp311-cp311-manylinux_2_17_i686.manylinux2014_i686.whl ; python_version == '3.11' and sys_platform == 'linux' and platform_machine == 'i686'
# 64-bit linux
tree-sitter @ https://github.com/Akuli/py-tree-sitter-builds/releases/download/v2022-08-24/tree_sitter-0.20.0-cp36-cp36m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl ; python_version == '3.6' and sys_platform == 'linux' and platform_machine == 'x86_64'
tree-sitter @ https://github.com/Akuli/py-tree-sitter-builds/releases/download/v2022-08-24/tree_sitter-0.20.0-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl ; python_version == '3.7' and sys_platform == 'linux' and platform_machine == 'x86_64'
tree-sitter @ https://github.com/Akuli/py-tree-sitter-builds/releases/download/v2022-08-24/tree_sitter-0.20.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl ; python_version == '3.8' and sys_platform == 'linux' and platform_machine == 'x86_64'
tree-sitter @ https://github.com/Akuli/py-tree-sitter-builds/releases/download/v2022-08-24/tree_sitter-0.20.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl ; python_version == '3.9' and sys_platform == 'linux' and platform_machine == 'x86_64'
tree-sitter @ https://github.com/Akuli/py-tree-sitter-builds/releases/download/v2022-08-24/tree_sitter-0.20.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl ; python_version == '3.10' and sys_platform == 'linux' and platform_machine == 'x86_64'
tree-sitter @ https://github.com/Akuli/py-tree-sitter-builds/releases/download/v2022-08-24/tree_sitter-0.20.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl ; python_version == '3.11' and sys_platform == 'linux' and platform_machine == 'x86_64'
# 32-bit windows
tree-sitter @ https://github.com/Akuli/py-tree-sitter-builds/releases/download/v2022-08-24/tree_sitter-0.20.0-cp36-cp36m-win32.whl ; python_version == '3.6' and sys_platform == 'win32' and platform_machine == 'x86'
tree-sitter @ https://github.com/Akuli/py-tree-sitter-builds/releases/download/v2022-08-24/tree_sitter-0.20.0-cp37-cp37m-win32.whl ; python_version == '3.7' and sys_platform == 'win32' and platform_machine == 'x86'
tree-sitter @ https://github.com/Akuli/py-tree-sitter-builds/releases/download/v2022-08-24/tree_sitter-0.20.0-cp38-cp38-win32.whl ; python_version == '3.8' and sys_platform == 'win32' and platform_machine == 'x86'
tree-sitter @ https://github.com/Akuli/py-tree-sitter-builds/releases/download/v2022-08-24/tree_sitter-0.20.0-cp39-cp39-win32.whl ; python_version == '3.9' and sys_platform == 'win32' and platform_machine == 'x86'
tree-sitter @ https://github.com/Akuli/py-tree-sitter-builds/releases/download/v2022-08-24/tree_sitter-0.20.0-cp310-cp310-win32.whl ; python_version == '3.10' and sys_platform == 'win32' and platform_machine == 'x86'
tree-sitter @ https://github.com/Akuli/py-tree-sitter-builds/releases/download/v2022-08-24/tree_sitter-0.20.0-cp311-cp311-win32.whl ; python_version == '3.11' and sys_platform == 'win32' and platform_machine == 'x86'
# 64-bit windows
tree-sitter @ https://github.com/Akuli/py-tree-sitter-builds/releases/download/v2022-08-24/tree_sitter-0.20.0-cp36-cp36m-win_amd64.whl ; python_version == '3.6' and sys_platform == 'win32' and platform_machine == 'AMD64'
tree-sitter @ https://github.com/Akuli/py-tree-sitter-builds/releases/download/v2022-08-24/tree_sitter-0.20.0-cp37-cp37m-win_amd64.whl ; python_version == '3.7' and sys_platform == 'win32' and platform_machine == 'AMD64'
tree-sitter @ https://github.com/Akuli/py-tree-sitter-builds/releases/download/v2022-08-24/tree_sitter-0.20.0-cp38-cp38-win_amd64.whl ; python_version == '3.8' and sys_platform == 'win32' and platform_machine == 'AMD64'
tree-sitter @ https://github.com/Akuli/py-tree-sitter-builds/releases/download/v2022-08-24/tree_sitter-0.20.0-cp39-cp39-win_amd64.whl ; python_version == '3.9' and sys_platform == 'win32' and platform_machine == 'AMD64'
tree-sitter @ https://github.com/Akuli/py-tree-sitter-builds/releases/download/v2022-08-24/tree_sitter-0.20.0-cp310-cp310-win_amd64.whl ; python_version == '3.10' and sys_platform == 'win32' and platform_machine == 'AMD64'
tree-sitter @ https://github.com/Akuli/py-tree-sitter-builds/releases/download/v2022-08-24/tree_sitter-0.20.0-cp311-cp311-win_amd64.whl ; python_version == '3.11' and sys_platform == 'win32' and platform_machine == 'AMD64'
# 64-bit Intel Mac
tree-sitter @ https://github.com/Akuli/py-tree-sitter-builds/releases/download/v2022-08-24/tree_sitter-0.20.0-cp36-cp36m-macosx_10_9_x86_64.whl ; python_version == '3.6' and sys_platform == 'darwin' and platform_machine == 'x86_64'
tree-sitter @ https://github.com/Akuli/py-tree-sitter-builds/releases/download/v2022-08-24/tree_sitter-0.20.0-cp37-cp37m-macosx_10_9_x86_64.whl ; python_version == '3.7' and sys_platform == 'darwin' and platform_machine == 'x86_64'
tree-sitter @ https://github.com/Akuli/py-tree-sitter-builds/releases/download/v2022-08-24/tree_sitter-0.20.0-cp38-cp38-macosx_10_9_x86_64.whl ; python_version == '3.8' and sys_platform == 'darwin' and platform_machine == 'x86_64'
tree-sitter @ https://github.com/Akuli/py-tree-sitter-builds/releases/download/v2022-08-24/tree_sitter-0.20.0-cp39-cp39-macosx_10_9_x86_64.whl ; python_version == '3.9' and sys_platform == 'darwin' and platform_machine == 'x86_64'
tree-sitter @ https://github.com/Akuli/py-tree-sitter-builds/releases/download/v2022-08-24/tree_sitter-0.20.0-cp310-cp310-macosx_10_9_x86_64.whl ; python_version == '3.10' and sys_platform == 'darwin' and platform_machine == 'x86_64'
tree-sitter @ https://github.com/Akuli/py-tree-sitter-builds/releases/download/v2022-08-24/tree_sitter-0.20.0-cp311-cp311-macosx_10_9_x86_64.whl ; python_version == '3.11' and sys_platform == 'darwin' and platform_machine == 'x86_64'
# M1 Mac
tree-sitter @ https://github.com/Akuli/py-tree-sitter-builds/releases/download/v2022-08-24/tree_sitter-0.20.0-cp38-cp38-macosx_11_0_arm64.whl ; python_version == '3.8' and sys_platform == 'darwin' and platform_machine == 'arm64'
tree-sitter @ https://github.com/Akuli/py-tree-sitter-builds/releases/download/v2022-08-24/tree_sitter-0.20.0-cp39-cp39-macosx_11_0_arm64.whl ; python_version == '3.9' and sys_platform == 'darwin' and platform_machine == 'arm64'
tree-sitter @ https://github.com/Akuli/py-tree-sitter-builds/releases/download/v2022-08-24/tree_sitter-0.20.0-cp310-cp310-macosx_11_0_arm64.whl ; python_version == '3.10' and sys_platform == 'darwin' and platform_machine == 'arm64'
tree-sitter @ https://github.com/Akuli/py-tree-sitter-builds/releases/download/v2022-08-24/tree_sitter-0.20.0-cp311-cp311-macosx_11_0_arm64.whl ; python_version == '3.11' and sys_platform == 'darwin' and platform_machine == 'arm64'
```

</details>


## How does it work?

Read `.github/workflows/build.yml` to see how GitHub actions builds the wheels.
Here are the steps, at a high level:
- Download py-tree-sitter v0.20.0 from GitHub (latest released version at the time of writing this)
- Apply a patch to its tests to make them work when cibuildwheel runs them
- Invoke [cibuildwheel](https://github.com/pypa/cibuildwheel)
- Once the above steps have ran on Windows, MacOS and Linux, create a release on GitHub and upload the wheels there


## License

py-tree-sitter and this project are both licensed under the MIT license.
[Here is the LICENSE file of py-tree-sitter.](https://github.com/tree-sitter/py-tree-sitter/blob/master/LICENSE)
[Here is the LICENSE file of this project.](https://github.com/Akuli/py-tree-sitter-builds)
