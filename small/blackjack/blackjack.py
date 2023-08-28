from mod import Cards, Color, Player

space = " " * 6
enclosure = "=" * 10
section = "-" * 10


def print_section(message="", prefix=section, suffix=section):
    print(f"{prefix} {message} {suffix}")


def print_popup(message="", prefix=">>>", suffix="<<<", color=Color.RESET):
    print(f"{prefix} {color}{message}{Color.RESET} {suffix}")


def print_enclosure():
    print(enclosure)


def press_key_to_next(message="次へ進むには、何かキーを押してください"):
    print_input(message)


def print_error(message, prefix=">"):
    print(f"{Color.RED}{prefix} {message}{Color.RESET}")


def print_input(message, prefix=">>>") -> str:
    return input(f"{Color.YELLOW}{prefix} {message}{Color.RESET}")


def print_action(message, prefix=">>>>>"):
    print(f"{Color.BG_BLUE}{prefix} {message}{Color.RESET}")


class Blackjack:
    def __init__(self) -> None:
        self.initialize()

    def initialize(self, money=0):
        self.cards = Cards()
        self.player = Player("プレイヤー", money)
        self.dealer = Player("ディーラー")

    def player_bed(self) -> None:
        print(f"あなたの所持金: {Color.BG_BLUE}{self.player.money}{Color.RESET}")
        while True:
            s = print_input("お金をかけてください: ")
            try:
                money = int(s)
                if money <= 0:
                    print_error("整数を入力してください")
                    continue
                if self.player.money < money:
                    print_error("所持金以上は掛けられません")
                    continue
                break
            except Exception:
                print_error("数字を入力してください")
        self.player.money -= money
        self.bed = money
        print_action(f"{self.bed} 掛けました")

    def start(self):
        print("=== Game Start ===")
        self.player_bed()
        for human in (self.player, self.dealer):
            for _ in range(2):
                self.draw(human)
        print_section("プレイヤーのターン")
        is_first = True
        while True:
            print_enclosure()
            self.print_dealer()
            self.print_hand()
            print_enclosure()
            if self.total(self.player) >= 21:
                break
            if is_first:
                print("ヒット か スタンド か ダブル を選んでください")
                action = self.choice_input(
                    "h or s or d : ",
                    ["h", "s", "d"],
                )
            else:
                print("ヒット か スタンド を選んでください")
                action = self.choice_input(
                    "h or s : ",
                    ["h", "s"],
                )
            if self.player_action(action):
                break
            is_first = False
        player_total = self.total(self.player)
        print(enclosure * 2)
        print(f"{Color.BG_GREEN}{Color.BLACK} プレイヤーの最終手札{Color.RESET}")
        self.print_hand()
        print(enclosure * 2)
        press_key_to_next()
        if player_total > 21:
            print_popup("バーストしました!", color=Color.RED)
            print_action(f"掛金 {self.bed} は没収です")
            self.rematch()
            return
        print_section("ディラーのターン")
        while True:
            if self.total(self.dealer) >= 17:
                break
            print_enclosure()
            self.print_hand(self.dealer)
            print_enclosure()
            press_key_to_next()
            card = self.draw(self.dealer)
            print_action(f"{card} を引きました")
        print(enclosure * 2)
        print(f"{Color.BG_GREEN}{Color.BLACK} ディーラーの最終手札{Color.RESET}")
        self.print_hand(self.dealer)
        press_key_to_next()
        print(enclosure * 2)
        dealer_total = self.total(self.dealer)
        self.result(player_total, dealer_total)
        self.rematch()

    def result(self, player_total, dealer_total) -> None:
        print_section("勝敗")
        v = 0
        if player_total == 21 and player_total != dealer_total:
            print_popup(f"{Color.BG_RED}BLACKJACK", color=Color.BLACK)
            v = 3
        elif dealer_total > 21:
            print_popup("ディーラーがバーストしました!", color=Color.GREEN)
            v = 2
        elif player_total > dealer_total:
            print_popup("プレイヤーの勝ちです!", color=Color.GREEN)
            v = 2
        elif player_total == dealer_total:
            print_popup("ドローです!", color=Color.BLUE)
            v = 1
        else:
            print_popup("ディーラーの勝ちです!", color=Color.RED)
        back = v * self.bed
        match v:
            case 0:
                message = "は没収です!"
            case 1:
                message = f"は {back} のままです!"
            case 2:
                message = f"は {back} になりました!"
            case 3:
                message = f"は BLACKJACK で {back} になりました!"
        print_action(f"掛金 {self.bed} {message}")
        self.player.money += back

    def player_action(self, action: str) -> bool:
        """player's action

        Args:
            action: h or s or d

        Returns:
            Break if return true
        """
        match action:
            case "h":
                card = self.draw(self.player)
                print_action(f"{card} を引きました")
            case "s":
                print_action("スタンドしました")
                return True
            case "d":
                if self.bed > self.player.money:
                    print(">> 所持金が足りませんのでダブルをできませんでした")
                    return False
                self.player.money -= self.bed
                self.bed *= 2
                card = self.draw(self.player)
                print_action(f"掛金を {self.bed} にしました")
                print_action(f"ダブルで {card} を引きました")
                return True
        return False

    def rematch(self) -> None:
        print_section("Rematch")
        money = self.player.money
        print(f"あなたの所持金: {money}")
        if money == 0:
            print(f"{Color.MAGENTA} あなたは金なしです! {Color.RESET}")
            exit()
        print("もう一回しますか？")
        one_more = print_input("y or n : ")
        if one_more != "n":
            self.initialize(money)
            self.start()

    def choice_input(self, message, choice: list):
        while True:
            select = print_input(message)
            if select in choice:
                return select

    def print_hand(self, human=None):
        if human is None:
            human = self.player
        total = self.total(human)
        print(f"{Color.UNDERLINE}{human.name}:{Color.RESET}")
        print(space + f"得点: {Color.BG_RED}{total}{Color.RESET}")
        print(space + f"手札: {human.cards}")

    def print_dealer(self):
        cards = self.dealer.cards.copy()
        cards[0] = "#"
        print(f"{Color.UNDERLINE}{self.dealer.name}:{Color.RESET}")
        print(space + f"手札: {cards}")

    def draw(self, human: Player) -> str:
        card = self.cards.draw()
        human.draw(card)
        return card

    def total(self, human: Player) -> int:
        total = 0
        cards = list(map(lambda x: x[1:], human.cards))
        ace_num = len(list(filter(lambda x: x == "A", cards)))
        for card in cards:
            match card:
                case "J" | "Q" | "K":
                    total += 10
                case "A":
                    pass
                case _:
                    total += int(card)
        for i in reversed(range(ace_num)):
            total += 11 if (11 - i) > total else 1
        return total


Blackjack().start()
