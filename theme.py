from data_handler import get_theme

themes = {
    "dark": {
        "bg": "#101010",
        "text": "#f1f1f1",
        "sec": "#717171",
        "ter": "#555555",
        "selected_bg": "#151515",
        "good": "#3B7735",
        "bad": "#773C35",
    }
}

theme = themes[get_theme()]
