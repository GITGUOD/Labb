import pandas as pd
import scipy.stats as st

series = pd.read_csv("means-collections-True-Data1.csv", index_col=0).squeeze("columns")
#series = pd.read_csv("means-collections-False-Data1.csv", index_col=0).squeeze("columns")
#series = pd.read_csv("means-mysort-True-Data1.csv", index_col=0).squeeze("columns")
#series = pd.read_csv("means-mysort-False-Data1.csv", index_col=0).squeeze("columns")


mean = series.mean()
sem = st.sem(series)
df = len(series) - 1

ci_low, ci_high = st.t.interval(
    0.95,      # confidence level
    df,        
    loc=mean,  # mean
    scale=sem  # standard error
)

jit = pd.read_csv("means-mysort-True-Data1.csv", index_col=0).squeeze("columns")
nojit = pd.read_csv("means-mysort-False-Data1.csv", index_col=0).squeeze("columns")
#t, p = st.ttest_ind(jit, nojit, equal_var=False)

t, p = st.ttest_ind(jit, nojit) # Vi ska använda detta då de är oberoende mätningar
#t, p = st.stats.ttest_rel(jit, nojit)

print("Mean:", mean)
print("95% CI:", ci_low, ci_high)
print("t-test results:", t, p)
