# Burrows-Wheeler DNA Sequence Alignment

This repository contains a Python implementation of the **Burrows-Wheeler Alignment (BWA)** algorithm, tailored for DNA sequence matching. This implementation focuses on providing a clear and educational perspective of the algorithm, making it easier to understand and explore the core concepts behind BWA.

---

## 🔬 **Project Overview**

The Burrows-Wheeler Transform (BWT) is a key component in several DNA sequence alignment algorithms, notably the **BWA algorithm** used in bioinformatics. This project demonstrates how the BWT, Suffix Arrays (SA), and other auxiliary data structures (C, Occ) can be applied to perform **efficient and accurate string matching** for DNA sequences.

### **Key Features:**
- **Case-Insensitive Search**: The search function is robust to case, making it flexible for varying input formats.
- **100% Accurate Results**: Unlike heuristic-driven implementations of BWA, this code guarantees accuracy at the cost of speed.
- **Detailed Use of Data Structures**: Utilizes Burrows-Wheeler Transform, Suffix Array, and auxiliary structures (C, Occ) for precise substring matching.
- **Pruning Inexact Matches**: Employs a D array to prune the search tree, optimizing inexact string matches.
- **Ease of Understanding**: Focuses on clarity and readability, avoiding complex optimizations to help users learn the core concepts.

---

## 📂 **Code Structure**

The core of this implementation revolves around the following components:
1. **Burrows-Wheeler Transform (BWT)**: Transforms the input DNA sequence to allow for efficient matching.
2. **Suffix Array (SA)**: Stores the sorted suffixes of the transformed sequence for fast lookup.
3. **C Array**: Keeps track of the starting positions of characters in the BWT-transformed string.
4. **Occ Array**: Efficiently counts occurrences of each character up to a given position in the string.
5. **D Array**: Prunes the search tree to speed up the inexact match search.

---

## 🚀 **How to Use**

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/bwa-dna-sequence-alignment.git
   cd bwa-dna-sequence-alignment
   ```

2. Install any dependencies (if applicable).

3. Run the script by passing a reference sequence:
   ```python
   from BWA import BWA

   reference_sequence = "ACGTACGTGACG"
   bwa = BWA(reference_sequence)
   
   # To search for a substring in the sequence:
   result = bwa.search("ACGT")
   print(result)
   ```

---

## 🧠 **Understanding the BWA Algorithm**

This implementation differs from the actual BWA algorithm in several ways, focusing on clarity over optimization:

- **Recursive Depth-First Search**: This code uses DFS to traverse the suffix tree, while the real BWA uses Breadth-First Search with a heap for partial alignment prioritization.
- **No Heuristics**: This code guarantees 100% accurate results without employing any heuristic methods like limiting search depth or pruning based on early seed matches.
- **Unoptimized Memory Use**: The real BWA reduces memory usage by calculating parts of the suffix array and occurrence array on the fly; this implementation does not.
- **Simplified Structure**: It does not leverage the optimization strategies found in BWA, such as limiting the maximum allowed difference in the first few bases (seeding).

---

## 🎯 **Planned Enhancements**
- **Incorporate Heuristics**: Future versions may include heuristic optimizations to trade off some accuracy for performance.
- **Memory Optimization**: Store fractions of the `Occ` and `SA` arrays to mimic the memory efficiency of the real BWA.
- **Support for Shorter Reads**: Add functionality to handle shorter DNA sequences more effectively.

---

This repository is an educational resource aimed at helping students and professionals alike understand the Burrows-Wheeler Transform and its application in DNA sequence alignment. While it does not match the speed or efficiency of production-ready tools like the official BWA, it is a stepping stone towards mastering this essential algorithm in bioinformatics.
