import numpy as np
import matplotlib.pyplot as plt
import re

if __name__ == "__main__":
    path = __file__[:-5]+"\\data\\"

    rhf = np.loadtxt(path+"h2_rhf.txt")[:,2]
    rhfd = np.loadtxt(path+"h2_rhf_vdz.txt")[:,2]
    rhft = np.loadtxt(path+"h2_rhf_vtz.txt")[:,2]
    rhfq = np.loadtxt(path+"h2_rhf_vqz.txt")[:,2]
    rhf5 = np.loadtxt(path+"h2_rhf_v5z.txt")[:,2]
    uhf = np.loadtxt(path+"h2_uhf.txt")[:,2]

    energies = []
    pattern = re.compile(r'CCSD\(T\)=\s*([+\-]?\d+\.\d+)D([+\-]\d+)')
    with open(path+'h2_ccsd.txt') as f:
        for line in f:
            m = pattern.search(line)
            if m:
                mantissa, exponent = m.groups()
                value = float(mantissa + 'E' + exponent)
                energies.append(value)
    ccsd = np.array(energies)
    energies = []
    pattern = re.compile(r'CCSD\(T\)=\s*([+\-]?\d+\.\d+)D([+\-]\d+)')
    with open(path+'h2_uccsd.txt') as f:
        for line in f:
            m = pattern.search(line)
            if m:
                mantissa, exponent = m.groups()
                value = float(mantissa + 'E' + exponent)
                energies.append(value)
    uccsd = np.array(energies)

    def prep(a):
        return (a-a[0])*2625.49646436

    rhf = prep(rhf)
    rhfd = prep(rhfd)
    rhft = prep(rhft)
    rhfq = prep(rhfq)
    rhf5 = prep(rhf5)
    uhf = prep(uhf)
    ccsd = prep(ccsd)
    uccsd = prep(uccsd)

    x = np.linspace(0.74,3.74,31)

    plt.plot(x[-5:],rhfd[-5:],label="RHF/cc-pVDZ")
    plt.plot(x[-5:],rhft[-5:],label="RHF/cc-pVTZ")
    plt.plot(x[-5:],rhfq[-5:],label="RHF/cc-pVQZ")
    plt.plot(x[-5:],rhf5[-5:],label="RHF/cc-pV5Z")

    plt.plot(x,rhf,label="RHF")
    plt.plot(x,uhf,'--',label="UHF")
    plt.plot(x,ccsd,label="CCSD(T)",)
    plt.plot(x,uccsd,'--',label="UCCSD(T)")
    plt.xlabel("Bond length (Å)")
    plt.ylabel("ΔE (kJ/mol)")
    plt.grid()
    plt.legend()
    plt.show()
