import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    path = __file__[:-7]+"\\data\\"

    nve = np.loadtxt(path+"spce_nve.txt",skiprows=1)
    nvt = np.loadtxt(path+"spce_nvt.txt",skiprows=1)
    ave = np.loadtxt(path+"spce_ave.txt",skiprows=1)
    rdf = np.loadtxt(path+"spce_rdf.txt",skiprows=4, max_rows=250)
    rdf = np.loadtxt(path+"saltw_rdf.txt",skiprows=4, max_rows=250)

    nve_tot_eng = nve[:,7]
    nvt_tot_eng = nvt[:,7]
    temp = ave[:,1]
    ave_pres = ave[:,8]
    peak = rdf[25:50,1]
    r_peak = rdf[25:50,1]
    integral = sum(peak*0.048*r_peak**2)
    weights = 0.048*r_peak**2
    weighted_avg = np.sum(peak * weights) / np.sum(weights)

    print(integral)
    print(4 * np.pi * 0.033 * integral)

    print("Weighted average of g(r):", weighted_avg)
    print(4 * np.pi * 0.033 * sum(peak))
    print(sum(ave_pres)/len(ave_pres))

    plt.figure(figsize=(10,5))
    plt.plot(ave_pres)
    plt.title("NVT ave/time simulation temperature")
    plt.grid()
    plt.show()

    plt.plot(rdf[:,1], rdf[:,2])
    plt.title("Salt water RDF for Cl-O")
    plt.grid()
    plt.show()