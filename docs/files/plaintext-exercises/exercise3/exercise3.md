---
title: "Visual Search Asymmetry in Threat Detection"
author: "A. Student"
date: "2025-02-15"
abstract: |
  We tested whether threatening stimuli (snakes) are detected
  faster than non-threatening stimuli (flowers) in a visual search
  task with 40 undergraduate participants. Snakes were detected
  approximately 86 ms faster than flowers, supporting the threat
  superiority effect. The results are consistent with evolutionary
  accounts of attentional prioritization for threat-relevant stimuli.
bibliography: refs.bib
csl: apa.csl
geometry: margin=1in
fontsize: 12pt
header-includes: |
  \usepackage{booktabs}
---

# Introduction

The threat superiority effect refers to the faster detection of
threatening stimuli in visual search [@ohman2001fears]. From an
evolutionary perspective, organisms that rapidly detect threats in
the environment have a survival advantage, and this pressure may
have shaped attentional mechanisms that persist in modern humans
[@ohman2001fears].

This effect has been demonstrated across a range of stimulus types.
Snakes and spiders are detected faster than flowers and mushrooms
[@ohman2001fears; @rakison2009does], and angry faces are detected
faster than happy or neutral faces in visual search arrays
[@fox2000facial]. Neuroimaging evidence suggests the amygdala
plays a central role in this rapid threat detection pathway
[@vuilleumier2005how].

The present study aimed to replicate the threat superiority effect
using a standard visual search paradigm with snake and flower
targets among neutral distractors.

# Methods

## Participants

Forty undergraduate students (28 female, mean age = 19.8 years,
$SD = 1.2$) participated for course credit. All had normal or
corrected-to-normal vision and reported no specific phobia of
snakes. The study was approved by the university research ethics
board.

## Stimuli and Design

Color photographs of snakes (target, threat), flowers (target,
non-threat), and mushrooms (distractors) were selected from a
validated image set [@lipp2004images]. Each image subtended
approximately $2.5° \times 2.5°$ of visual angle.

Search displays contained 8 items arranged in a circle (radius =
$6°$) around a central fixation cross. On target-present trials
(50%), one item was the target (snake or flower) among 7
mushroom distractors. On target-absent trials, all 8 items were
mushrooms.

We used a 2 (target type: snake, flower) $\times$ 2 (target
presence: present, absent) within-subjects design. Each
participant completed 200 trials (50 per cell), presented in
random order.

## Apparatus

Stimuli were displayed on a 24-inch LCD monitor (1920 $\times$
1080 pixels, 60 Hz) at a viewing distance of 57 cm. The
experiment was programmed in PsychoPy [@peirce2019psychopy].

## Data Analysis

Trials with reaction times shorter than 200 ms or longer than
2000 ms were excluded as anticipations or lapses (1.8% of all
trials). We computed mean reaction times for correct responses
in each condition and analyzed them using a 2 $\times$ 2
repeated-measures ANOVA.

The effect size was quantified using partial eta squared:

$$\eta_p^2 = \frac{SS_{\text{effect}}}{SS_{\text{effect}} + SS_{\text{error}}}$$

# Results

Mean reaction times are shown in Table 1. There was a significant
main effect of target type, $F(1, 39) = 14.2$, $p < .001$,
$\eta_p^2 = .27$, indicating that snake targets were detected
faster than flower targets. There was also a significant main
effect of target presence, $F(1, 39) = 89.4$, $p < .001$,
$\eta_p^2 = .70$, with present trials faster than absent trials.
The interaction was not significant, $F(1, 39) = 1.03$,
$p = .316$.

| Target  | Present     | Absent      |
|---------|-------------|-------------|
| Snake   | 612 (89)    | 831 (102)   |
| Flower  | 698 (94)    | 854 (110)   |

: Mean reaction times in milliseconds by target type and target
presence. Standard deviations in parentheses. {#tbl:rts}

The search asymmetry—faster detection of snakes compared to
flowers—was 86 ms on target-present trials and 23 ms on
target-absent trials.

![Mean reaction time by condition. Error bars show $\pm 1$ SE.](search_figure.pdf){width=70%}

# Discussion

Our findings replicate the threat superiority effect
[@ohman2001fears]. Snake targets were detected approximately 86 ms
faster than flower targets on target-present trials, with a large
effect size ($\eta_p^2 = .27$). This is consistent with the
proposal that attention is preferentially allocated to
phylogenetically relevant threat stimuli.

The pattern of results is informative. The larger search asymmetry
on target-present trials than target-absent trials suggests that
the effect is driven primarily by faster *detection* of snakes
rather than faster *rejection* of snake-absent displays. This is
consistent with the idea that threatening stimuli capture attention
rather than simply being easier to categorize [@fox2000facial].

One limitation of the current study is that we did not control for
low-level visual features such as spatial frequency or color
distribution. It is possible that snakes are simply more visually
distinctive than flowers among mushroom distractors. Future studies
should use scrambled-image controls or match stimuli on low-level
properties [@lipp2004images].

In conclusion, these results add to the body of evidence supporting
an evolved attentional bias toward threat-relevant stimuli. The
robustness of this effect across many studies and paradigms suggests
it reflects a fundamental feature of human visual attention
[@vuilleumier2005how].

# References
