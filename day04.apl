⍝ Reading / Parsing
data ← ⊃⎕NGET 'C:/test.txt' 1
Parse ← {⍎¨'|'(≠⊆⊢)⊃1↓':'(≠⊆⊢)⍵}

⍝ Part A
Points      ← ⌊2*¯1+⊢
TotalPoints ← +/{Points≢⊃∩/⍵}¨

⍝ Print Results
TotalPoints Parse ¨ data
