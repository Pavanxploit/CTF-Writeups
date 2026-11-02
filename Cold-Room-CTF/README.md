# Cold Room CTF – Google SecOps Threat Hunting

A hands-on Security Operations and Threat Hunting CTF documenting my investigation of three multi-stage intrusion scenarios using **Google Security Operations (Google SecOps / Chronicle)**.

The challenge involved investigating simulated enterprise attacks, generating and refining UDM queries, analysing security events, identifying attacker activity, and mapping findings to MITRE ATT&CK.

**Investigation:** 3 attack scenarios | 18 flags

## Skills Demonstrated

- SIEM Investigation – Google SecOps
- Threat Hunting and Event Analysis
- Unified Data Model (UDM) Queries
- AI-Assisted Query Generation and Validation
- MITRE ATT&CK Framework
- Detection Engineering – YARA-L
- Security Log Analysis
- Incident Investigation and Attack Timeline Reconstruction

## Investigation Scenarios

| Scenario | Attack Theme | Flags |
|---|---|---|
| Scenario 1 – FAKEUPDATES | Fake browser updates, Kerberoasting, lateral movement and data staging | 1–6 |
| Scenario 2 – OAuth Heist | Credential phishing, MFA tampering, Google Drive theft and database exfiltration | 7–12 |
| Scenario 3 – Rogue Synthesis | AI-enabled malware, malicious IDE extension and CI/CD compromise | 13–18 |

## Investigation Methodology

My investigation workflow involved:

1. Analysing challenge briefings and identifying relevant attack indicators.
2. Translating investigation questions into searchable security artifacts.
3. Using the Google SecOps query generator to generate initial UDM queries.
4. Reviewing, refining and executing queries.
5. Analysing event details, raw logs and relevant UDM fields.
6. Pivoting across users, IP addresses, domains, processes and files.
7. Reconstructing attack timelines and mapping activity to MITRE ATT&CK.

## Repository Contents

The detailed investigation documentation is maintained in the `files/ctf-secops-threat-hunting/` directory.

- **Scenario walkthroughs:** Investigation steps, query prompts, results and troubleshooting.
- **Attack timelines:** Reconstruction of attacker activity.
- **MITRE ATT&CK mappings:** Techniques associated with each scenario.
- **Detection rules:** Experimental YARA-L detection drafts.
- **Cheatsheets:** UDM field pitfalls and query-generator prompt patterns.

## Tools and Technologies

- Google Security Operations (Chronicle)
- Unified Data Model (UDM)
- YARA-L
- MITRE ATT&CK
- Security Event Analysis
- Threat Hunting

## Key Learnings

- Building effective UDM queries from investigation requirements.
- Understanding event relationships and relevant UDM fields.
- Investigating suspicious authentication and endpoint activity.
- Pivoting between security telemetry sources.
- Identifying why initial queries return incomplete or irrelevant results.
- Reconstructing multi-stage attack scenarios.
- Translating investigation findings into detection engineering ideas.

## AI Assistance and Validation

AI assistance was used as a guide during parts of the investigation, particularly for query-generation prompts, UDM query refinement and understanding event fields.

All searches were executed in the Google SecOps training environment. The investigation journals document unsuccessful approaches and corrections.

The YARA-L detections are experimental drafts and have not all been validated in a live production tenant.

## Disclaimer

- All investigations were conducted in an authorised CTF/training environment.
- Flag values have been redacted.
- No real organisation's logs, credentials or confidential information are included.
- This project is an independent educational exercise and is not affiliated with Google or the CTF organisers.

---

**Author:** Pavan Kumar  
**GitHub:** [@Pavanxploit](https://github.com/Pavanxploit)