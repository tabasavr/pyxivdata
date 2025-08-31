from pyxivdata.common import GameLanguage
from pyxivdata.installation.resource_reader import GameResourceReader
from pyxivdata.resource.excel.rowdef import GatheringItemRow, ItemRow

def __main__():
    with GameResourceReader(default_language=[GameLanguage.English]) as game:
        ore: GatheringItemRow = game.excels["GatheringItem"][42]
        print(ore)
        print([(column, ore[i]) for i, column in enumerate(ore._mapping.keys())])
        print(ore.Item)

        item: ItemRow = game.excels["Item"][ore.Item]
        print(item)
        print([(column, item[i]) for i, column in enumerate(item._mapping.keys())])


if __name__ == "__main__":
    exit(__main__())
