import numpy as np
import matplotlib.pyplot as plt

def combine_files():
    ohh = np.genfromtxt(path+"ohh_data.txt")
    x = ohh[:,1]
    y = ohh[:,2]
    z = ohh[:,3]

    mol = np.genfromtxt(path+"data_mol.txt")
    i = mol[:,0]
    m = mol[:,1]
    a = mol[:,2]
    c = mol[:,3]

    with open(path+"gen.txt", "w") as f:
        for l in range(len(x)):
            f.write(f"\t{int(i[l])}\t {int(m[l])}\t {int(a[l])}\t {c[l]}\t {x[l]}\t {y[l]}\t {z[l]}\n")

def saltwater():
    saltw = np.genfromtxt(path+"saltwater.txt")
    pres = saltw[:,-2]
    print(sum(pres)/len(pres))

    plt.figure(figsize=(10,5))
    plt.plot(pres)
    plt.title("Saltwater Simulation Pressure")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    path = __file__[:-12]+"\\data\\"
    combine_files()