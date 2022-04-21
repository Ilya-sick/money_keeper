#money_keeper

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class Money_keeper(MDApp):
    def build(self):
        return MDLabel(text="Hello, Money Keeper!", halign="center")


Money_keeper().run()