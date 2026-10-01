# Numerical Analysis - Polynomial Interpolation

This repository contains the Python implementation of polynomial interpolation methods (Lagrange and Newton) along with the final assignment report.

## Repository Structure

- lagrange/
  - lagrange.py: Implementation of Lagrange interpolation algorithm.
  - graphes.py: Plotting scripts for exponential function exp(x).
- newton/
  - newton.py: Implementation of Newton's divided differences algorithm.
  - graphes.py: Plotting scripts for logarithmic function log2(x).
- Report.pdf: Final academic report with results, graphs, and conclusions.
- README.md: Repository documentation.

## Summary of Results

- Lagrange Method: Tested on f(x) = exp(x). Increasing the number of interpolation nodes significantly improves accuracy.
- Newton Method: Tested on f(x) = log2(x) using divided differences. It yields mathematically equivalent results to Lagrange, but allows adding new nodes without recalculating from scratch.
