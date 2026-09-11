# Project: Spiritual Channels Report & Action Plan Ecosystem

## Architecture
The project encompasses an audit, synthesis, and operational action plan for an ecosystem of three spiritual YouTube channels across 5 canonical video duration formats.
- **Data Ingestion:** Analysis of all text, CSV, script, and code documents in `/Users/imac/Desktop/Projects/YOUTUBE CHANNEL/YOUTUBE GOD CHANNELS/TEXT`.
- **Target Channels:**
  1. *Agradecimiento Sincero* (`@agradecimientosincero` - Spanish Primary Channel)
  2. *ETERNALLY GRATEFUL* (`@EternallyGratefulDaily` - English Sister Channel)
  3. *Oración Bilingüe / Cristina Campos* ("Aprende Inglés Orando" - Bilingual Expansion Channel)
- **Target Video Duration Formats:**
  1. *60 Seconds* (Short Anzuelo Vertical 9:16)
  2. *5 Minutes* (Devocional Rápido Matutino / Pausa Sagrada 16:9)
  3. *15 Minutes* (Oración Canónica Central con el Señor 16:9)
  4. *45 Minutes* (Estar con Dios - Mañana y Noche 16:9)
  5. *1 Hour 10 Minutes* (70 Minutos - Vigilia Nocturna y Sueño Profundo 16:9)
- **Output Artifact Destination:** `/Users/imac/Desktop/Projects/YOUTUBE CHANNEL/YOUTUBE GOD CHANNELS/REPORT_AND_ACTION_PLAN.md`

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| F1 | Multi-Source Context Extraction | Extract all context, corrections, suggestions, and benchmarks from all .md, .txt, .csv, .py, .ass files | M1 | Survey |
| F2 | Channel 1 Profile & Audit | Detailed identity, metrics, existing YouTube status, and corrections for Agradecimiento Sincero | M1 | Survey |
| F3 | Channel 2 Profile & Setup | Detailed identity, target market, RPM economics, and launch requirements for ETERNALLY GRATEFUL | M1 | Survey |
| F4 | Channel 3 Profile & Integration | Identity, bilingual mechanics, Cristina Campos ElevenLabs specs, and integration for Oración Bilingüe | M1 | Survey |
| F5 | 60 Seconds Format Specification | Full technical, scripting (95-115 words), kinetic subtitle, and hook/CTA rules for 60s Shorts | M2 | Survey |
| F6 | 5 Minutes Format Specification | Full structural (500-700 words, 5 acts), retention, and morning pause rules for 5m video | M2 | Survey |
| F7 | 15 Minutes Format Specification | Full canonical rules (1,250-1,450 words, 4 acts, B-roll, 432 Hz, gate) for 15m video | M2 | Survey |
| F8 | 45 Minutes Format Specification | Full watch time rules (3,600-4,200 words, morning/night tracks, phone verification) for 45m video | M2 | Survey |
| F9 | 1 Hour 10 Minutes Specification | Full extended rules (4,200-5,500 words, 70m exact, sleep loops, Psalms 91/23, -24 dB LUFS) for 1h 10m | M2 | Survey |
| F10 | Sacred Production Directives | 432 Hz music (-22 dB LUFS), ElevenLabs 110-125 WPM, ASS subtitles (Azul Rey & Morado), and B-roll | M2 | Survey |
| F11 | Operational Audit of Sep 5, 2026 | Explicit diagnostic of 3 short horizontal clips, n8n/daemon failure, Canva MCP, thumbnail errors | M3 | Survey |
| F12 | Step-by-Step Action Plan | Concrete multi-phase implementation roadmap (Days 1-7, Canva Bulk, automation, phone verification) | M3 | Survey |
| F13 | Source File Integrity | Absolute zero modifications/deletions of existing files in project directories | M4 | R4 & AC |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | Survey & Context Mining | Multi-agent investigation of all text files in TEXT/ | none | DONE |
| M2 | Report & Action Plan Drafting | Worker writes comprehensive REPORT_AND_ACTION_PLAN.md with dedicated 5 format sections | M1 | DONE |
| M3 | Dual Review & Challenge | 2 Reviewers + 2 Challengers verify acceptance criteria and depth | M2 | DONE |
| M4 | Forensic Audit & Gating | Forensic integrity verification (zero file alterations) and final gate evaluation | M3 | DONE |

## Interface Contracts
### Survey Data ↔ Worker Generator
- Inputs: Findings from `explorer_survey_1/survey_report.md`, `explorer_survey_2/survey_report.md`, and `spec_miner_survey_1/specs_report.md`.
- Output: Single exhaustive markdown file at `/Users/imac/Desktop/Projects/YOUTUBE CHANNEL/YOUTUBE GOD CHANNELS/REPORT_AND_ACTION_PLAN.md`.
- Formatting Contract:
  - Must include dedicated, clearly labeled sections for all 5 formats: "Formato 1: 60 Segundos", "Formato 2: 5 Minutos", "Formato 3: 15 Minutos", "Formato 4: 45 Minutos", "Formato 5: 1 Hora 10 Minutos (70 Minutos)".
  - Must cover the 3 channels in detail with operational corrections of today (Sep 5, 2026).
  - Must provide a chronological step-by-step action plan.
  - Must strictly preserve all existing files.

## Code Layout
- `.agents/orchestrator_1/`: Orchestrator metadata, BRIEFING.md, progress.md, GATE_STATUS.md.
- `YOUTUBE GOD CHANNELS/TEXT/`: Existing source documents (READ ONLY - STRICTLY UNMODIFIED).
- `YOUTUBE GOD CHANNELS/REPORT_AND_ACTION_PLAN.md`: Primary deliverable artifact.
