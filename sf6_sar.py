from rdkit import Chem

if __name__ == "__main__":
    # SAR parameter: log10(k_OH) for SF6 (cm³ molecule⁻¹ s⁻¹ at 298 K)
    # Based on literature lifetime ~3200 years at [OH]≈1e6 molecule/cm³ ⇒
    # k ≈ 1/(τ·[OH]) ≈ 1e-17 ⇒ log10(k) ≈ -17
    SAR_PARAMS = {
        'SF6': -17.0,
    }

    # SMARTS pattern to recognize the SF6 fragment
    SAR_SMARTS = {
        'SF6': '[S]([F])([F])([F])([F])([F])[F]',
    }

    # compile the SMARTS
    patterns = {
        name: Chem.MolFromSmarts(smarts)
        for name, smarts in SAR_SMARTS.items()
    }

    # sanity check
    for name, patt in patterns.items():
        if patt is None:
            raise ValueError(f"Invalid SMARTS for {name}")

    # load SF6
    smiles = 'S(F)(F)(F)(F)(F)F'
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        raise ValueError(f"Invalid SMILES: {smiles}")

    # count groups and sum log10(k)
    log10_k_total = 0.0
    for name, patt in patterns.items():
        count = len(mol.GetSubstructMatches(patt))
        log10_k_total += SAR_PARAMS[name] * count

    k_OH = 10**log10_k_total  

    # compute lifetime τ = 1 / (k_OH × [OH])
    OH_conc = 1e6  # typical tropospheric [OH] in molecule/cm³
    tau_s = 1.0 / (k_OH * OH_conc)
    tau_years = tau_s / (3600 * 24 * 365.25)

    print(f"Estimated k(OH + SF6) = {k_OH:.2e} cm³·molecule⁻¹·s⁻¹")
    print(f"Estimated atmospheric lifetime = {tau_years:.1f} years")
