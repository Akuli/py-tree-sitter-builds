# py-tree-sitter-builds

The [py-tree-sitter](https://pypi.org/project/tree-sitter/) project
(not to be confused with tree-sitter-python)
provides Python bindings for the awesome [tree-sitter](https://tree-sitter.github.io/) parsing library.
The documentation of py-tree-sitter says that you need to have a C compiler installed to use it,
but installing a C compiler can be highly non-trivial depending on which operating system you have.
It's also a huge dependency for what is otherwise a small and simple parsing library.

To use tree-sitter without a C compiler, you need to install two projects instead of `pip install tree-sitter`:
- tree-sitter-builds (this project)
- [tree-sitter-languages](https://pypi.org/project/tree-sitter-languages/)

These two projects provide binary wheels, i.e. platform-specific `.whl` files that don't require a C compiler to be installed with pip.


## Installation

```
$ pip install tree-sitter-builds
```

After installing, `import tree_sitter` should work.


## How does it work?

Read `.github/workflows/build.yml` to see how GitHub actions builds the wheels.
Here are the steps, at a high level:
- Download py-tree-sitter v0.20.0 from GitHub (latest released version at the time of writing this)
- Apply a patch to its tests to make them work when cibuildwheel runs them
- Invoke [cibuildwheel](https://github.com/pypa/cibuildwheel)
- Once the above steps have ran on Windows, MacOS and Linux, upload the wheels to PyPI


## License

py-tree-sitter and this project are both licensed under the MIT license.
[Here is the LICENSE file of py-tree-sitter.](https://github.com/tree-sitter/py-tree-sitter/blob/master/LICENSE)
[Here is the LICENSE file of this project.](https://github.com/Akuli/py-tree-sitter-builds)
