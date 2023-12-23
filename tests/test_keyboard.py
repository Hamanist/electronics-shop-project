from src.keyboard import Keyboard, MixinLanguage


def test_mixin_language():
    keybord = MixinLanguage()
    assert keybord.get_language() == 'EN'


def test_change_lang():
    keybord_mix = MixinLanguage()
    keybord_mix.get_language()
    keybord = Keyboard('Dark Project KD87A', 9600, 5)
    keybord.change_lang()
    assert keybord.language == 'RU'
    keybord.change_lang()
    assert keybord.language == 'EN'
