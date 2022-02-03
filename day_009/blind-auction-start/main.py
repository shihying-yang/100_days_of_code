# from replit import clear
# #HINT: You can call clear() to clear the output in the console.

from os import system

from art import logo


def add_more_bidders(all_bidders):
    """add more bidders to the auction"""
    name = input("What is your name?: ")
    bid = float(input("What is your bid?: $"))
    all_bidders[name] = bid
    return all_bidders


def find_winner(all_bidders):
    """find the winner from all the bidders"""
    for k, v in all_bidders.items():
        if v == max(all_bidders.values()):
            print(f"The winner is {k} with a bid of ${v}")
            break


if __name__ == "__main__":
    # print the logo
    print(logo)

    bidders = {}
    to_add_more = True
    while to_add_more:
        # add bidders
        bidders = add_more_bidders(bidders)
        more_bidder = input("Are there any other bidders? Type 'yes' or 'no'. ")
        to_add_more = more_bidder.lower().startswith("y")
        if to_add_more:
            system("clear")
    # print(bidders)
    find_winner(bidders)
