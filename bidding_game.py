from art import logo

def check_highest_bid(bidding):
    highest_bid = 0
    highest_bidder = ""
    for key in bidding:
        if bidding[key] > highest_bid:
            highest_bid = bidding[key]
            highest_bidder = key
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")

def bidding_game():
    print(logo)
    bidding_info = {}
    check_bidder = "y"
    while check_bidder == "y":
        bidder = input("Enter your name to start bidding: ")
        bid_price = int(input("Enter your bid: "))
        bidding_info[bidder] = bid_price
        check_bidder = input("Are there any other bidders? Type 'y' for yes or 'n' for no: ")
        print("\n" * 100)

    if check_bidder == "n":
        check_highest_bid(bidding_info)

bidding_game()

