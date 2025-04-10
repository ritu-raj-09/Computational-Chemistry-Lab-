# Computational-Chemistry-Lab-
# TST Rate Constant Calculator from Gaussian Log Files

This is a Python script that calculates the **rate constant** using **Transition State Theory (TST)** by extracting **vibrational frequencies** from Gaussian frequency job output files (`.log`). It requires Gaussian outputs for both the **reactant** and the **transition state (TS)**.

---

##  Features

- Parses vibrational frequencies directly from Gaussian log files.
- Calculates TST rate constant at a given temperature.
- Only asks for:
  - Temperature (in Kelvin)
  - Activation energy (in kJ/mol)
  - File paths for reactant and TS log files

---

##  How to Use

1. Make sure you have Gaussian frequency calculations completed for:
   - Your **reactant**
   - Your **transition state**

2. Save the output files (.log).

3. Run the script
