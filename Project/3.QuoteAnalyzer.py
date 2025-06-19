import pandas as pd

with open ("3.txt", "r") as f:
    data = f.read()
    words = [word.strip().lower() for word in data.split()]
    words_series = pd.Series(words)
    
print(words_series.value_counts().head(5))

    