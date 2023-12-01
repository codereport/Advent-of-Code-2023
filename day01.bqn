
# Part A
data ← •file.Lines "../Advent-of-Code-2023/data/01.txt"

Nums ← +´(•BQN ⊑∾(⊑⌽))¨∊⟜"0123456789"⊸/ 
Nums ¨ data

# Part B

Translate ← # this is non-trivial maybe do later
Nums ∘ Translate ¨ data
