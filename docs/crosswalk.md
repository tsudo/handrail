# Master crosswalk

*Licensed Apache-2.0 (LICENSE-code). Copyright 2026 Jason Robbins (AI Security Risk Workbook v3.0); modifications copyright 2026 Keith Crawford. Generated from `data/` by the project's build step; edit the data, not this page. See NOTICE.*

Every control in the catalog, with where it sits in each framework. The [spreadsheet version](../kit/crosswalk.xlsx) adds how to verify each control, the evidence to keep, the functions that require it, and a reverse index you can filter by framework reference.

Standards are cited by identifier: ISO/IEC 42001 by clause or control number, CSA AI Controls Matrix and SOC 2 by bare ID, OWASP by ID. Read the standards themselves for their requirements. Control identifiers such as POS-01 come from the AI Security Risk Workbook v3.0.

**Applies:** E = every tool; V = anything bought, or built on a third-party model; F = when a listed function needs it.

## AI Posture & Governance (POS)

| Control | Name | Applies | ISO/IEC 42001 | NIST AI RMF | OWASP | MITRE ATLAS | EU AI Act | SOC 2 | CSA AICM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| POS-01 | Tool registration | E | A.4.2, A.6.2.7, A.9.4 | GOVERN 1.6, MAP 1.1, MAP 3.3 | LLM03, ASI04 | AML.M0023 | Art. 26, Art. 49, Art. 11 | CC6.1, CC3.2, CC2.1 | GRC-05, DCS-06, UEM-02, STA-16 |
| POS-02 | Risk classification | E | 6.1.2, 6.1.4, 8.4, A.5.2 | MAP 1.5, MAP 5.1, MEASURE 1.1, MANAGE 1.2 | LLM01, LLM10, ASI01, ASI10 | AML.TA0004, AML.TA0011, AML.M0035 | Art. 6, Art. 9, Art. 27 | CC3.1, CC3.2, CC3.4 | GRC-02, GRC-10, TVM-12 |
| POS-03 | Approval obtained | E | A.3.2, A.6.2.5, 5.3 | GOVERN 1.4, GOVERN 2.1, MANAGE 1.1 | LLM06, ASI03 | AML.M0021 | Art. 26(1), Art. 17 | CC5.1, CC5.3, CC8.1 | GRC-01, GRC-06, UEM-02, CCC-04 |
| POS-04 | Policy alignment | E | A.2.2, A.2.3, A.9.2 | GOVERN 1.1, GOVERN 1.2, GOVERN 2.2 | ASI09, LLM02 | AML.M0021, AML.M0018 | Art. 4, Art. 26 | CC1.1, CC1.4, CC2.2 | GRC-09, HRS-15, HRS-02 |
| POS-05 | Owner assignment | E | A.3.2, 5.3 | GOVERN 2.1, GOVERN 2.3, MAP 1.2 | ASI10, ASI03 | AML.M0019, AML.M0024 | Art. 26(2), Art. 17 | CC1.3, CC2.2 | GRC-06, DSP-06, STA-05 |
| POS-06 | Vendor assessment | V | A.10.2, A.10.3 | GOVERN 6.1, GOVERN 6.2, MAP 4.1, MAP 4.2 | LLM03, ASI04 | AML.T0010, AML.M0014, AML.M0023 | Art. 25, Art. 53, Art. 26, Art. 13 | CC9.2, CC3.2 | STA-01, STA-09, STA-12, STA-15, A&A-02 |
| POS-07 | Compliance mapping | F | 4.2, A.2.2, A.8.3 | GOVERN 1.1, MAP 1.1 | — | — | Art. 6, Art. 26, Art. 27, Art. 50 | CC1.1, CC2.3, CC3.1 | GRC-07, A&A-04 |
| POS-08 | Data residency review | F | A.7.3, A.10.3, A.7.5 | MAP 4.1, GOVERN 1.1, MANAGE 3.1 | LLM02, LLM03 | AML.M0005, AML.M0019 | Art. 22 | C1.1, CC6.7, P4.1 | DSP-19, DSP-10, STA-10 |

## Runtime Protection & Guardrails (RUN)

