

class Player:
    def __init__(self, name, profession) -> None:
        self.name = name
        self.profession = profession
        self.financial_statement = FinancialStatement()
        self.small_deal = []
        self.big_deal = []
        self.market = []
        self.doodads = []

    def take_turn(self):
        pass

class FinancialStatement:
    def __init__(self, profession) -> None:
        self.profession = profession.profession_name
        self.salary = profession.salary
        self.expenses = profession.expenses
        self.assets = profession.assets
        self.liabilities = profession.liabilities

class Profession:
    def __init__(self, profession_name, salary, expenses, assets, liabilities) -> None:
        self.profession_name = profession_name
        self.salary = salary
        self.expenses = expenses
        self.assets = assets
        self.liabilities = liabilities


class DealCard:
    def __init__(self) -> None:
        pass
class MarketCard:
    def __init__(self) -> None:
        pass

class DoodadCard:
    def __init__(self) -> None:
        pass



teacher = Profession(
    "teacher",
    4000,
    {"taxes": 1000, "Home Mortgage": 1000, "School Loan": 100},
    {"Real Estate": 0},
    {"Home Mortgage": 500000}
)