from data_handler import get_theme

themes = {
    "dark": {
        "bg": "#101010",
        "text": "#f1f1f1",
        "ter": "#555555",
        "selected_bg": "#151515",
        "good": "#00ff00",
        "bad": "#ff0000",
    }
}

theme = themes[get_theme()]
