# SWS405 Digital Forensics – Assignment 2: MemLabs

Memory forensics on the [MemLabs](https://github.com/stuxnet999/MemLabs) challenge images (Labs 1–5) using Volatility 2.
Each lab is a Windows 7 RAM dump. The goal was to reconstruct what the user was doing and recover the hidden flags.

**Royal University of Bhutan · College of Science and Technology · Autumn Semester 2026**
Module tutor: Pema Thinley

📄 **The full write-up is in [REPORT.md](REPORT.md)**. It has the investigation log, a labelled screenshot for every flag, and the forensic reasoning for each lab.

## Results

| Lab | Theme | Flags | Key techniques |
|---|---|---|---|
| 1 – Beginner's Luck | Crashed PC: terminal, Paint, WinRAR | 3 | `consoles`, `hashdump`, `memdump` + raw pixel rendering |
| 2 – A New World | Browser + password manager | 3 | `envars`, KeePass database from `dumpfiles`, `chromehistory` |
| 3 – The Evil's Den | Malicious encoding script | 1 (2 halves) | `cmdline`, reversing XOR + Base64, `steghide` |
| 4 – Obsession | Deleted Desktop file | 1 | `mftparser`: resident `$DATA` in the MFT |
| 5 – Black Tuesday | Encrypted archive | 2 | `iehistory`, Base64 filename as RAR password |

All 10 flags are listed in [REPORT.md § 2](REPORT.md#2-summary-of-flags). Lab 6 (optional bonus) was not attempted.

## Repository layout

```
.
├── README.md
├── REPORT.md                 ← the assignment report
├── screenshots/Lab1..Lab5/   ← labelled evidence screenshots (Figure L.N)
└── memlabs/
    ├── out/                  ← full, unfiltered output of every Volatility plugin run
    ├── Lab1..Lab5/dump/      ← artefacts recovered from memory (archives, images, scripts, KeePass DB…)
    ├── Lab2/mega/            ← Important.zip fetched from the link found in Chrome history
    ├── scripts/              ← helper scripts (see below)
    └── docker/               ← Dockerfiles for the Volatility 2 / tools environment
```

The memory images themselves (about 1 GB each) and the 254 MB mspaint process dump are not committed (see `.gitignore`).
Download the images from the MemLabs repo to reproduce.

## Scripts

| Script | Purpose |
|---|---|
| `reverse_evilscript.py` | Lab 3: undoes `evilscript.py` (Base64-decode, then XOR each byte with 3) |
| `raw2png.py` | Lab 1: renders raw process-memory bytes as an image (`dump offset width height out.png`) |
| `find_canvas.py`, `find_strokes.py`, `find_gray.py`, `nonwhite.py`, `width.py`, `overview.py` | Lab 1: locating the Paint canvas inside `2424.dmp` and finding its row width |
| `build_report.py`, `build_report_md.py` | Generate the report (Word / Markdown) from one source |

## Environment

- Kali Linux, zsh
- Volatility 2.6.1 on Python 2.7 (Docker image `python:2.7`, since Kali no longer packages Volatility 2 or Python 2)
- [superponible/volatility-plugins](https://github.com/superponible/volatility-plugins) for `chromehistory`
- steghide, unrar, 7-Zip, KeePassXC

Example:

```bash
volatility -f MemoryDump_Lab1.raw --profile=Win7SP1x64 consoles
volatility --plugins=$HOME/volatility-plugins -f MemoryDump_Lab2.raw --profile=Win7SP1x64 chromehistory
```

| Lab | Profile |
|---|---|
| 1, 2, 4, 5 | `Win7SP1x64` |
| 3 | `Win7SP1x86_23418` |
