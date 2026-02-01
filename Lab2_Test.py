from Lab2 import removeNA

import pandas as pd


df = pd.DataFrame({
  "a": [12, pd.NA, 10, pd.NA],
  "b": [11, pd.NA, 15, 20]
})
print(df)

print("Removed NA")
print(removeNA(df))
