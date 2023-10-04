from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Label, Footer


class TheScreen(Screen):
    CSS_PATH = "screen.tcss"
    BINDINGS = [("f", "pop_screen", "Pop Screen")]

    def compose(self) -> ComposeResult:
        yield Label("The Screen")
        yield Footer()


class TheApp(App):
    CSS_PATH = "app.tcss"
    SCREENS = {"screen": TheScreen}
    BINDINGS = [("f", "push_screen('screen')", "Push Screen")]

    def compose(self) -> ComposeResult:
        yield Label("The App")
        yield Footer()
