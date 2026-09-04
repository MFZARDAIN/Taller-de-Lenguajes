# 🏆 Programming Language Popularity — TIOBE Index (February 2026)

> Comprehensive dataset and analysis of programming language popularity based on the TIOBE Programming Community Index

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![TIOBE](https://img.shields.io/badge/Source-TIOBE_Index-blue)](https://www.tiobe.com/tiobe-index/)
[![Python](https://img.shields.io/badge/Python-3.9+-green.svg)](https://python.org)

---

## 📋 Overview

The **TIOBE Programming Community Index** is one of the most widely recognized indicators of programming language popularity worldwide. This dataset provides:

- **Current rankings** for 28 programming languages (February 2026)
- **Historical trends** spanning 26 years (2001–2026) for the top 10 languages
- **Hall of Fame** — every "Language of the Year" winner from 2003–2024

## 📁 Files

| File | Records | Description |
|------|---------|-------------|
| `tiobe_index_feb_2026.csv` | 28 | Current language rankings with ratings, paradigms & metadata |
| `tiobe_historical_yearly.csv` | 26 | Yearly average positions for top 10 languages (2001–2026) |
| `tiobe_hall_of_fame.csv` | 22 | Language of the Year winners (2003–2024) |

## 📊 Key Columns

### `tiobe_index_feb_2026.csv`
| Column | Type | Description |
|--------|------|-------------|
| `Rank` | int | Current TIOBE ranking position |
| `Language` | str | Programming language name |
| `Rating_Pct` | float | Market share percentage |
| `Change_Pct` | float | Year-over-year change in rating |
| `Status` | str | Trend direction (↑/↓/=) |
| `Paradigm` | str | Programming paradigm (OOP, Functional, etc.) |
| `Year_Created` | int | Year the language was first released |
| `Creator` | str | Original creator(s) |
| `Primary_Use` | str | Main use cases |
| `Typing` | str | Type system (Static/Dynamic/N/A) |

### `tiobe_historical_yearly.csv`
| Column | Type | Description |
|--------|------|-------------|
| `Year` | int | Calendar year (2001–2026) |
| `Python`, `C`, `C++`, ... | int | Average ranking position for that year |

### `tiobe_hall_of_fame.csv`
| Column | Type | Description |
|--------|------|-------------|
| `Year` | int | Award year |
| `Language` | str | Winning language |
| `Rating_Change_Pct` | float | Percentage rating increase that year |

## 🔑 Key Insights

- **Python** dominates with **21.81%** rating — 10+ points ahead of C
- Python peaked at **26.98%** in July 2025 before domain-specific languages gained ground
- **R** and **Perl** have staged comebacks into the top 11
- **Rust** continues rising (rank #14, +0.38%), while **PHP** declines (rank #13)
- Python has won **Language of the Year** 6 times — more than any other language

## 🔬 Methodology

The TIOBE Index is calculated based on the number of search engine results for queries of the form `+"<language> programming"` across **25+ search engines** including Google, Bing, Amazon, Wikipedia, Baidu, and others.

- The **maximum** of all query variants is used (not the sum) to avoid inflation
- Ratings represent the percentage of all hits for all indexed languages
- Only languages that are **Turing complete** and have a **Wikipedia entry** are included

**Data compilation for this dataset:**
- Current rankings: official TIOBE publication, February 2026
- Historical positions: TIOBE's published long-term history tables
- Hall of Fame: TIOBE's official archive
- Language metadata: cross-referenced with Wikipedia and official documentation

## 📚 Data Sources & Provenance

| Source | URL | Data Used |
|--------|-----|-----------|
| TIOBE Index | [tiobe.com/tiobe-index](https://www.tiobe.com/tiobe-index/) | Rankings, ratings, history |
| TIOBE Methodology | [tiobe.com/.../definition](https://www.tiobe.com/tiobe-index/programminglanguages_definition) | Index calculation method |
| Wikipedia | [wikipedia.org](https://wikipedia.org) | Language metadata |

## 📄 License

This dataset is released under **CC BY 4.0** (Creative Commons Attribution 4.0 International).

- You are free to share and adapt this dataset
- **Attribution required**: Please credit the TIOBE Index (www.tiobe.com) as the original data source

## 👤 Author

**Khurram Shahzad**
Mentor: **Dr. Aammar Tufail**

If you found this dataset useful, please consider **upvoting ⬆️** and **sharing**!
