import random


class Cards:
    extensions = ["♥", "♣", "♦", "♠"]
    numbers = ["A"] + [str(i) for i in range(2, 11)] + ["J", "Q", "K"]

    def __init__(self) -> None:
        self.cards: list[str] = [
            f"{e}{n}" for n in Cards.numbers for e in Cards.extensions
        ]
        self.shuffle()

    def draw(self) -> str:
        return self.cards.pop(0)

    def shuffle(self):
        random.shuffle(self.cards)


class Player:
    def __init__(self, name, money=0) -> None:
        self.cards: list[str] = []
        self.name: str = name
        self.money: int = 1000 if money == 0 else money

    def draw(self, card: str) -> str:
        self.cards.append(card)


class Color:
    BLACK = "\033[30m"  # (文字)黒
    RED = "\033[31m"  # (文字)赤
    GREEN = "\033[32m"  # (文字)緑
    YELLOW = "\033[33m"  # (文字)黄
    BLUE = "\033[34m"  # (文字)青
    MAGENTA = "\033[35m"  # (文字)マゼンタ
    CYAN = "\033[36m"  # (文字)シアン
    WHITE = "\033[37m"  # (文字)白
    COLOR_DEFAULT = "\033[39m"  # 文字色をデフォルトに戻す
    BOLD = "\033[1m"  # 太字
    UNDERLINE = "\033[4m"  # 下線
    INVISIBLE = "\033[08m"  # 不可視
    REVERCE = "\033[07m"  # 文字色と背景色を反転
    BG_BLACK = "\033[40m"  # (背景)黒
    BG_RED = "\033[41m"  # (背景)赤
    BG_GREEN = "\033[42m"  # (背景)緑
    BG_YELLOW = "\033[43m"  # (背景)黄
    BG_BLUE = "\033[44m"  # (背景)青
    BG_MAGENTA = "\033[45m"  # (背景)マゼンタ
    BG_CYAN = "\033[46m"  # (背景)シアン
    BG_WHITE = "\033[47m"  # (背景)白
    BG_DEFAULT = "\033[49m"  # 背景色をデフォルトに戻す
    RESET = "\033[0m"  # 全てリセット
