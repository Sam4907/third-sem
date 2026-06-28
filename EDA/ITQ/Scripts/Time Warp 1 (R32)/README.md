# Time Warp 1 (R32)

This directory contains the computational engine designed to simulate the FIFA World Cup Group Stage (Phase 1) and resolve the final round-of-32 qualification pool.

---

## Author's Note
After a small break from EDA which led me to frontend development, I couldn't resist coming back to analyse data and draw inferences from it. So, with the ongoing FIFA World Cup 2026 going on, I tried to predict who'll make it to the Round of 32 using only permutations and combinations on paper. Spoiler alert: it took way too long and my brain couldn't consider all the possibilites at once. So I decided to write code for it. Spoiler alert again: it took way too long. 

I think the reason it took so long was because I had to prepare all the csv files used for this project myself. If that had been avoided, then it would've been easier. But the fact that I had the csv files just as I wanted them, it was much easier to parse data and visualise the matrix. Another thing that is important to note is that I designed this engine to only predict the final matchday results so I could reduce the number of moving parts, as I'm still starting out. Moreover, I had to use a very standard 1-0 scoreline for a win. 

When I first started calculating weights to assign to each parallel group outcome, my baseline instinct was to map betting odds. However, I quickly realized that betting lines are highly volatile and inherently warped by market sentiment and reputation rather than technical form. Navigating that preliminary odds-based path produced some highly erratic results, which ultimately forced me to pivot toward a mathematically robust Poisson Matrix Model. While the final qualifying lists have plenty of overlap, anchoring the engine to an expected goals ($xG$) framework ensures the predictions favor true tactical efficiency over public hype.

Now, we wait for Matchday 3 to wrap up on the pitch so we can see how the Qualiverse stacks up against reality.

>Spider-Man 2099: This here, this is all of us. All of our lives woven together in a beautiful web of life and destiny
>
>Miles Morales 1610: The Spider-Verse...
>
>Spider-Man 2099: Spider-Verse, oh, that's stupid. It's called the Arachno-Humanoid Poly-Multiverse. Which sounds stupid too, I guess. 

## Project Evolution

The Group Stage engine underwent a significant algorithmic overhaul to isolate the simulation from external market biases:

### Stage 1: The Bookmaker Model (Odds-Based)
The initial iteration of the script (see `itq_script_uo.py`) ingested public bookmaker data (`odds.csv`). While functionally complete, this version was heavily compromised by market vulnerabilities:
* **Public Hype Bias:** Odds reflected public betting volumes and historical reputation rather than current technical form.
* **What went wrong:** Relying strictly on betting lines caused major anomalies in group progression. For instance, in Group B, public betting heavily favored a traditional powerhouse narrative, advancing Switzerland as group winners while dropping an in-form Canadian side to a lower seed, which did not sit right with me, hence the analytical upgrade.

### Stage 2: Poisson Matrix Model
To establish an objective data basis, the legacy engine was decoupled from bookmaker files. The system now maps pure, underlying team execution metrics derived directly from tournament data (`xg.csv`):
* **Expected Goals (xG):** Quantifies territorial dominance and high-quality chance creation to establish an absolute Attack Strength rating.
* **Goals Against (GA):** Quantifies defensive structural integrity to calculate a Defense Weakness factor.
* **Note:** In further iterations of the model, Elo ratings have also been included.

---

## Core Mathematics Involved

### 1. Strength Vector Normalization
Raw team statistics are converted into relative performance factors by dividing them against the macro-tournament average per match:

$$\text{Attack Strength}_A = \frac{\text{xG Generated}_A / \text{Matches Played}}{\text{Tournament Average xG}}$$

$$\text{Defense Weakness}_A = \frac{\text{Goals Conceded}_A / \text{Matches Played}}{\text{Tournament Average GA}}$$

### 2. The Poisson Distribution Grid
When Team A plays Team B, their relative strength vectors are cross-multiplied against the tournament scoring average to isolate match-specific expected goal goals ($\lambda_A, \lambda_B$):

$$\lambda_A = \text{Attack Strength}_A \times \text{Defense Weakness}_B \times \text{AvgGoals}_{\text{tournament}}$$

A $6 \times 6$ scoreline grid matrix is generated via independent Probability Mass Functions ($PMF$):

$$P(X=x, Y=y) = \frac{\lambda_A^x e^{-\lambda_A}}{x!} \times \frac{\lambda_B^y e^{-\lambda_B}}{y!}$$

Summing the respective triangles and diagonals of the joint probability grid yields isolated, mathematically pristine probabilities for a Home Win, Draw and Away Win.

This transition immediately corrected the model's trajectory. Swapping to xG revealed that Canada was significantly underpriced by the market. In the Poisson matrix simulation, this data asset correctly propelled Canada to the top of Group B with a $+7$ simulated goal difference, aligning the simulation with true tactical efficiency rather than public speculation.

---

## Final Round of 32
Time Warp 1 automates the complex 12-group FIFA progression logic:
1. **Top 24:** It filters and extracts the top 2 teams from Groups A-L using a strict descending hierarchy: Points $\rightarrow$ Goal Difference $\rightarrow$ Goals Scored.
2. **Additional 8:** The 12 third-place survivors are consolidated into a temporary matrix. The engine runs a global tournament-wide descending sort across their point profiles and executes a strict `.head(8)` slice, instantly eliminating the bottom 4 underperforming variants.

---
## Author Details
**Developer:** [Sameeha Yasmin](https://github.com/Sam4907)

**Contact me:** [samyasmin49@gmail.com](mailto:samyasmin49@gmail.com)

**LinkedIn:** https://www.linkedin.com/in/sameeha-yasmin-a75a1437b/