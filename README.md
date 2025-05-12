# Correlational Power Analysis for AES-128

This repository contains the implementation of Correlational Power Analysis (CPA) on AES-128 encryption, using power trace data from the TeSCASE project.

## Overview

Correlational Power Analysis is a side-channel attack technique that exploits the relationship between power consumption and operations in cryptographic implementations. By analyzing power consumption patterns during encryption operations, we can potentially extract secret keys.

This project:
1. Modifies the TeSCASE CPA tool to extract intermediate data during analysis
2. Generates visualization plots of correlation data for each key byte
3. Analyzes the results to demonstrate how power analysis can compromise cryptographic implementations

