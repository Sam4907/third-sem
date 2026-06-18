# Third Semester Portfolio: Pre-Semester Version

This monorepo tracks my transition from writing backend exploratory data analysis scripts to deploying full-stack, low-latency web applications. The core theme across these projects is breaking down complex sports telemetry data using high-performance computation.

---

## Author's Note
After an eventful first year of engineering, I wanted to use this semester break to dive into data analysis and build a solid foundation. It started as a personal challenge to write clean backend exploratory data analysis scripts (`GridVector-Core` and `Regista`).

However, once the data logic was working, I decided to push myself a step further and finally learn frontend development, which has always been something I've wanted to learn.

This repository serves as a sandbox for my third semester, going from EDA to endpoints.

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
│
├──todo.txt
└──README.md (this file)

```

---
## Pre-Semester Projects

For full implementation details, mathematical breakdowns and documentation, please refer to the individual project directories:

* **[Regista](./EDA/Regista/README.md):** Advanced UCL midfield playmaking analysis using customized position-stratified scoring using Pandas.
* **[GridVector-Core](./EDA/GridVector/README.md):** High-performance, low-level F1 simulation data engine built completely on pure NumPy array masking.
* **[GridVector-App](./Frontend/GridVector-App/README.md):** Full-stack interactive evolution of the data core, mapping analytics to an asynchronous neon dark-mode UI.

---
## Author Details
**Developer:** [Sameeha Yasmin](https://github.com/Sam4907)

**Contact me:** [samyasmin49@gmail.com](mailto:samyasmin49@gmail.com)

**LinkedIn:** https://www.linkedin.com/in/sameeha-yasmin-a75a1437b/