| Control | Name | Applies | ISO/IEC 42001 | NIST AI RMF | OWASP | MITRE ATLAS | EU AI Act | SOC 2 | CSA AICM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RUN-01 | Input validation | F | A.6.2.4, A.6.2.6 | MEASURE 2.7, MEASURE 2.5, MANAGE 2.2 | LLM01, LLM07, ASI01 | AML.T0051, AML.T0054, AML.T0068, AML.T0093, AML.M0020, AML.M0033 | Art. 15(5), Art. 15(1) | CC6.6, CC6.8, PI1.2 | AIS-08, AIS-15, TVM-11, LOG-14 |
| RUN-02 | Output filtering | F | A.6.2.6, A.8.2, A.9.3 | MEASURE 2.6, MEASURE 2.10, MANAGE 2.2, MANAGE 4.1 | LLM05, LLM02, LLM09 | AML.T0057, AML.T0077, AML.T0067, AML.T0102, AML.M0020, AML.M0033 | Art. 15(1), Art. 15(4), Art. 50(1) | PI1.3, PI1.4, C1.1, CC6.7 | AIS-09, LOG-15, TVM-11, IAM-18 |
| RUN-03 | Rate limiting (per user) | F | A.4.5, A.6.2.6 | MEASURE 2.7, MANAGE 2.2, MAP 3.2 | LLM10 | AML.T0034, AML.T0029, AML.T0024, AML.M0004 | Art. 15(1), Art. 15(5) | A1.1, CC6.1, CC7.2 | AIS-10, I&S-02, TVM-11 |
| RUN-04 | Rate limiting (per workload) | F | A.4.5, A.6.2.6 | MANAGE 2.2, MANAGE 2.4, MEASURE 2.7 | LLM10, ASI08, ASI10 | AML.T0034.002, AML.T0029, AML.M0036, AML.M0004 | Art. 15(1), Art. 14(4)(e) | A1.1, A1.2, CC7.2 | I&S-02, AIS-10, AIS-11 |
| RUN-05 | Content safety | F | A.5.4, A.5.5, A.9.3 | MEASURE 2.6, MEASURE 2.11, MANAGE 1.3 | LLM05, LLM09, ASI09 | AML.T0048, AML.T0054, AML.T0088, AML.M0020, AML.M0022 | Art. 5, Art. 50(1), Art. 53 | CC5.2, PI1.1 | TVM-11, TVM-02, AIS-09, GRC-09 |
| RUN-06 | Multi-modal input validation | F | A.6.2.4, A.7.4 | MEASURE 2.7, MEASURE 2.5 | LLM01, ASI01 | AML.T0129, AML.T0051.001, AML.T0043, AML.M0033 | Art. 15(5), Art. 15(1) | CC6.6, PI1.2 | AIS-08, AIS-15, LOG-14 |
| RUN-07 | Domain restrictions (egress) | F | A.6.2.5, A.4.5 | MEASURE 2.7, MANAGE 2.4 | LLM02, ASI02, ASI08 | AML.T0025, AML.T0086, AML.T0072, AML.T0008.005, AML.M0032, AML.M0030 | Art. 15(5) | CC6.6, CC6.7, CC6.1 | I&S-03, I&S-09, I&S-06 |
| RUN-08 | Prompt cache isolation | F | A.6.2.5, A.4.5 | MEASURE 2.10, MANAGE 2.4 | LLM02, ASI06 | AML.T0057, AML.T0092, AML.T0080.001, AML.M0031, AML.M0027 | Art. 15(5) | C1.1, CC6.1, CC6.3 | AIS-14, DSP-17, I&S-06 |
| RUN-09 | Fallback and graceful degradation | F | A.6.2.6, A.8.4, 10.2 | MANAGE 2.4, MANAGE 2.3, MANAGE 4.1 | LLM09, ASI08, ASI10 | AML.T0029, AML.T0031, AML.T0076 | Art. 15(4), Art. 14(4)(e), Art. 20 | A1.2, A1.3, CC7.5, CC9.1 | BCR-04, BCR-09, MDS-11, CCC-09 |

## Shadow AI & Usage Discovery (SHA)

| Control | Name | Applies | ISO/IEC 42001 | NIST AI RMF | OWASP | MITRE ATLAS | EU AI Act | SOC 2 | CSA AICM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SHA-01 | Tool visibility | E | A.4.2, A.6.2.6 | GOVERN 1.6, GOVERN 1.5, MAP 1.1 | LLM03, ASI04 | AML.T0047, AML.T0132, AML.T0114, AML.M0023, AML.M0024 | Art. 26, Art. 4 | CC6.1, CC7.1, CC7.2 | UEM-04, UEM-02, DCS-06, LOG-07 |
| SHA-02 | Sanctioned status | E | A.9.2, A.2.2 | GOVERN 1.4, GOVERN 1.6, MANAGE 1.1 | LLM03, ASI04 | AML.M0021, AML.M0019 | Art. 26(1), Art. 4 | CC6.1, CC6.8, CC5.3 | UEM-02, GRC-04, HRS-15 |
| SHA-03 | User access tracked | F | A.6.2.8, A.6.2.6 | GOVERN 1.5, MEASURE 2.4, MANAGE 4.1 | LLM02, ASI03 | AML.M0024, AML.T0012, AML.T0040 | Art. 12, Art. 26(6), Art. 14 | CC6.1, CC7.2, CC4.1 | LOG-12, LOG-04, IAM-13 |
| SHA-04 | Usage analytics | F | A.6.2.6, 9.1 | MEASURE 2.4, MANAGE 4.1, MEASURE 3.1 | LLM10, ASI10 | AML.M0024, AML.T0034, AML.T0029 | Art. 26(5), Art. 72, Art. 12 | CC7.2, CC4.1, A1.1 | LOG-03, LOG-05, LOG-13, I&S-02 |
| SHA-05 | Personal-account blocking | V | A.9.2, A.2.2 | GOVERN 1.5, MANAGE 2.2, MEASURE 2.10 | LLM02 | AML.T0057, AML.M0019, AML.M0021 | Art. 26, Art. 4 | CC6.6, CC6.7, C1.1 | UEM-11, I&S-09, HRS-15, DSP-10 |

