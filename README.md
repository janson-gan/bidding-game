# 🏷️ Secret Bidding Game

I'm currently exploring Python fundamentals through mini projects, and this is a simple \*\*Secret Bidding Game\*\*. The idea is: the first bidder enter the name and bid amount, then the program ask if there's another bidder. If yes, the screen clear and prompt for the next bidder name and bid. This way, nobody can see the previous bids. When there's no more bidders, the program will display the highest bidder's name and bid.

---

## 🎯 What this project does

* Prompts each bidder to enter their name and bid amount.
* Stores all bids in a dictionary.
* Compares bids to find the highest bidder.
* Announces the winner with their bid.

---

## 🛠️ How it works

1. Run the script in your terminal:
```bash
python bidding_game.py
```
2. Enter your name and bid when prompted.
3. Indicate if there are more bidders (y for yes, n for no).
4. Once bidding ends, the program prints the winner.



📚 What I learned

- How to use dictionaries to store key-value pairs.
- Writing functions to keep logic organized.
- Using loops and conditionals to control program flow.
- Practicing clean input/output handling in Python.



🚀 Next steps

I plan to extend this project by:

- Adding input validation (e.g., preventing negative bids).
- Saving results to a file for record keeping



## Example Output
<p align="left">
  <img width="400" height="334" alt="image" src="https://github.com/user-attachments/assets/ea58bc09-7c81-4e72-b2ed-943030056824" /><br>
  <img width="400" height="97" alt="image" src="https://github.com/user-attachments/assets/bf8defa7-7d7a-4708-8f5a-50866c380118" /><br>
  <img width="400" height="44" alt="image" src="https://github.com/user-attachments/assets/2b7f2ca6-e893-494e-a145-e3aff6fa6d35" />
</p>

---

## ⚡ Challenges
- Figuring out how to store multiple bids and link them to each bidder’s name.
- Making sure the program correctly identifies the highest bid.
- Clearing the screen so that each new bidder cannot see the previous bids.

---
Made with ❤️ using Python
