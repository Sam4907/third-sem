Markdown
# GridVector App: 2025 F1 Season Telemetry Dashboard

Building on GridVector-Core, GridVector-App is a full-stack, low-latency telemetry web application designed to track, calculate, and visualize driver and constructor performances from the 2025 Formula 1 season. Built on a pure vectorized NumPy computation engine and mapped via a lightweight Flask REST API, the platform delivers real-time sports analytics straight to a clean, custom-themed, interactive frontend dashboard.

---

## 1. Author's Note
This project started out as a neat, well-behaved local data script to learn exploratory data analysis called `GridVector-Core`. It did its math, it read its CSV, and life was simple. But then I had a reckless thought: *"What if I could present the analysis visually?"*. So, I finally embarked on the journey to pick up frontend, which I've always wanted to. Welcome to `GridVector-App`the full-stack evolution that gave me a massive pre-semester headache. 

Upgrading this engine meant moving past pure NumPy matrix operations and diving headfirst into the chaotic waters of web development. I had to wrangle with Flask routes, bypass CORS issues, and force Python types to play nice with JavaScript. Also, paying attention to detail was key. I spent hours working on the effect for the title of the page and even went as far as trying to customise dropdowns and the scrollbar. I spent way too long debugging custom font rendering for `Snasm.ttf`, hardcoding team-specific hex colors so the UI looked like a real paddock dashboard, and making sure my dropdown checkboxes closed properly when you clicked literally anywhere else on the screen. 

In the end, it works as intended. It translates raw vector masks into a dark-mode racing interface, proving that sports analytics doesn't have to look like a boring spreadsheet. I survived the full-stack upgrade, the API routes are green, and as Charles Leclerc once said...

> "Lando, we can be world champion I said. Please Lando. LANDO! Lando, Lando."

## 2. API Endpoint & Query Reference

The Flask backend exposes custom micro-routes executing high-performance analytical masks:

### Core Global Analytics

* **`/overtaker` (`gr_overtaker`)**: Filters out non-finishing states (`DQ`, `NC`, `DNF`) and computes the differential between starting and finishing positions across all tracks, sorting drivers by maximum grid progression.
* **`/eff` (`gr_eff_index`)**: Computes structural positional consistency by calculating driver standard deviations directly via raw bincount array weights:
  $$\sigma = \sqrt{\frac{\sum x^2}{N} - \left(\frac{\sum x}{N}\right)^2}$$
  The results are ceil-rounded and inverted to construct a volatility ranking.
* **`/lwma` (`gr_lwma`)**: Applies a Linear Weighted Moving Average across execution rows, sorting metrics chronologically by driver to prioritize more recent track performances.
* **`/constructor` (`strong_team`)**: Evaluates team reliability by analyzing set differences (`np.setdiff1d`) to isolate constructor operations that achieved zero mechanical DNFs or structural DSQs.
* **`/dnf` (`racer_dnf`)**: Maps driver career completions. Intersects unique entry structures against DNF instances to return live race completion percentages.
* **`/trifecta` (`masterclass`)**: Isolates flawless Grand Prix weekends by scanning for the ultimate racing triplet: starting from Pole Position (`P1`), claiming the Grand Prix Victory (`P1`), and securing the official Fastest Lap.
* **`/dropoff` (`dropoff`)**: Flags negative outliers by returning top-5 grid qualifiers who failed to score a single point (`Points == 0`) by the checkered flag.

### Parametric Selector Analytics

* **`/recovery/<driver>` (`out_of_pos_recov`)**: Tracks custom driver comebacks. Filters for rows where the designated driver started outside the top 10 (`>10`) but managed to recover into a point-scoring position.
* **`/clean/<team>` (`team_clean_sweep`)**: Aggregates track results to isolate dominant team lockouts where both active stable drivers secured a podium sweep ($\le 3$), displaying their cumulative points package.
* **`/mvp/<track>` (`mvp_per_track`)**: Computes positional dominance at an individual circuit by isolating drivers who accounted for more than 60.0% of their team's combined weekend point haul.

---

## 3. Frontend Implementation & Interface

The user interface uses a vanilla web approach designed around modern responsive dashboard components:

* **`index.html`**: Structures a two-column layout separating interactive sidebar menus from core telemetry layout container cards.
* **`style.css`**: Configures a premium neon aesthetic driven by custom typography (`Snasm.ttf`) alongside team specific identity coloring matrices mapped to runtime DOM components.
* **`index.js`**: Drives client-side navigation state handling, controls event bubbling on custom dropdown select boxes, issues asynchronous `fetch` queries, and dynamically maps raw JSON response vectors straight into safe HTML layouts.

---

## 4. Quick Start & Execution

### 1. Environment Setup
Install the lightweight data parsing and routing packages:
```bash
pip install flask flask-cors numpy
```

### 2. Launch the Application
Ensure F1_2025_RaceResults.csv and your asset folders (fonts/, Images/) are organized in the project folder, then boot up the local production host:

```Bash
python app.py
```
Once initialized, navigate your local browser endpoint to: http://127.0.0.1:5000/

# Author & Data Attribution

* **Developer:** [Sameeha Yasmin](https://github.com/Sam4907)
* **Data Source:** Telemetry and results compiled from the 2025 F1 Season dataset hosted on [Kaggle](https://www.kaggle.com/datasets/makslypko/f1-race-result-2025)