## Observability & Evaluation (OBS)

| Control | Name | Applies | ISO/IEC 42001 | NIST AI RMF | OWASP | MITRE ATLAS | EU AI Act | SOC 2 | CSA AICM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OBS-01 | Audit logging | F | A.6.2.8, A.6.2.7 | GOVERN 4.2, MEASURE 2.4, MEASURE 2.8, MANAGE 4.1 | LLM01, LLM10, ASI01, ASI10 | AML.M0024 | Art. 12, Art. 19, Art. 26(6) | CC7.2, CC7.3, CC4.1 | LOG-07, LOG-08, LOG-11, LOG-14, LOG-15 |
| OBS-02 | Log retention | F | A.6.2.8, 7.5 | GOVERN 4.2, MEASURE 2.8, MANAGE 4.3 | LLM01, ASI01, ASI10 | AML.M0024 | Art. 19(1), Art. 26(6) | CC7.2, CC7.3, CC4.1 | LOG-02, LOG-09, DSP-16 |
| OBS-03 | SIEM integration | F | A.6.2.6, A.8.4 | MEASURE 2.7, MANAGE 4.1, GOVERN 4.3 | ASI08, ASI10 | AML.M0024, AML.T0051, AML.T0086, AML.T0101 | Art. 15(5), Art. 26(5), Art. 73 | CC7.2, CC7.3, CC7.4 | LOG-03, LOG-05, SEF-06 |
| OBS-04 | Alerting configured | F | A.6.2.6, A.8.4 | MANAGE 4.1, MEASURE 3.1, MEASURE 3.3 | LLM10, ASI10, ASI08 | AML.M0024, AML.M0038 | Art. 26(5), Art. 14(4), Art. 72 | CC7.2, CC7.3, CC4.2 | LOG-03, LOG-13, SEF-06 |
| OBS-05 | Performance and drift monitoring | F | A.6.2.6, A.6.2.4, 9.1 | MEASURE 2.4, MEASURE 2.5, MEASURE 4.2, MANAGE 4.1 | LLM09, LLM04, ASI10 | AML.T0031, AML.T0062, AML.T0060, AML.M0038, AML.M0024 | Art. 15(1), Art. 72, Art. 13(3)(b) | PI1.3, PI1.4, CC4.1, A1.1 | MDS-10, MDS-11, LOG-15, AIS-03 |
| OBS-06 | Red team and adversarial testing | F | A.6.2.4, A.6.2.6 | MEASURE 2.7, MEASURE 1.3, MEASURE 2.5 | LLM01, LLM07, ASI01, ASI05 | AML.M0035, AML.M0016, AML.T0051, AML.T0054, AML.T0080, AML.T0086 | Art. 9(6), Art. 15(5), Art. 55(1)(a), Art. 17(1)(d) | CC4.1, CC4.2, CC7.1 | TVM-06, MDS-06, MDS-07, TVM-12 |
| OBS-07 | Bias and fairness testing | F | A.5.4, A.7.4, A.6.2.4 | MEASURE 2.11, MEASURE 2.2, MANAGE 1.3 | LLM09, ASI09 | AML.T0048.002, AML.T0130, AML.M0022 | Art. 10(2)(f), Art. 15(4), Art. 27 | PI1.3, PI1.4, P7.1 | GRC-11, DSP-24, MDS-03 |
| OBS-08 | Agent behavior monitoring | F | A.6.2.6, A.6.2.8, A.9.4 | MEASURE 2.4, MANAGE 4.1, MANAGE 2.4, MEASURE 3.1 | ASI10, ASI08, ASI02, LLM06 | AML.M0038, AML.M0037, AML.M0024, AML.T0124, AML.T0116, AML.T0117, AML.T0086, AML.T0101 | Art. 26(5), Art. 14(4)(e), Art. 72 | CC7.2, CC7.3, CC4.1 | LOG-15, LOG-03, LOG-13, IAM-19, MDS-10 |

## Data Protection for AI (DAT)

