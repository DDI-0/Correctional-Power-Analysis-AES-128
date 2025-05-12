Project 4: Encryption II: Correlational Power Analysis
Due: Friday 26th April, 2024
Introduction
On the previous assignments, we developed a pseudo-random number generator and used its
output as a stream cipher. We characterized the quality of the random numbers obtained
from the PRNG using the NIST Test Suite. We further included an AES-128 core on the
SoC and used it to decrypt a program in memory and run it.
In this assignment, we will explore a common weakness of hardware implementation of
cryptosystems. With knowledge of how the cryptosystem works, and how it is implemented,
we can analyze power consumption traces of the device in operation to extract secrets.
1 Correlational Power Analysis
Correlational Power Analysis is a type of attack which makes use of variations in power
consumption of digital circuits as they switch. As the number of lines changing during a
particular operation increases, so does the amount of power used by the circuit.
Correlational Power Analysis aims to relate changes in power consumption to guessed
key values. For the implementation of AES-128 being tested, a round is divided into multiple
operations. We attack one round, and attempt to guess the round key by correlating key
guesses to changes in power.
2 Dataset and Program
Unfortunately, we currently lack the facilities to extract power traces ourselves. As such,
we will use the traces as well as the source code from the TeSCASE project at
https://chest.coe.neu.edu/?current page=SOURCE CODE.
Please obtain a copy of the source code and analyze it. To build it you will need CMake.
You do not need to compile this code on your board, in fact, you should build it on your
own machine. If you use Windows, please build it under WSL for ease of use. Even when
running on a CPU, the code does its analysis quickly.
2.1 Dumping Intermediates
We wish to dump intermediates of the analysis the CPA tool is performing. The analysis is
performed by the cpa::cpa() function in src/cpa/cpa.cpp. In particular, we are interested
in the loop which finds the hamming distance set with the highest correlations (line 191 in
1
EECE.4610/7110 Practical Hardware Security
and Cryptography
my copy of the code). Modify this loop to store the highest three sets for every possible
byte, then save this data into a file or files (choose at your own convenience).
Once this data is obtained, use any language of your convenience to generate plots of
the dataset. You should have a total of 16 × 3 = 48 plots, three for every key byte. Record
the Pearson correlation alongside each plot. Include these plots in your report.
3 Deliverables
The following items must be submitted.
• (30pt) A report summarizing your modifications to the code, experimentation, and
discussing results. For graduate students, the report must be at least five (5) pages
long and must contain a high level diagram of the design done in Part 2. Reports must
be typeset as single spaced, single column, on a 12pt serif typeface (e.g. Computer
Modern or Times). Any code in the report must use a monospace typeface.
• (50pt) The dataset obtained by modifying the code.
• (20pt) The program you wrote used to plot the data.
Code used to generate the plots can be written in any language of your choosing.
4 Extra Credit
For twenty (20) extra points, perform correlational power analysis on the full TeSCASE
masked dataset. Include your results in the report.
2
