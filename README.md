# Third Semester Portfolio: Pre-Semester Version

This monorepo tracks my transition from writing backend exploratory data analysis scripts to deploying full-stack, low-latency web applications. The core theme so far across these projects is breaking down complex sports telemetry data using high-performance computation.

---

## Author's Note
After an eventful first year of engineering, I wanted to use this semester break to dive into data analysis and build a solid foundation. It started as a personal challenge to write clean backend exploratory data analysis scripts (`GridVector-Core` and `Regista`).

However, once the data logic was working, I decided to push myself a step further and finally learn frontend development (through `GridVector-App`), which has always been something I've wanted to learn.

With the start of the world cup, I wanted to see if I could predict who'll be crowned champions so I started working on `Into the Qualiverse`.

This repository serves as a sandbox for my third semester, going from EDA to endpoints and everything in between.

>"Our goal is to win Premier League"  
> ~A very unfortunate Ruben Amorim

## Repository Structure

The workspace is organized into two primary segments: core exploratory data engines and interactive web applications.

```
📁 third-sem/
│
├── 📁 EDA/                       # Pure Mathematical Data Engines
│   ├── 📁 Regista/               # UCL Playmaking Normalization Engine
│   │   ├── reg.py                # Pandas execution script
│   │   ├── Midfield_Playmaking.csv
│   │   └── README.md
│   │
│   └── 📁 GridVector/            # F1 2025 Telemetry Analysis Core
│       ├── gridvector-core.py    # NumPy array slicing scripts
│       ├── F1_2025_RaceResults.csv
│       └── README.md
│
|── 📁 Frontend/                  # Full-Stack Application Layer
|   │
|   └── 📁 GridVector-App/        # Interactive Paddock Dashboard
|       ├── 📁 Fonts/             # Snasm.ttf assets
|       ├── 📁 Images/            # Visual UI layouts & logos
|       ├── app.py                # Flask REST API Middleware
|       ├── index.html            # Dashboard structure
|       ├── style.css             # Dark-mode neon style layout
|       ├── index.js              # Asynchronous DOM event handlers
|       ├── F1_2025_RaceResults.csv
|       └── README.md
|── 📁 ITQ/
|   │
|   ├── 📁 Data/                  # Files containing standings
|   │   ├── 📁 Placeholders/      # Initial placeholder CSV files
|   │   │   ├── F.csv            
|   │   │   ├── QF.csv
|   │   │   ├── R16_placeholder.csv
|   │   │   ├── SF.csv
|   │   │   └── W.csv  
|   │   ├── annex_c.csv           # Compiled official FIFA annex C
|   │   ├── extraction.py         # Python script to convert fotmob json to csv
|   │   ├── F.csv                 # Generated file for teams competing for finals (semi-finalists)
|   │   ├── odds.csv              # Curated file containing odds for round 3
|   │   ├── R_16.csv              # Generated file for teams competing for R16 (R32 team)
|   │   ├── SF.csv                # Generated file for teams competing for semi-finals (quarter-finalists)
|   │   ├── standings.csv         # Initial standings before round 3
|   │   ├── W.csv                 # Generated file for teams competing to win (finalists)
|   │   └── xg.csv                # Flattened csv for each team's xg
|   │
|   ├── 📁 Scripts/               # Pandas execution scripts
|   │   ├── 📁 Time Warp 1 (R32)/ # Preliminary baseline trials              
|   │   │   ├── itq_script_uo.py  # Script using odds              
|   │   │   ├── itq_script_xg.py  # Script using xg
|   │   │   └── README.md                
|   │   ├── itq_phase_five.py     # Script generates finalists             
|   │   ├── itq_phase_four.py     # Script generates semi-finalists
|   │   ├── itq_phase_six.py      # Script generates winner
|   │   ├── itq_phase_three.py    # Script generates quarter-finalists
|   │   ├── itq_phase_two.py      # Script generates R16
|   │   └── log.txt               # Model validation log
|   └──README.md 
├──todo.txt
└──README.md (this file)

```

---
## Pre-Semester Projects

For full implementation details, mathematical breakdowns and documentation, please refer to the individual project directories:

* **[Regista](./EDA/Regista/README.md):** Advanced UCL midfield playmaking analysis using customized position-stratified scoring using Pandas.
* **[GridVector-Core](./EDA/GridVector/README.md):** High-performance, low-level F1 simulation data engine built completely on pure NumPy array masking.
* **[GridVector-App](./Frontend/GridVector-App/README.md):** Full-stack interactive evolution of the data core, mapping analytics to an asynchronous neon dark-mode UI.
* **[Into the Qualiverse](./EDA/ITQ/README.md):** parsimonious prediction engine using a Poisson probability distribution to identify the single most mathematically probable path to the finals.

---
## Author Details
**Developer:** [Sameeha Yasmin](https://github.com/Sam4907)

**Contact me:** [samyasmin49@gmail.com](mailto:samyasmin49@gmail.com)

**LinkedIn:** https://www.linkedin.com/in/sameeha-yasmin-a75a1437b/