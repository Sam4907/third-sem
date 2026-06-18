# GridVector: Custom F1 Driver Rankings & Performance Models

GridVector is a high-performance Python analytics engine designed to extract, transform, and evaluate Formula 1 race pace, overtakes, and driver efficiency indexes. It translates multi-axis racing telemetry data into distinct, actionable ranking models.

---

## 1. Author's Note

As a huge fan of both Formula 1 and data science, I built this project to merge two of my favorite worlds. My core objective was to break away from slow, repetitive `for-loops` and force myself to think purely in terms of multi-dimensional arrays. To do that, I wanted to get low-level with NumPy operations like advanced vectorization, data validation, boolean masking, multi-key indirect sorting (`np.lexsort`), and direct mathematical matrix manipulation. 

To challenge myself, I deliberately worked with a flat, multi-variant CSV dataset, limited to races from the 2025 F1 season. I avoided relying on Pandas abstractions and handled all data validation and manual string-to-numeric conversions myself to keep memory aligned. 

Some of these telemetry queries stretched me thin. When designing analytics like the Linear Weighted Moving Average (`gr_lwma`), I had to figure out how to map aggregated historical group properties back onto raw dataset rows without collapsing performance arrays. Overcoming those roadblocks forced me to master the nuances of NumPy broadcasting, vector tracking, and C-speed category binning (`np.bincount`). Ultimately, this project turned a raw passion for racing strategy into a deep, low-level understanding of how mathematical operations scale efficiently on real-world datasets.

> It's lights out and away we go!

---

## 2. Core Technical Engine & API Reference

GridVector parses raw race result matrices by leveraging fully vectorized operations. The logic is divided into two primary categories: Specialized Race Queries and Mathematical Frameworks.

### Specialized Race Queries

#### 1. Out-of-Position Recovery (`out_of_pos_recov`)
Queries specific instances where a designated driver started outside the Top 10 grid slots but executed a successful recovery drive to finish inside the points. It applies a strict multi-condition boolean mask to filter out status anomalies like DNFs, DQs, and non-classified (NC) states.

#### 2. Podium Lockout Tracker (`team_clean_sweep`)
Identifies when a single constructor dominated a race weekend. It applies an inverse boolean mask mapping array indices back to matching team metrics to pinpoint weekends where both cars secured a Top-3 podium finish simultaneously.

#### 3. Finishes and Retirals Rate (`racer_dnf`)
Calculates a driver's historical finishing reliability profile. It programmatically captures non-disqualified entries and evaluates the mathematical quotient of `DNF` text occurrences against total calendar events.

#### 4. Unrewarded Speedster (`fastest_lap_pointless`)
Isolates weekends where a driver achieved the fastest lap of the Grand Prix (`Set Fastest Lap == "Yes"`) but failed to finish within the Top 10 positions, meaning they were ineligible to secure the corresponding World Championship bonus point.

#### 5. The Perfect Weekend Trifecta (`masterclass`)
Scans the historical records to isolate supreme dominant driver performances. It returns rows where a driver simultaneously secured Pole Position (`Starting Pos == 1`), won the Grand Prix (`Pos == 1`), and logged the fastest lap of the race.

#### 6. Qualifying Drop-Off (`dropoff`)
Tracks structural pace degradation from Saturday to Sunday. This query filters for entries where a driver qualified in a premium Top 5 slot but suffered a severe drop-off during the main race to finish completely out of the point-scoring positions (`Points == 0`).

#### 7. Overtaker of the Race Grid Report (`gr_overtaker`)
Isolates genuine track-position gains. It filters out non-finishers and maps a structural delta vector ($Starting\ Pos - Final\ Pos$). It utilizes a multi-key indirect sort via `np.lexsort` combined with categorical maximum indexing to print a beautifully padded text-aligned grid report of maximum overtakes per track.

#### 8. Team Point Dominance (`mvp`)
Calculates instances where a single driver scored greater than 60% of their constructor's total points for a given weekend. This utilizes element-wise divisions powered by `np.bincount` to aggregate grouped team points instantly across variable array tracks without slow iterations.

#### 9. Bulletproof Chassis Check (`strong_team`)
Evaluates mechanical reliability across constructors. It computes a structural set difference via `np.setdiff1d` between the master array of teams and a subset tracking mechanical retirements (`DNF`) or technical disqualifications (`DSQ`) to reveal teams with perfect reliability.

#### 10. Aggregated Driver Efficiency (`strong_racer`)
Determines the field's most mathematically efficient racer by evaluating the specialized ratio:
$$\text{Efficiency Metric} = \frac{\text{Total Championship Points}}{\text{Average Starting Position}}$$
It aggregates points and grid positions across driver categories using fast `np.bincount` scaling, returning the optimal value index.

---

### Mathematical Frameworks

#### 11. Millisecond Conversion Parser (`float_conv`)
Handles low-level data transformation by cleaning string-based lap times (e.g., `1:24.532`). It applies text tokenization via `np.char.split`, vector-transposes the shape using `zip_longest`, and translates chronological strings into raw floating-point seconds:
$$\text{Seconds} = (\text{Minutes} \times 60) + \text{Seconds} + \left(\frac{\text{Milliseconds}}{1000}\right)$$

#### 12. Performance Consistency Index (`gr_eff_index`)
Instead of using basic averages, this function evaluates field consistency by calculating a driver's native **Standard Deviation** over completed race slots. It executes a completely vectorized algebraic matrix expansion for variance ($E[X^2] - (E[X])^2$) across element-wise squaring arrays:
$$\text{std} = \sqrt{\frac{\sum X^2}{N} - \left(\frac{\sum X}{N}\right)^2}$$

#### 13. Single-Driver Linear Weighted Moving Average (`lwma`)
Tracks localized form trends for a single asset. It isolates a driver's completed timelines, maps an incremental linear sequence matrix ($1, 2, \dots, K$), and calculates the dot-product weights to place heavier mathematical significance on current form versus early-season performance.

#### 14. Global Linear Decay Moving Average (`gr_lwma`)
The engine's primary ranking framework. It sorts the entire 2025 dataset chronologically per driver using `np.lexsort`. It builds an expanding, non-uniform weighting matrix across boundaries using nested `np.cumsum` shifts, performing a global, category-binned dot product to output the current momentum rank of the entire grid.

---

## 3. Tech Stack & Dependencies

* **Language Runtime:** Python 3.10+
* **Mathematical Core:** NumPy (Highly optimized vectorized array structures)
* **Data Sequence Handling:** Standard `itertools` library pipelines

---

## 4. Quick Start & Execution

### 1. Installation
Ensure you have the optimized NumPy mathematical library installed in your current runtime environment:
```bash
pip install numpy
```

### 2. Dataset Alignment
Ensure your `F1_2025_RaceResults.csv` tracking matrix is situated directly within the root project subfolder alongside your Python files.

### 3. Execution
To run the analytical suite and output all terminal grid reports, uncomment the execution calls at the base of the script and initialize:
```bash
python gv.py
```

---

## 👥 Authors & Data Attribution

* **Developer:** [Sameeha Yasmin](https://github.com/Sam4907)
* **Data Source:** Telemetry and results compiled from the 2025 F1 Season dataset hosted on [Kaggle](https://www.kaggle.com/datasets/makslypko/f1-race-result-2025).