| Control | Name | Applies | ISO/IEC 42001 | NIST AI RMF | OWASP | MITRE ATLAS | EU AI Act | SOC 2 | CSA AICM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DAT-01 | DLP rules active | F | A.7.2, A.7.3, A.9.2 | MAP 4.1, MAP 4.2, MANAGE 2.4, MEASURE 2.10 | LLM02, ASI02 | AML.T0057, AML.T0025, AML.T0086, AML.M0019, AML.M0030 | Art. 10, Art. 26 | CC6.7, C1.1, P6.1 | UEM-11, DSP-10, DSP-17, DSP-07 |
| DAT-02 | PII detection | F | A.7.4, A.5.4, A.7.3 | MEASURE 2.10, MAP 4.1 | LLM02, LLM05 | AML.T0057, AML.T0024.000, AML.M0033 | Art. 10(5), Art. 26(9) | C1.1, P4.1, P6.1 | DSP-04, DSP-17, LOG-14, LOG-15, DSP-22 |
| DAT-03 | Data classification | F | A.7.2, A.7.4, A.7.5, A.7.6 | MAP 4.1, MEASURE 2.10, MANAGE 1.2 | LLM02, LLM08 | AML.M0005, AML.M0019, AML.T0036, AML.T0085 | Art. 10(2), Art. 26(4) | C1.1, CC3.2, P3.1 | DSP-04, DSP-03, DSP-05, DCS-05 |
| DAT-04 | Encryption in transit | F | A.6.2.5, A.10.3 | MEASURE 2.7, MEASURE 2.10 | LLM02, ASI07 | AML.M0012, AML.T0025 | Art. 15(5) | CC6.7, CC6.1 | CEK-03, CEK-04, DSP-10, I&S-03 |
| DAT-05 | Encryption at rest | F | A.6.2.5, A.4.5 | MEASURE 2.7, MEASURE 2.10 | LLM02, LLM08, ASI06 | AML.M0012, AML.M0005, AML.T0035, AML.T0037 | Art. 15(5), Art. 10(5) | CC6.1, C1.1, CC6.7 | CEK-03, CEK-08, CEK-12, DSP-17 |
| DAT-06 | Data masking | F | A.7.6, A.7.2, A.6.2.8 | MEASURE 2.10, MAP 4.1 | LLM02, LLM05 | AML.M0012, AML.T0057, AML.T0037 | Art. 10(5)(b), Art. 12 | C1.1, CC6.7, P4.1 | DSP-15, DSP-22, DSP-17, LOG-09 |
| DAT-07 | Retention policies | F | A.7.2, A.7.3, A.6.2.8 | MEASURE 2.10, GOVERN 1.7, MANAGE 3.1 | LLM02, ASI06 | AML.M0005, AML.T0035, AML.T0085 | Art. 12, Art. 19, Art. 26(6) | C1.2, P4.2, P4.3 | DSP-16, DSP-02, DSP-12 |
| DAT-08 | Training data opt-out | F | A.10.3, A.7.3, A.7.5 | MAP 4.1, GOVERN 6.1, MANAGE 3.1 | LLM02, LLM03 | AML.M0025, AML.T0024.000 | Art. 25(4), Art. 53(1), Art. 10 | C1.1, P4.1, CC9.2 | STA-10, DSP-12, DSP-15, DSP-20 |
| DAT-09 | Content provenance and watermarking | F | A.8.2, A.8.5, A.9.3 | MEASURE 2.8, MAP 5.2 | LLM09, ASI09 | AML.T0088, AML.T0052.001, AML.M0034 | Art. 50(2), Art. 50(4) | PI1.4, CC2.3 | DSP-20, AIS-09, GRC-09 |
| DAT-10 | Incident disclosure to users | F | A.8.4, A.8.3, A.8.5 | MANAGE 4.3, GOVERN 4.3 | ASI09, LLM09 | AML.T0048 | Art. 73, Art. 26(5), Art. 20 | CC7.4, CC7.5, CC2.3, P6.6 | SEF-07, DSP-18, SEF-03, SEF-08 |

## NHI & Agentic Access (NHI)

