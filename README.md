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

This project is not released anywhere yet.
Once it is released somewhere,
I will update this README with installation instructions.

Read `.github/workflows/build.yml` to see how the wheels are built.
It basically downloads py-tree-sitter v0.20.0 (latest released version at the time of writing this)
and invokes [cibuildwheel](https://github.com/pypa/cibuildwheel).


## Supported platforms

- Windows, MacOS or Linux.
    - Newer, arm-based macs are supported only when using Python compiled for Intel (x86_64) processors. Please create an issue if this is a problem for you.
- Python 3.6 or newer.

Binary wheels for using py-tree-sitter without a C compiler.


## License

py-tree-sitter and this project are both licensed under the MIT license.
[Here is the LICENSE file of py-tree-sitter.](https://github.com/tree-sitter/py-tree-sitter/blob/master/LICENSE)
[Here is the LICENSE file of this project.](https://github.com/Akuli/py-tree-sitter-builds)


## TODO

- Usage/installation/requirements.txt instructions, or a release on pypi?
- Use this thing in Porcupine
- Post a comment to https://github.com/tree-sitter/py-tree-sitter/issues/103
