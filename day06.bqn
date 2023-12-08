str ← •Import "util/strings.bqn"

# Parsing
times‿dist ← str.ToNats ¨ 9⊸↓ ¨ •file.Lines "data/06.txt"

# Part A
CanWin    ← +´⊣<(-⟜↕×↕)∘⊢
WaysToWin ← ×´CanWin¨

# Part B
FlattenInts ← str.ToNats · ∾ •Fmt ¨

# Print Results
•Show dist WaysToWin times
•Show dist WaysToWin ○ FlattenInts times
