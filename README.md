# Fork of PyXivData
Aims to let you access game resources with the least amount of friction.

Work in progress.

# Usage
The package is not published to PyPI. You can still use it by targeting this GitHub repo directly.

[!IMPORTANT]
You need to target `dist` branch or a specific commit. `main` branch contains original upstream code

With pip ([docs](https://pip.pypa.io/en/latest/topics/vcs-support/#git)):
```
python3 -m pip install "pyxivdata @ git+https://github.com/tabasavr/pyxivdata.git@dist"
```

With uv ([docs](https://docs.astral.sh/uv/pip/packages/#installing-a-package)):
```
uv pip install "git+https://github.com/tabasavr/pyxivdata.git@dist"
```

# Versioning
Since this package depends on EXDSchema, it uses an unusual versioning scheme that consists of two part. The beginning is semver-like `major.minor.patch` that covers everything except generated row definitions. The suffix matches EXDSchema's version

```
major.minor.patch.EXDSchema
```

# Diff to original
Added support for [EXDSchema](https://github.com/xivdev/EXDSchema).

Added codegen based on EXDSchema for code completion support.

# Updating EXDSchema
1. Update `codegen/EXDSchema` submodule
2. Run `codegen/gen.py`. Requires pyyaml or similar  (e.g. `uv run --with pyyaml codegen/gen.py`)
3. Update `version` in `pyproject.toml`
