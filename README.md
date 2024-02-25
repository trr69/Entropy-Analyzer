# File Entropy Calculator

This script calculates the entropy of a given file, measuring the degree of randomness or unpredictability in the data. It processes the file in chunks, computes the entropy of each chunk, and displays the progress along with the entropy level. At the end, it provides a classification of the final entropy level as high, moderate, or low.

## Usage

```bash
python entropy_analyzer.py file_path

## Principle of Entropy Calculation

Entropy is a measure of uncertainty or randomness in data. It quantifies the amount of information contained in the data and indicates how unpredictable the data is. The higher the entropy, the more unpredictable or random the data.

### Working Principle

1. **Breaking Data into Symbols:** In the context of file analysis, each byte of data is treated as a symbol.

2. **Counting Symbol Frequencies:** For each symbol (byte), the number of occurrences in the data is counted.

3. **Calculating Probability of Symbol Occurrence:** The probability of each symbol occurring in the data is calculated by dividing its frequency by the total number of symbols.

4. **Computing Entropy:** Using the probabilities of symbol occurrence, the entropy of the data is computed using Shannon's formula:

   ```plaintext
   H = -∑(P(x_i) * log2(P(x_i)))
Where:

- **H** is the entropy in bits,
- **P(x_i)** is the probability of symbol **x_i** occurring,
- **n** is the number of different symbols in the data.
