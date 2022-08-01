def print_menu(enum):
    for val in enum:
        print(str.title(f"{val.value}. {val.name}").replace("_", " "))


def divider(length):
    print("-" * length)


def div():
    divider(30)


def subdiv():
    divider(19)


def title(atitle: str, length: int = 30):
    divider(length)
    print(atitle)
    divider(length)
