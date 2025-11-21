import sys
import json
from typing import List, Dict


class FilterValues:
    _MODKEY_MAPPINGS = {
        0: "",
        1: "SHIFT",
        4: "CTRL",
        5: "SHIFT + CTRL",
        8: "ALT",
        9: "SHIFT + ALT",
        12: "CTRL + ALT",
        64: "SUPER",
        65: "SUPER + SHIFT",
        68: "SUPER + CTRL",
        72: "SUPER + ALT",
        76: "SUPER + CTRL + ALT",
    }

    def __init__(self, keybinds: List[Dict]) -> None:
        self._keybinds = keybinds

    def get_menu_lines(self):
        menu_lines = (self._get_menu_line(keybind) for keybind in self._keybinds)
        return "\n".join(menu_lines)

    def _get_menu_line(self, keybind: Dict):
        keys = self._get_keys(keybind)
        description = keybind["description"]
        command = self._get_command(keybind)
        return f'<b>{keys}</b> <i>{description}</i> <span color="cyan">{command}</span>'

    def _get_keys(self, keybind: Dict):
        modmask = keybind["modmask"]
        modmask_text = self._MODKEY_MAPPINGS.get(modmask, str(modmask))
        keybind_text = str.upper(keybind["key"])
        plus_symbol = " + " if modmask_text and keybind_text else ""
        return f"{modmask_text}{plus_symbol}{keybind_text}"

    def _get_command(self, keybind: Dict):
        return f"{keybind['dispatcher']} {keybind['arg']}"


if __name__ == "__main__":
    data = json.loads("".join(sys.stdin))
    print(FilterValues(data).get_menu_lines())
