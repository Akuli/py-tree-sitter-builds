# py-tree-sitter-builds

The [py-tree-sitter](https://pypi.org/project/tree-sitter/) project
(not to be confused with tree-sitter-python)
provides Python bindings for the awesome [tree-sitter](https://tree-sitter.github.io/) parsing library.
The documentation of py-tree-sitter says that you need to have a C compiler installed to use it,
but installing a C compiler can be highly non-trivial depending on which operating system you have.
It's also a huge dependency for what is otherwise a small and simple parsing library.

This project lets you use py-tree-sitter without a C compiler
by providing binary wheels that were built using a C compiler,
but don't require a C compiler to be installed.
The wheels contain:
- the `tree_sitter` module from [py-tree-sitter](https://pypi.org/project/tree-sitter/) v0.20.0
- the `tree_sitter_languages` module from [py-tree-sitter-languages](https://pypi.org/project/tree-sitter-languages/) v1.4.0


## Installation

```
$ pip install tree-sitter-builds
```

After installing, `import tree_sitter` and `import tree_sitter_languages` should work.
For documentation, see the documentation of:
- [py-tree-sitter-languages](https://pypi.org/project/tree-sitter-languages/1.4.0/)
- [py-tree-sitter](https://pypi.org/project/tree-sitter/0.20.0/) (use `tree_sitter_languages` instead of the "Setup" part)


## How does it work?

Read `.github/workflows/build.yml` to see how GitHub actions builds the wheels.
Here are the steps, at a high level:
- Download py-tree-sitter v0.20.0 and py-tree-sitter-languages v1.4.0 from GitHub
    (these are the latest released versions at the time of writing this)
- Create a `tests` directory that contains the tests from both of them
- Edit py-tree-sitter's tests to use py-tree-sitter-languages
- Invoke [cibuildwheel](https://github.com/pypa/cibuildwheel) with the same configuration as py-tree-sitter-languages uses
- Once the above steps have ran on Windows, MacOS and Linux, upload the wheels to PyPI


## License

py-tree-sitter and this project are both licensed under the MIT license.
[Here is the LICENSE file of py-tree-sitter.](https://github.com/tree-sitter/py-tree-sitter/blob/master/LICENSE)
[Here is the LICENSE file of this project.](https://github.com/Akuli/py-tree-sitter-builds/blob/main/LICENSE)
