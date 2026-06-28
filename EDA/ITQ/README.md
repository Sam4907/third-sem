# Into the Qualiverse
Into the Qualiverse is a parsimonious prediction engine that uses a Poisson probability distribution, driven by expected goals ($xG$, $xGA$) and Elo ratings, to simulate knockout brackets. By generating and weighting every possible tournament permutation, it identifies the single most mathematically probable path to the finals.

## Author's Note
As something that started out as just a zeal to predict who'd enter the Round of 32 in the FIFA World Cup, Into the Qualiverse has now evolved into a full-fledged mathematical prediction model. It dynamically reads standings as provided and uses primarily a Poisson probability distribution model to predict the survivors of the required bracket. The idea was to create a parsimonious implementation using a blend of expected goals ($xG$), expected goals against ($xGA$) and Elo ratings.

It is called `Into the Qualiverse` as a spin on `Into the Spiderverse` and also because I like to think of each permutation as a different universe. Each round is referred to as a `Time Warp` because it fit the theme perfectly and made perfect sense (at least in my head). The entire workflow of `Time Warp 1` can be found at the ["Scripts/Time Warp 1/README.md"](EDA/ITQ/Scripts/Time%20Warp%201%20(R32)/README.md). Adding onto that premilinary methodology, Elo ratings were included to add a historical aspect to the model.

Unable to find the `annex_c.csv` anywhere, as released by FIFA in a PDF (eye-roll), I realised that a smarter workaround to generating all complicated 495 possibilities myself for the R32 was simply converting the PDF to a `.xslx` file and finally into a CSV. This made accessing the lookup table so much easier and cleaner.

Furthermore, I encountered an annoying problem. I found myself looking up match data ($xG$ and $xGA$) every time I revisited the project. My first instinct to solve this problem was to quickly find an API that opened a backdoor to Sofascore or FotMob. Unfortunately, neither of the services provided an official API. The next solution I could think of was finding a scraper developed by a fellow fan. Despite trying quite a few options, I was unable to find a reliable repo for this purpose. Hence, I settled for a workaround. It didn't take long to find the json file (`fotmob_ext.json`) for the FotMob page and writing a quick Python script (`extraction.py`) to parse the required data into a clean CSV file (`xg.csv`). It does not provide instant and live data, but it semi-automated the process. 

I have to admit football (not soccer) is not an easy sport to predict. Dark horses are known for surprises and one bad match can ruin the entire campaign even for the best teams. For instance, watching Germany lose to Ecuador hurt me and the model. Finally, as for the model validation, only time will tell. The intermittent validation can be found at ["Scripts/log.txt"](EDA/ITQ/Scripts/log.txt). I will be updating each CSV file with the actual results after each round, but the original prediction will always be available in `log.txt`. For the time being, ITQ predicts `SPAIN` will take it home, and as a fan of the Spain NT, I'm not complaining!

>Dr. Strange: I went forward in time. To view alternate futures. To see all the possible outcomes of the coming conflict.
>
>Quill: How many did you see?
>
>Dr. Strange: Fourteen million, six hundred and five.
>
>Tony Stark: How many did we win?
>
>Dr. Strange: One.

## Project Structure
```
📁 ITQ/
│
├── 📁 Data/                  # Files containing standings
│   ├── 📁 Placeholders/      # Initial placeholder CSV files
│   │   ├── F.csv            
│   │   ├── QF.csv
│   │   ├── R16_placeholder.csv
│   │   ├── SF.csv
│   │   └── W.csv  
│   ├── annex_c.csv           # Compiled official FIFA annex C
│   ├── extraction.py         # Python script to convert fotmob json to csv
│   ├── F.csv                 # Generated file for teams competing for finals (semi-finalists)
│   ├── odds.csv              # Curated file containing odds for round 3
│   ├── R_16.csv              # Generated file for teams competing for R16 (R32 team)
│   ├── SF.csv                # Generated file for teams competing for semi-finals (quarter-finalists)
│   ├── standings.csv         # Initial standings before round 3
│   ├── W.csv                 # Generated file for teams competing to win (finalists)
│   └── xg.csv                # Flattened csv for each team's xg
│
├── 📁 Scripts/               # Pandas execution scripts
│   ├── 📁 Time Warp 1 (R32)/ # Preliminary baseline trials              
│   │   ├── itq_script_uo.py  # Script using odds              
│   │   ├── itq_script_xg.py  # Script using xg
│   │   └── README.md                
│   ├── itq_phase_five.py     # Script generates finalists             
│   ├── itq_phase_four.py     # Script generates semi-finalists
│   ├── itq_phase_six.py      # Script generates winner
│   ├── itq_phase_three.py    # Script generates quarter-finalists
│   ├── itq_phase_two.py      # Script generates R16
│   └── log.txt               # Model validation log
│
└──README.md (this file)
```

## Execution Flow

To simulate the tournament from the group stage through to crowning the champion, the scripts must be run sequentially. Each phase updates the respective standings and dynamically generates the matchup brackets for the subsequent round.

### 1. Data Ingestion & Preprocessing
If you need to update the underlying expected goals data from the raw FotMob tracker file before running the model:

```bash
python Data/extraction.py
```
This parses `fotmob_ext.json` and overrides `Data/xg.csv` with updated, flattened metrics.

### 2. Simulating the Knockout Stages
Run the execution pipeline in chronological order. Each script reads the current state of the universe, applies the Poisson distribution combined with Elo ratings, and outputs the survivors:

```bash
# Phase 2: Predicts Round of 32 outcomes -> Generates Round of 16 Brackets
python Scripts/itq_phase_two.py

# Phase 3: Predicts Round of 16 outcomes -> Generates Quarter-Finalists
python Scripts/itq_phase_three.py

# Phase 4: Predicts Quarter-Final outcomes -> Generates Semi-Finalists
python Scripts/itq_phase_four.py

# Phase 5: Predicts Semi-Final outcomes -> Generates Finalists
python Scripts/itq_phase_five.py

# Phase 6: Predicts the Grand Final -> Generates the Winner
python Scripts/itq_phase_six.py
```
---
## Author Details
**Developer:** [Sameeha Yasmin](https://github.com/Sam4907)

**Contact me:** [samyasmin49@gmail.com](mailto:samyasmin49@gmail.com)

**LinkedIn:** https://www.linkedin.com/in/sameeha-yasmin-a75a1437b/