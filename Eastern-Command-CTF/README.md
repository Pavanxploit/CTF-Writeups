# Eastern Command & PARCHAM CTF — Cybersecurity Investigation Portfolio

This repository documents my learning and practical work across two stages of cybersecurity assessments. It covers the investigation methods I used, the challenges I worked on, and the technical concepts I learned while solving them.

This is my personal portfolio and independent documentation. It is not an official report from Eastern Command or the organizers of the assessments.

## About This Repository

I created this repository to keep my cybersecurity investigation notes, challenge write-ups, scripts, and supporting evidence organized in one place.

The work is divided into two parts:

- **Round 1 — Threat Intelligence & Security Analytics:** Malware analysis, log investigation, and intercepted-audio denoising and transcription.
- **Round 2 — PARCHAM CTF:** Technical challenges involving CEMA, RF Analysis, UAV systems, and 5G/Mobile Analysis.

Each write-up focuses on the approach I took to understand the problem, analyze the available data, verify my findings, and document the results. Where applicable, I also include scripts and evidence that help explain or reproduce the analysis.

## Repository Structure

```text
.
├── README.md
├── round-1-threat-intelligence/
│   ├── README.md
│   ├── reports/
│   │   └── report-template.md
│   └── evidence/
│       └── README.md
├── round-2-parcham-ctf/
│   ├── README.md
│   ├── challenges/
│   │   ├── uav-dead-reckoning.md
│   │   ├── uav-hopscotch-ii.md
│   │   ├── uav-consensus.md
│   │   └── challenge-index.md
│   ├── scripts/
│   │   └── README.md
│   └── evidence/
│       └── README.md
├── methodology/
│   └── investigation-workflow.md
└── .gitignore
```

## Areas I Worked On

The assessments gave me an opportunity to practise different investigation and data-analysis techniques.

- **Malware analysis:** Examining available artifacts and documenting relevant observations.
- **Log analysis:** Investigating event records to understand suspicious activity and reconstruct a sequence of events.
- **Audio analysis:** Working on noise reduction and transcription of intercepted audio.
- **Python and data analysis:** Using scripts to process data, test ideas, and reproduce results.
- **UAV data analysis:** Examining trajectory and sensor data to investigate movement and positioning.
- **RF analysis:** Studying signal characteristics, frequency patterns, and channel behaviour.
- **Technical reporting:** Recording the methodology, evidence, findings, and limitations of an investigation.

This list reflects the areas covered by my assessment work. The individual write-ups describe the specific tools and techniques used for each challenge.

## Round 1 — Threat Intelligence & Security Analytics

The first round involved three investigation tasks:

1. **Malware analysis** — Examine the supplied artifacts and document the analysis process and relevant findings.
2. **Log analysis** — Investigate the available logs to determine what happened, identify the affected systems or accounts where supported by evidence, and establish how the activity occurred.
3. **Audio denoising and transcription** — Process the supplied audio to improve intelligibility and recover as much of the spoken content as possible.

My documentation for this round records the investigation steps, tools used, important observations, supporting evidence, and conclusions. It also distinguishes between findings directly supported by the artifacts and interpretations that require further verification.

[View Round 1 documentation](round-1-threat-intelligence/README.md)

## Round 2 — PARCHAM CTF

The second round involved technical challenges across four tracks:

- CEMA
- RF Analysis
- UAV
- 5G/Mobile Analysis

The challenges required me to examine the supplied data, understand the underlying technical problem, and work towards a result that could be supported by analysis.

The UAV challenge notes in this repository cover topics such as dead-reckoning data, hop-pattern analysis, and sensor-based position estimation. Each write-up explains the problem, the approach taken, the relevant calculations or scripts, and the result obtained.

A screenshot captured during the assessment showed my profile at **8th place with 10,025 points**. This records the leaderboard as it appeared at that particular time; it should not be interpreted as the final event ranking.

[View Round 2 documentation](round-2-parcham-ctf/README.md)

## How I Document an Investigation

I use the following workflow to keep my analysis organized and make my conclusions easier to verify.

1. **Understand the scope:** Identify the objective, available artifacts, and permitted actions.
2. **Preserve the original data:** Keep source files unchanged and perform analysis on working copies.
3. **Record file hashes:** Use hashes when appropriate to identify files and check their integrity.
4. **Examine the evidence:** Inspect the relevant artifacts, logs, signals, or datasets.
5. **Maintain investigation notes:** Record commands, observations, timestamps, and important decisions.
6. **Validate important findings:** Cross-check results against other available evidence wherever possible.
7. **Document the reasoning:** Explain how the evidence supports each conclusion rather than presenting only the final answer.
8. **Record limitations:** Mention missing data, assumptions, uncertainties, and anything that could not be verified.
9. **Make the work reproducible:** Include suitable scripts and instructions when sharing them is permitted.
10. **Review before publishing:** Remove sensitive information and check the applicable challenge rules.

## Responsible Disclosure and Publishing

This repository is intended for learning, technical documentation, and professional portfolio development.

I will publish only material that I am authorized to share. Original challenge archives, malware samples, private correspondence, access links, credentials, personal information, and restricted challenge solutions will not be included where their disclosure is prohibited by the relevant rules or permissions.

Any scripts or techniques documented here must be used only in environments where the necessary authorization has been obtained.

## Disclaimer

This is an independently maintained educational portfolio. It is not an official publication and does not imply employment, affiliation, sponsorship, or endorsement by Eastern Command, PARCHAM, or the event organizers.

All third-party materials remain subject to their respective owners' rights and applicable event rules. The findings and explanations in individual write-ups represent my own analysis of the materials I was permitted to examine.