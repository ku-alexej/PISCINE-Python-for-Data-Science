# ft_package

`ft_package` is a simple educational Python package created for learning how to build and distribute Python packages.

It provides a single function:

```python
count_in_list(lst: list, to_count: any) -> int
```

This function counts and returns the number of occurrences of `to_count` in the given list.

## Build the package

Install the build tool:

```bash
pip install build
```

Build the package:

```bash
python -m build
```

## Install the package

From the source distribution:

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```

Or from the wheel:

```bash
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

## Verify the installation

List installed packages:

```bash
pip list
```

Show information about the package:

```bash
pip show -v ft_package
```

## Usage

```bash
python3 -c "from ft_package import count_in_list; print(count_in_list(['toto', 'tata', 'toss'], 'toss'))"
```

```
pip uninstall ft_package
```