import sys
from datetime import datetime

from Cython.Build import cythonize
from setuptools import Extension, setup

with open("README.md") as file:
    readme_text = file.read()

setup(
    name="tree_sitter_builds",
    version=datetime.utcnow().strftime("%Y.%m.%d"),  # Only used while building wheels
    description="Python bindings to the Tree-sitter parsing library",
    long_description=readme_text,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    author="Akuli",
    author_email="akuviljanen17@gmail.com",
    url="https://github.com/Akuli/py-tree-sitter-builds",
    project_urls={
        "Documentation": "https://github.com/Akuli/py-tree-sitter-builds",
        "Source": "https://github.com/Akuli/py-tree-sitter-builds",
        "Tracker": "https://github.com/Akuli/py-tree-sitter-builds/issues",
    },
    license="Apache 2.0",
    packages=["tree_sitter", "tree_sitter_languages"],
    ext_modules=[
        # tree_sitter
        Extension(
            "tree_sitter.binding",
            ["tree_sitter/core/lib/src/lib.c", "tree_sitter/binding.c"],
            include_dirs=["tree_sitter/core/lib/include", "tree_sitter/core/lib/src"],
            extra_compile_args=(
                None
                if sys.platform == "win32"
                else ["-std=c99", "-Wno-unused-variable"]
            ),
        ),
        # tree_sitter_languages
        *cythonize("tree_sitter_languages/core.pyx", language_level="3"),
    ],
    package_data={"tree_sitter_languages": ["languages.so", "languages.dll"]},
)