| Control | Name | Applies | ISO/IEC 42001 | NIST AI RMF | OWASP | MITRE ATLAS | EU AI Act | SOC 2 | CSA AICM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NHI-01 | Service account scoping | F | A.6.2.5, A.4.5, A.9.2 | MEASURE 2.7, MAP 2.1, MANAGE 1.3 | LLM06, ASI03 | AML.T0012, AML.T0091, AML.M0026, AML.M0028, AML.M0019 | Art. 15(5) | CC6.1, CC6.2, CC6.3 | IAM-05, IAM-16, IAM-19, IAM-03 |
| NHI-02 | Secrets management | F | A.6.2.5, A.4.5 | MEASURE 2.7 | LLM02, LLM07, ASI03 | AML.T0055, AML.T0083, AML.T0082, AML.T0098, AML.M0012, AML.M0005 | Art. 15(5) | CC6.1, CC6.2, CC6.7 | IAM-15, CEK-21, AIS-12 |
| NHI-03 | Credential rotation | F | A.6.2.6, A.6.2.5 | MEASURE 2.7 | ASI03 | AML.T0012, AML.T0055, AML.T0091 | Art. 15(5) | CC6.1, CC6.2, CC6.3 | CEK-12, IAM-15, IAM-07 |
| NHI-04 | Short-lived tokens | F | A.6.2.5 | MEASURE 2.7 | ASI03, LLM06 | AML.T0091.000, AML.T0113, AML.T0012, AML.M0026 | Art. 15(5) | CC6.1, CC6.2 | IAM-14, IAM-16, IAM-10 |
| NHI-05 | Agent authentication | F | A.6.2.5, A.4.5 | MEASURE 2.7, MANAGE 1.3 | ASI03, ASI07, ASI10 | AML.T0073, AML.T0074, AML.T0118, AML.M0032, AML.M0026 | Art. 15(5) | CC6.1, CC6.6, CC6.7 | IAM-13, IAM-14, IAM-19, IAM-03 |
| NHI-06 | Intent validation | F | A.9.2, A.9.4, A.6.2.6 | MAP 3.5, MANAGE 2.4, MEASURE 2.6 | ASI01, ASI02, LLM06 | AML.T0053, AML.T0051, AML.M0030, AML.M0037, AML.M0038 | Art. 14(4) | CC5.2, CC6.1, PI1.2 | IAM-19, AIS-11, IAM-16, GRC-15 |
| NHI-07 | Tool and function authorization | F | A.6.2.5, A.6.2.8, A.9.4 | MEASURE 2.7, MANAGE 2.4, MAP 3.5 | ASI02, LLM06, ASI03 | AML.T0053, AML.T0086, AML.T0101, AML.M0028, AML.M0030, AML.M0024 | Art. 15(5), Art. 12, Art. 14(4)(d) | CC6.1, CC6.3, CC7.2 | IAM-19, IAM-16, AIS-10, LOG-11, AIS-11 |
| NHI-08 | Sub-agent spawn limits | F | A.6.2.5, A.6.2.6, A.9.4 | MANAGE 2.4, MEASURE 2.7, MANAGE 2.2 | ASI10, ASI08, LLM06, LLM10 | AML.T0103, AML.T0108, AML.T0124, AML.T0034.002, AML.M0037, AML.M0036 | Art. 14, Art. 15(1), Art. 12 | CC6.1, A1.1, CC7.2 | AIS-11, IAM-19, I&S-02, IAM-03 |
| NHI-09 | Autonomous action limits | F | A.9.2, A.9.3, A.6.2.6 | GOVERN 3.2, MAP 3.5, MANAGE 2.4, MANAGE 1.3 | ASI02, ASI10, LLM06, ASI09 | AML.M0029, AML.M0037, AML.T0101, AML.T0086, AML.T0048 | Art. 14(1), Art. 26(2) | CC5.2, CC6.1, PI1.3 | GRC-15, IAM-18, AIS-11, CCC-04 |
| NHI-10 | Agentic boundary controls | F | A.6.2.3, A.6.2.5, A.10.2 | MEASURE 2.7, MAP 3.3, MANAGE 2.4 | ASI07, ASI08, ASI10, LLM06 | AML.T0118, AML.T0080, AML.M0032, AML.M0033 | Art. 15(5), Art. 14(4) | CC6.1, CC6.6, CC6.7 | AIS-11, I&S-06, IAM-19, AIS-10 |
| NHI-11 | Shell and filesystem sandbox | F | A.6.2.5, A.4.5 | MEASURE 2.7, MANAGE 2.4 | ASI05, ASI02, LLM05 | AML.T0050, AML.T0105, AML.T0097, AML.T0112, AML.M0011, AML.M0032 | Art. 15(5) | CC6.1, CC6.6, CC6.8, CC7.1 | AIS-13, I&S-04, I&S-06, TVM-02 |
| NHI-12 | Agent memory protection | F | A.7.4, A.7.6, A.6.2.6 | MEASURE 2.7, MEASURE 2.10, MANAGE 2.4 | ASI06, LLM08, LLM02 | AML.T0080, AML.T0092, AML.T0094, AML.M0031, AML.M0027 | Art. 15(5), Art. 12 | CC6.1, C1.1, PI1.2 | AIS-14, DSP-21, DSP-17, IAM-17 |

## AI Supply Chain (SUP)

