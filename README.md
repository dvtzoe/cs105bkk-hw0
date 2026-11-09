# HW0: pipeline check

**Ungraded.** HW0 checks that your whole setup works before the first graded homework: GitHub, your laptop, the tests, and GitHub Actions. The code part is small and practises Session 1: names and objects, default arguments, `*args`, and comprehensions.

**Due:** the start of Session 2, Tue 10 Nov (D17).

## 1. Get your own copy

1. On this repository's GitHub page, click **Use this template** → **Create a new repository**.
2. Owner: your own account. Name: `cs105bkk-hw0`. Click **Create repository**.
3. Clone **your** new repository and open the folder in VS Code:

   ```
   git clone https://github.com/<your-username>/cs105bkk-hw0.git
   ```

## 2. Set up and see red

From the repository folder:

```
python -m venv .venv
```

Activate it. On macOS: `source .venv/bin/activate`. On Windows: `.venv\Scripts\activate`.

```
python -m pip install pytest
python -m pytest
```

Every test fails with `NotImplementedError`. That is the starting point.

## 3. Write the code

Open `inventory.py`. An inventory is a dict that maps an item name to how many you have, for example `{"potion": 3, "arrow": 12}`. Write the three functions:

1. `add_item(inventory, item, count=1)` returns a **new** inventory with `count` more of `item`. If the item is new, it starts at `count`. The inventory you were given must not change.
2. `total_items(*inventories)` returns how many items there are in all the inventories given together. With no inventories, the total is `0`.
3. `running_low(inventory, limit=2)` returns the names of the items with **fewer than** `limit` left, sorted A to Z.

Run `python -m pytest` until every test passes.

## 4. Fill in NOTES.md

Answer the three questions in `NOTES.md`. A few honest sentences each are enough.

## 5. Commit, push, and check Actions

```
git add inventory.py NOTES.md
git commit -m "Finish HW0"
git push
```

On your repository's GitHub page, open the **Actions** tab. GitHub runs the tests on every push. A green tick means they passed there too. That result is feedback for you, not a grade.

## 6. Upload to Google Classroom

Upload a `.zip` of your repository and paste its link in the HW0 assignment on Google Classroom. *(Proposal O13)*
