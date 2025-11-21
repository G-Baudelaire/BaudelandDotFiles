import unittest
import json
from rofi_keybinds import FilterValues


class Tests(unittest.TestCase):
    test_json = json.loads("""
        [
            {
                "locked": false,
                "mouse": false,
                "release": false,
                "repeat": true,
                "non_consuming": false,
                "modmask": 64,
                "submap": "",
                "key": "Return",
                "keycode": 36,
                "catch_all": false,
                "dispatcher": "exec",
                "arg": "kitty",
                "description": "Open terminal"
            },
            {
                "locked": false,
                "mouse": false,
                "release": false,
                "repeat": true,
                "non_consuming": false,
                "modmask": 64,
                "submap": "",
                "key": "Return",
                "keycode": 36,
                "catch_all": false,
                "dispatcher": "exec",
                "arg": "kitty",
                "description": "Open terminal"
            }
        ]
    """)

    def test_get_keybinds_single(self):
        filter_text = FilterValues(self.test_json[0:1])
        keybinds_text = filter_text.get_menu_lines()
        EXPECTED = '<b>SUPER + RETURN</b> <i>Open terminal</i> <span color="cyan">exec kitty</span>'
        self.assertEqual(keybinds_text, EXPECTED)

    def test_get_keybinds_multiple(self):
        filter_text = FilterValues(self.test_json)
        keybinds_text = filter_text.get_menu_lines()
        expected = '<b>SUPER + RETURN</b> <i>Open terminal</i> <span color="cyan">exec kitty</span>\n<b>SUPER + RETURN</b> <i>Open terminal</i> <span color="cyan">exec kitty</span>'
        self.assertEqual(keybinds_text, expected)


#    def test_filter_non_rofi_values(self):
#        filtered_values = FilterValues(self.test_json).filter_values(self.test_json[0])
#        expected_values = JSONDecoder().decode(
#            """{
#            "modmask": 64,
#            "key": "Return",
#            "keycode": 36,
#            "dispatcher": "exec",
#            "arg": "kitty",
#            "description": "Open terminal"
#            }"""
#        )
#
#        self.assertEqual(filtered_values, expected_values)


if __name__ == "__main__":
    unittest.main()
