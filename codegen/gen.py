import os
import sys
import yaml
import typing
from pathlib import Path


class RowWriter:
    field_idx: int = 0

    def __init__(self, file):
        self.file = file

    def write_class_header(self, name):
        print(f"class {name}Row(ExdRow):", file=self.file)

    def write_display_field(self, display_field):
        print(f"    _display_field: str = '{display_field}'", file=self.file)
        print(f"", file=self.file)

    def write_field(self, name):
        print(f"    {name}: typing.Any = {self.field_idx}", file=self.file)
        self.field_idx += 1


def __main__() -> typing.Any:
    schema_dir = Path(__file__).parent / "EXDSchema"
    rowdef_path = (
        Path(__file__).parent.parent
        / "src"
        / "pyxivdata"
        / "resource"
        / "excel"
        / "rowdef.py"
    )
    with open(rowdef_path, "w") as rowdef:
        print("from pyxivdata.resource.excel.reader import ExdRow", file=rowdef)
        print("import typing", file=rowdef)
        print("", file=rowdef)

        for path in schema_dir.glob("*.yml"):
            print(path)
            with open(path, "r") as file:
                writer = RowWriter(rowdef)
                yml = yaml.safe_load(file)

                writer.write_class_header(yml["name"])

                if "displayField" in yml:
                    writer.write_display_field(yml["displayField"])

                for field in yml["fields"]:
                    write_field(field, writer)

                print(f"", file=rowdef)

    return 1


def write_field(field, writer: RowWriter, name_prefix: str = ""):
    field_name = name_prefix + field.get("name", "")

    if len(field_name) == 0:
        print("Empty field name", file=sys.stderr)

    if field.get("type") == "array":
        for sub_idx in range(field["count"]):
            if "fields" in field:
                for sub_field in field["fields"]:
                    write_field(sub_field, writer, name_prefix=f"{field_name}{sub_idx}")
            else:
                writer.write_field(f"{field_name}{sub_idx}")
    else:
        writer.write_field(field_name)


if __name__ == "__main__":
    exit(__main__())
