# Basics of NumPy

A collection of hands-on Python notebooks covering core NumPy concepts, array operations, and practical data analysis exercises.

## Notebooks

### `numpy_data_science_practice.ipynb`
A practical walkthrough benchmarking NumPy against standard Python lists and applying array manipulation to sports data.

**Topics Covered:**
* **Performance Benchmarking:** Comparing execution speed between standard Python loops and vectorized NumPy operations across 1,000,000 elements (~85x speedup).
* **Array Creation & Attributes:** Working with 1D/2D arrays (`np.array`), placeholders (`np.zeros`, `np.ones`, `np.full`), ranges (`np.arange`), and inspecting `.shape`, `.size`, and `.dtype`.
* **Cricket Scorecard Analysis (2D Indexing & Slicing):**
  * Extracting specific rows, columns, and sub-matrices (top-order batting, match-wise scores).
  * **Fancy Indexing:** Targeting specific `(row, column)` coordinate pairs to update player scores in-place.
  * **Axis Operations:** Computing match totals using `np.sum(..., axis=1)`.
* **Custom Modules:** Creating and importing local `.py` helper modules (`%%writefile mytools.py`) inside Google Colab.

## Tech Stack
* **Language:** Python 3
* **Libraries:** NumPy (`v2.4.6`), Matplotlib
* **Environment:** Google Colab
