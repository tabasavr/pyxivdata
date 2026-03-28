# Fork of PyXivData
Aims to let you access game resources with the least amount of friction.

Work in progress.

# Diff to original
Added support for [EXDSchema](https://github.com/xivdev/EXDSchema).

Added codegen based on EXDSchema for code completion support.

# Updating EXDSchema
1. Update `codegen/EXDSchema` submodule
2. Run `codegen/gen.py`. Requires pyyaml or similar  (e.g. `uv run --with pyyaml codegen/gen.py`)