| Control | Name | Applies | ISO/IEC 42001 | NIST AI RMF | OWASP | MITRE ATLAS | EU AI Act | SOC 2 | CSA AICM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SUP-01 | Model provenance | F | A.6.2.7, A.4.2, A.10.3 | GOVERN 6.1, MAP 4.1, MANAGE 3.2 | LLM03, LLM04, ASI04 | AML.T0010.003, AML.T0115.001, AML.T0111, AML.M0023, AML.M0014 | Art. 11, Art. 13, Art. 53(1)(a), Art. 25 | CC9.2, CC8.1, CC6.8 | MDS-03, MDS-09, DSP-20, STA-16 |
| SUP-02 | Model version pinning | F | A.6.2.5, A.6.2.6, 8.1 | MANAGE 3.2, MANAGE 4.1, GOVERN 1.5 | LLM03, LLM04, ASI04 | AML.T0109, AML.T0010.003, AML.T0076, AML.M0014, AML.M0017 | Art. 3(23), Art. 43(4), Art. 25(1)(c), Art. 17 | CC8.1, CC7.1, CC6.8 | CCC-06, CCC-01, CCC-04, MDS-03 |
| SUP-03 | Model rollback procedure | F | A.6.2.6, A.8.4, 10.2 | MANAGE 2.4, MANAGE 4.1, MANAGE 2.3 | LLM03, LLM04, ASI08 | AML.T0031, AML.T0076, AML.T0109 | Art. 15(4), Art. 20 | A1.2, A1.3, CC8.1, CC7.5 | CCC-09, MDS-11, BCR-08, BCR-04 |
| SUP-04 | Training data lineage | F | A.7.5, A.7.3, A.7.2, A.7.4 | MAP 4.1, MEASURE 2.1, MANAGE 3.2 | LLM04, LLM03 | AML.T0020, AML.T0010.002, AML.T0059, AML.M0025, AML.M0007 | Art. 10(2), Art. 11, Art. 53(1)(c) | CC9.2, C1.1, P3.1 | DSP-20, DSP-05, MDS-01, MDS-04 |
| SUP-05 | Training data opt-in | F | A.7.3, A.5.4, A.8.5 | MAP 4.1, MEASURE 2.10 | LLM02, LLM04 | AML.M0025, AML.T0024.000 | Art. 10(5) | P2.1, P3.1, P4.1 | DSP-12, DSP-08, DSP-11, DSP-20 |
| SUP-06 | ML pipeline security | F | A.6.1.3, A.6.2.3, A.6.2.5, A.4.4 | MEASURE 2.7, MANAGE 3.2, GOVERN 1.4 | LLM03, LLM04, ASI04, ASI05 | AML.T0010.001, AML.T0010.004, AML.T0119, AML.T0018, AML.M0013, AML.M0014, AML.M0016 | Art. 15(5), Art. 17, Art. 9 | CC8.1, CC6.1, CC6.8, CC7.1 | MDS-01, AIS-04, AIS-06, AIS-12, CCC-03 |
| SUP-07 | Model integrity verification | F | A.6.2.4, A.6.2.5, A.10.3 | MANAGE 3.2, MEASURE 2.7, MAP 4.2 | LLM03, LLM04, ASI04 | AML.T0010.003, AML.T0018.002, AML.T0011.000, AML.T0115.001, AML.M0014, AML.M0013, AML.M0008 | Art. 15(5), Art. 11, Art. 43 | CC6.8, CC8.1, CC7.1 | MDS-08, MDS-09, MDS-13, MDS-02, DSP-23 |
| SUP-08 | Third-party model assessment | F | A.10.3, A.10.2, A.6.2.4, A.5.2 | GOVERN 6.1, MAP 4.1, MAP 4.2, MANAGE 3.1, MANAGE 3.2 | LLM03, LLM04, ASI04 | AML.T0010.003, AML.T0111, AML.T0115.001, AML.M0008, AML.M0014, AML.M0023 | Art. 25, Art. 53, Art. 55, Art. 26(1) | CC9.2, CC3.2, CC3.4 | MDS-12, STA-09, STA-15, MDS-05, GRC-11 |
| SUP-09 | Plugin, extension and MCP validation | F | A.4.4, A.10.3, A.6.2.4 | GOVERN 6.1, MAP 4.2, MANAGE 3.1, MEASURE 2.7 | ASI04, LLM03, ASI02 | AML.T0010.005, AML.T0110, AML.T0011.002, AML.T0115.002, AML.T0099, AML.M0014, AML.M0013, AML.M0028, AML.M0023 | Art. 25, Art. 15(5), Art. 26(1) | CC6.8, CC9.2, CC8.1 | STA-16, STA-08, AIS-05, TVM-05, UEM-02 |
| SUP-10 | Vector store security | F | A.7.4, A.7.5, A.6.2.5, A.6.2.6 | MEASURE 2.7, MEASURE 2.10, MAP 4.2 | LLM08, LLM04, LLM02, ASI06 | AML.T0070, AML.T0071, AML.T0064, AML.T0066, AML.T0082, AML.T0085.000, AML.M0005, AML.M0019, AML.M0033 | Art. 10, Art. 15(5), Art. 12 | CC6.1, CC6.3, PI1.2, C1.1 | DSP-21, IAM-17, DSP-17, DSP-23, IAM-05 |
| SUP-11 | System prompt protection | F | A.6.2.3, A.6.2.5 | MEASURE 2.7 | LLM07, LLM01, ASI01 | AML.T0056, AML.T0069, AML.T0084, AML.T0083, AML.M0020, AML.M0000 | Art. 15(5), Art. 11 | CC6.1, C1.1, CC6.7 | AIS-15, IAM-15, AIS-02, TVM-11 |
| SUP-12 | Embedding integrity | F | A.7.4, A.7.6, A.6.2.4 | MEASURE 2.7, MEASURE 2.5, MANAGE 3.2 | LLM08, LLM04, ASI06 | AML.T0070, AML.T0010.002, AML.T0059, AML.T0099, AML.M0014, AML.M0025, AML.M0007 | Art. 10, Art. 15(5), Art. 12 | PI1.2, PI1.3, CC6.1, CC8.1 | DSP-23, DSP-21, MDS-01, CCC-07 |
| SUP-13 | Agent action attestation | F | A.6.2.8, A.6.2.6, A.8.4 | MEASURE 2.8, MANAGE 4.1 | ASI10, ASI03, ASI07, LLM06 | AML.M0024, AML.M0029, AML.M0013, AML.T0074, AML.T0101, AML.T0053 | Art. 12, Art. 14, Art. 19 | CC7.2, CC4.1, CC6.1 | LOG-11, IAM-12, LOG-02, IAM-19 |

