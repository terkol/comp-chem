import numpy as np
import matplotlib.pyplot as plt

def build_spectrum(freqs, ints):
    S = ints * conv
    spec = np.zeros_like(nu)
    for f, Si in zip(freqs, S):
        spec += (Si / (sigma * np.sqrt(2*np.pi))) * np.exp(-0.5*((nu-f)/sigma)**2)
    return spec

if __name__ == "__main__":
    h = 6.62607015e-34; c = 2.99792458e8; k = 1.380649e-23; T = 288.0; NA = 6.02214076e23
    nu = np.linspace(300, 1100, 4000); nu_m = nu * 100

    # Earth blackbody (normalized)
    B = (2 * h * c**2 * nu_m**3) / (np.exp(h*c*nu_m/(k*T)) - 1)
    B_norm = (B / B.max())/(10**(15))

    # Experimental
    exp_freqs = np.array([610, 930])
    exp_ints = np.array([150.0, 550.0])

    # PM6 (high and low T1u)
    pm6_freqs = np.array([246.7826, 447.5975, 784.0157])
    pm6_ints = np.array([0.0018+0.0245+0.0016, 148.7534+144.9454+156.1385, 638.5079+565.6045+539.9526])  # average of triplet intensities

    # DFT full 15 modes
    dft_freqs = np.array([312.6252, 470.6098, 555.7781, 611.5526, 708.7802, 912.3799])
    dft_ints = np.array([0, 0, 3*25.8842, 0, 0, 3*434.1006]) 

    # Conversion
    conv = 1e7 / NA; sigma = 5.0

    xsec_exp = build_spectrum(exp_freqs, exp_ints)
    xsec_pm6 = build_spectrum(pm6_freqs, pm6_ints)
    xsec_dft = build_spectrum(dft_freqs, dft_ints)

    # Plot
    plt.figure(figsize=(10,4))
    plt.plot(nu, B_norm,   '-.', label='Earth Blackbody (288K)')
    plt.plot(nu, xsec_exp, ':', label='Literature (NIST)')
    plt.plot(nu, xsec_pm6, label='PM6')
    plt.plot(nu, xsec_dft, label='DFT (B3LYP/6-31+G(d,p))')

    plt.xlim(300, 1100)
    plt.xlabel('Wavenumber (cm$^{-1}$)')
    plt.ylabel('Intensity (arbitrary units)')
    plt.title('Experimental, PM6, and DFT peaks for SF$_{6}$ IR absorption')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()
