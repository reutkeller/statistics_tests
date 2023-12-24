# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/statistics_tests/significant_test.ipynb.

# %% auto 0
__all__ = ['data', 'df']

# %% ../nbs/statistics_tests/significant_test.ipynb 3
import pandas as pd
import numpy as np
# import statsmodels.api as sm
# import scipy.stats as stats
# from statsmodels.formula.api import ols

import matplotlib.pyplot as plt
# import scipy.stats as stats

# import seaborn as sns


# import scikit_posthocs as sp
# import pandas as pd
# import numpy as np
# from io import StringIO

# %% ../nbs/statistics_tests/significant_test.ipynb 5
data = {
    'id': ['A' + str(i) for i in range(1, user_defined_number + 1)],
    'value': np.random.rand(30).tolist(),
    'group': np.random.permutation(np.tile(np.arange(1, 7), 5))
}

df=pd.DataFrame(data)
df
