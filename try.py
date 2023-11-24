import pandas as pd
import numpy as np

if __name__ == "__main__":
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    print(s[0])
    