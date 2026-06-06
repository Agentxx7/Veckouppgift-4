from uppgifter import (
    uppgift1,
    eko,
    loopa_fem_varv,
    last,
    cut_edges,
    increase,
    average,
    pretty_print
)

from twentyone import start_twentyone
from poker import run_poker_demo
from turtle_uppgifter import run_turtle_demo


def run_uppgifter():
    uppgift1("David")

    eko("hej")
    eko("hej", 3)

    loopa_fem_varv()

    print(last([1, 2, 3]))

    print(cut_edges([1, 2, 3, 4]))

    print(increase(1))

    print(average(4, 8))

    pretty_print(["a", "b", 3.14])


def main():
    # Välj vad du vill köra genom att kommentera in/ut.

    # run_uppgifter()
    # start_twentyone()
    # run_poker_demo()
    run_turtle_demo()


if __name__ == "__main__":
    main()