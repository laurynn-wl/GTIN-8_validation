# GTIN-8_validation

## Overview
This project implements a validation system for GTIN-8 (Global Trade Item Number) codes, which are commonly represented using barcodes. The GTIN-8 consists of a seven-digit code plus a check digit, which is crucial for ensuring the validity of the product code.

## Features
- **GTIN-8 Calculation:** Automatically calculates the eighth digit (check digit) for any given seven-digit number using a specific algorithm.
- **GTIN-8 Validation:** Validates an entire eight-digit GTIN-8 code by verifying that the computed check digit matches the provided check digit.

## Example
For the seven-digit code `1324562`, the check digit is computed to complete the GTIN-8 as `13245627`. The validation process involves summing the digits based on a pattern of multiplying every other digit by 3 and the others by 1, ensuring that the total is a multiple of 10.

## Usage
- Input any seven-digit number to receive the corresponding GTIN-8 code with its check digit.
- Input an eight-digit GTIN-8 code to check its validity.

This project provides a practical tool for managing GTIN-8 codes, improving accuracy in product identification.
