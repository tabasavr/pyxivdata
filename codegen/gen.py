import os
import yaml
import typing
from pathlib import Path

def __main__() -> typing.Any:
    schema_dir = Path(__file__).parent / "EXDSchema"
    rowdef_path = Path(__file__).parent.parent / "src" / "pyxivdata" / "resource" / "excel" / "rowdef.py"
    with open(rowdef_path, "w") as rowdef:
        print("from pyxivdata.resource.excel.reader import ExdRow", file=rowdef)
        print("import typing", file=rowdef)
        print("", file=rowdef)

        for path in schema_dir.glob("*.yml"):
            print(path)
            with open(path, "r") as file:
                yml = yaml.safe_load(file)
                print(f"class {yml["name"]}Row(ExdRow):", file=rowdef)

                if "displayField" in yml:
                    print(f"    _display_field: str = '{yml["displayField"]}'", file=rowdef)
                    print(f"", file=rowdef)

                idx = 0
                for field in yml["fields"]:
                    if field.get("type") == "array":
                        for sub_idx in range(field["count"]):
                            print(f"    {field["name"]}{sub_idx}: typing.Any = {idx}", file=rowdef)
                            idx += 1
                    else:
                        print(f"    {field["name"]}: typing.Any = {idx}", file=rowdef)
                        idx += 1

                print(f"", file=rowdef)

    return 1


if __name__ == "__main__":
    exit(__main__())
