import json
import copy

with open('data.json', 'r') as file:
    data = json.load(file)

def get_portfolio() -> list[str]:
    return data["portfolio"]

def save_portfolio(tickers: list[str]) -> None:
    new_data = copy.deepcopy(data)
    new_data["portfolio"] = tickers
    with open("data.json", "w") as outfile:
        json.dump(new_data, outfile, indent=4)

def get_lists() -> dict[str, list[str]]:
    return data["lists"]

def get_list(name: str) -> list[str]:
    return get_lists().get(name, [])

def set_list(name: str, tickers: list[str]) -> None:
    new_data = copy.deepcopy(data)
    new_data["lists"][name] = tickers
    with open("data.json", "w") as outfile:
        json.dump(new_data, outfile, indent=4)

def add_list(name: str) -> None:
    set_list(name, [])

def get_theme() -> str:
    return data["theme"]
