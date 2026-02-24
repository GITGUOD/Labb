import subprocess
import pandas as pd
import numpy as np

java = r"C:\Users\tonny\AppData\Local\Programs\Eclipse Adoptium\jdk-17.0.8.101-hotspot\bin\java.exe"
classpath = r"C:\Users\tonny\AppData\Roaming\Code\User\workspaceStorage\95abed6f19a055b53b6ee5c56cea94a4\redhat.java\jdt_ws\EDAA35-Labb_c5548da5\bin"

inFile = r"C:\Users\tonny\OneDrive\Documents\EDAA35\EDAA35-Labb\Labb_5\data2.txt"
#algorithm = "collections"   # eller "mysort"
algorithm = "mysort"   # eller "collections"

jit = True                  # False = -Xint
#dataType = "data1"
dataType = "data2"
n = 600
runs = 10                   # eller 100

means = []

for i in range(runs):
    resultFile = f"run-{algorithm}-{jit}-{i}-{dataType}.csv"

    cmd = [
        java,
        "-cp", classpath,
        "Labb_5.Measure",
        inFile,
        resultFile,
        str(n),
        algorithm,
    ]

    if not jit:
        cmd.insert(1, "-Xint")

    print("Running:", cmd)
    subprocess.run(cmd)

    df = pd.read_csv(resultFile, index_col=0)
    steady = df[100:]   # eller df[450:] beroende på grafen
    means.append(steady.mean()[0])

pd.Series(means).to_csv(f"means-{algorithm}-{jit}-{dataType}.csv")
print("Saved:", f"means-{algorithm}-{jit}-{dataType}.csv")
