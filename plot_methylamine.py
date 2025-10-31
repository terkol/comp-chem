import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    run = np.loadtxt(__file__[:-19]+"\\data\\log.txt")
    temps = run[:,1]
    engs = run[:,8]
    avg_pot_eng = sum(engs)/len(engs)
    print(avg_pot_eng)

    thou2 = list(range(2002))
    plt.plot(thou2, temps)
    plt.title("Temperature")
    plt.grid()
    plt.legend()
    plt.show()
    plt.plot(thou2, engs)
    plt.title("Potential Energy")
    plt.grid()
    plt.legend()
    plt.show()