## ISO/IEC 42001 references and the controls that support them

For a certification gap review. A reference with controls here is supported by Level 2 records; one missing from this list needs its own evidence (see [what Level 2 evidences](what-level-2-evidences.md)).

| Reference | Controls |
| --- | --- |
| 4.2 Understanding the needs and expectations of interested parties | POS-07 |
| 5.3 Roles, responsibilities and authorities | POS-03, POS-05 |
| 6.1.2 AI risk assessment | POS-02 |
| 6.1.4 AI system impact assessment | POS-02 |
| 7.5 Documented information | OBS-02 |
| 8.1 Operational planning and control | SUP-02 |
| 8.4 AI system impact assessment | POS-02 |
| 9.1 Monitoring, measurement, analysis and evaluation | SHA-04, OBS-05 |
| 10.2 Nonconformity and corrective action | RUN-09, SUP-03 |
| A.2.2 AI policy | POS-04, POS-07, SHA-02, SHA-05 |
| A.2.3 Alignment with other organizational policies | POS-04 |
| A.3.2 AI roles and responsibilities | POS-03, POS-05 |
| A.4.2 Resource documentation | POS-01, SHA-01, SUP-01 |
| A.4.4 Tooling resources | SUP-06, SUP-09 |
| A.4.5 System and computing resources | RUN-03, RUN-04, RUN-07, RUN-08, DAT-05, NHI-01, NHI-02, NHI-05, NHI-11 |
| A.5.2 AI system impact assessment process | POS-02, SUP-08 |
| A.5.4 Assessing AI system impact on individuals or groups of individuals | RUN-05, OBS-07, DAT-02, SUP-05 |
| A.5.5 Assessing societal impacts of AI systems | RUN-05 |
| A.6.1.3 Processes for responsible AI system design and development | SUP-06 |
| A.6.2.3 Documentation of AI system design and development | NHI-10, SUP-06, SUP-11 |
| A.6.2.4 AI system verification and validation | RUN-01, RUN-06, OBS-05, OBS-06, OBS-07, SUP-07, SUP-08, SUP-09, SUP-12 |
| A.6.2.5 AI system deployment | POS-03, RUN-07, RUN-08, DAT-04, DAT-05, NHI-01, NHI-02, NHI-03, NHI-04, NHI-05, NHI-07, NHI-08, NHI-10, NHI-11, SUP-02, SUP-06, SUP-07, SUP-10, SUP-11 |
| A.6.2.6 AI system operation and monitoring | RUN-01, RUN-02, RUN-03, RUN-04, RUN-09, SHA-01, SHA-03, SHA-04, OBS-03, OBS-04, OBS-05, OBS-06, OBS-08, NHI-03, NHI-06, NHI-08, NHI-09, NHI-12, SUP-02, SUP-03, SUP-10, SUP-13 |
| A.6.2.7 AI system technical documentation | POS-01, OBS-01, SUP-01 |
| A.6.2.8 AI system recording of event logs | SHA-03, OBS-01, OBS-02, OBS-08, DAT-06, DAT-07, NHI-07, SUP-13 |
| A.7.2 Data for development and enhancement of AI system | DAT-01, DAT-03, DAT-06, DAT-07, SUP-04 |
| A.7.3 Acquisition of data | POS-08, DAT-01, DAT-02, DAT-07, DAT-08, SUP-04, SUP-05 |
| A.7.4 Quality of data for AI systems | RUN-06, OBS-07, DAT-02, DAT-03, NHI-12, SUP-04, SUP-10, SUP-12 |
| A.7.5 Data provenance | POS-08, DAT-03, DAT-08, SUP-04, SUP-10 |
| A.7.6 Data preparation | DAT-03, DAT-06, NHI-12, SUP-12 |
| A.8.2 System documentation and information for users | RUN-02, DAT-09 |
| A.8.3 External reporting | POS-07, DAT-10 |
| A.8.4 Communication of incidents | RUN-09, OBS-03, OBS-04, DAT-10, SUP-03, SUP-13 |
| A.8.5 Information for interested parties | DAT-09, DAT-10, SUP-05 |
| A.9.2 Processes for responsible use of AI systems | POS-04, SHA-02, SHA-05, DAT-01, NHI-01, NHI-06, NHI-09 |
| A.9.3 Objectives for responsible use of AI system | RUN-02, RUN-05, DAT-09, NHI-09 |
| A.9.4 Intended use of the AI system | POS-01, OBS-08, NHI-06, NHI-07, NHI-08 |
| A.10.2 Allocating responsibilities | POS-06, NHI-10, SUP-08 |
| A.10.3 Suppliers | POS-06, POS-08, DAT-04, DAT-08, SUP-01, SUP-07, SUP-08, SUP-09 |

