import pandas as pd
import matplotlib.pyplot as plt
import glob

def load_mean(algorithm, jit, dataType):
    '''
    medelvärde per iteration över alla runs
    '''
    files = glob.glob(f"run-{algorithm}-{jit}-*-{dataType}.csv")

    runs = []
    for file in files:
        df = pd.read_csv(file, index_col=0)
        runs.append(df.iloc[:, 0])

    combined = pd.concat(runs, axis=1)
    return combined.mean(axis=1)


algorithm = "mysort"
dataType = "data1"
# dataType = "data2"


# algorithm = "collections"
# dataType = "data1"
# dataType = "data2"

mean_false = load_mean(algorithm, False, dataType)
mean_true  = load_mean(algorithm, True, dataType)

plt.figure()

plt.plot(mean_false, label="JIT OFF (-Xint)")
plt.plot(mean_true, label="JIT ON")

plt.title(f"{algorithm} comparison | {dataType}")
plt.xlabel("Iteration")
plt.ylabel("Time")
plt.legend()

plt.show()