# Parsing

data  ← •file.Lines "../Advent-of-Code-2023/data/test.txt"
Parse ← str.ToArray ¨ '|' str.SplitAt 1⊏ ':' str.SplitAt 𝕩 # these functions don't exist
cards ← Parse ¨ data

# Part A

Points      ← ⌊2⋆¯1+⊢
TotalPoints ← { +´ Points +´⊒∾ ¨ 𝕩 }

# Print Results

TotalPoints cards
