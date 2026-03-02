import pandas as pd
import scipy.stats as st

jit = pd.read_csv("means-collections-True-Data2.csv",index_col=0).squeeze("columns")

nojit = pd.read_csv("means-collections-False-Data2.csv", index_col=0).squeeze("columns")

# Räkna ut medelvärde för både
mean_jit = jit.mean()
mean_nojit = nojit.mean()

# konfidensintervallet 95%
def ci95(series):
    mean = series.mean()
    sem = st.sem(series)
    df = len(series) - 1
    return st.t.interval(0.95, df, loc=mean, scale=sem)

ci_jit = ci95(jit)
ci_nojit = ci95(nojit)

# t-test
t, p = st.ttest_ind(jit, nojit, equal_var=False)

# speedup
speedup = mean_nojit / mean_jit

print("JIT medelvärde:", mean_jit, "CI:", ci_jit)
print("NO JIT medelvärde:", mean_nojit, "CI:", ci_nojit)
print("Hur många gånger snabbare var JIT körningen jämfört med utan JIT :", speedup)
print("Hur långt ifrån varandra medelvärdena är, alltså den relativa variationen", "t =", abs(t))
print("Sannolikheten att skillnaden är baserad på slump","p =", p)