## SOC 2 criteria and the controls that support them

For security questionnaires and SOC 2 audits. The assessment records that list these controls hold the evidence.

| Criterion | Controls |
| --- | --- |
| A1.1 | RUN-03, RUN-04, SHA-04, OBS-05, NHI-08 |
| A1.2 | RUN-04, RUN-09, SUP-03 |
| A1.3 | RUN-09, SUP-03 |
| C1.1 | POS-08, RUN-02, RUN-08, SHA-05, DAT-01, DAT-02, DAT-03, DAT-05, DAT-06, DAT-08, NHI-12, SUP-04, SUP-10, SUP-11 |
| C1.2 | DAT-07 |
| CC1.1 | POS-04, POS-07 |
| CC1.3 | POS-05 |
| CC1.4 | POS-04 |
| CC2.1 | POS-01 |
| CC2.2 | POS-04, POS-05 |
| CC2.3 | POS-07, DAT-09, DAT-10 |
| CC3.1 | POS-02, POS-07 |
| CC3.2 | POS-01, POS-02, POS-06, DAT-03, SUP-08 |
| CC3.4 | POS-02, SUP-08 |
| CC4.1 | SHA-03, SHA-04, OBS-01, OBS-02, OBS-05, OBS-06, OBS-08, SUP-13 |
| CC4.2 | OBS-04, OBS-06 |
| CC5.1 | POS-03 |
| CC5.2 | RUN-05, NHI-06, NHI-09 |
| CC5.3 | POS-03, SHA-02 |
| CC6.1 | POS-01, RUN-03, RUN-07, RUN-08, SHA-01, SHA-02, SHA-03, DAT-04, DAT-05, NHI-01, NHI-02, NHI-03, NHI-04, NHI-05, NHI-06, NHI-07, NHI-08, NHI-09, NHI-10, NHI-11, NHI-12, SUP-06, SUP-10, SUP-11, SUP-12, SUP-13 |
| CC6.2 | NHI-01, NHI-02, NHI-03, NHI-04 |
| CC6.3 | RUN-08, NHI-01, NHI-03, NHI-07, SUP-10 |
| CC6.6 | RUN-01, RUN-06, RUN-07, SHA-05, NHI-05, NHI-10, NHI-11 |
| CC6.7 | POS-08, RUN-02, RUN-07, SHA-05, DAT-01, DAT-04, DAT-05, DAT-06, NHI-02, NHI-05, NHI-10, SUP-11 |
| CC6.8 | RUN-01, SHA-02, NHI-11, SUP-01, SUP-02, SUP-06, SUP-07, SUP-09 |
| CC7.1 | SHA-01, OBS-06, NHI-11, SUP-02, SUP-06, SUP-07 |
| CC7.2 | RUN-03, RUN-04, SHA-01, SHA-03, SHA-04, OBS-01, OBS-02, OBS-03, OBS-04, OBS-08, NHI-07, NHI-08, SUP-13 |
| CC7.3 | OBS-01, OBS-02, OBS-03, OBS-04, OBS-08 |
| CC7.4 | OBS-03, DAT-10 |
| CC7.5 | RUN-09, DAT-10, SUP-03 |
| CC8.1 | POS-03, SUP-01, SUP-02, SUP-03, SUP-06, SUP-07, SUP-09, SUP-12 |
| CC9.1 | RUN-09 |
| CC9.2 | POS-06, DAT-08, SUP-01, SUP-04, SUP-08, SUP-09 |
| P2.1 | SUP-05 |
| P3.1 | DAT-03, SUP-04, SUP-05 |
| P4.1 | POS-08, DAT-02, DAT-06, DAT-08, SUP-05 |
| P4.2 | DAT-07 |
| P4.3 | DAT-07 |
| P6.1 | DAT-01, DAT-02 |
| P6.6 | DAT-10 |
| P7.1 | OBS-07 |
| PI1.1 | RUN-05 |
| PI1.2 | RUN-01, RUN-06, NHI-06, NHI-12, SUP-10, SUP-12 |
| PI1.3 | RUN-02, OBS-05, OBS-07, NHI-09, SUP-12 |
| PI1.4 | RUN-02, OBS-05, OBS-07, DAT-09 |
