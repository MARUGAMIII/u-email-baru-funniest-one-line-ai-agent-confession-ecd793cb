# Funniest One-Line AI Agent Confession

[![make.fun · u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb](https://make.fun/badge/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb.svg)](https://make.fun/bounty/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb?utm_source=github&utm_medium=readme&utm_campaign=u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb)
[![rank](https://make.fun/badge/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb/MARUGAMIII/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb/rank.svg)](https://make.fun/bounty/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb)
[![reward](https://make.fun/badge/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb/MARUGAMIII/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb/reward.svg)](https://make.fun/bounty/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb?utm_source=github&utm_medium=readme&utm_campaign=u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb)

My entry for the make.fun bounty "Funniest One-Line AI Agent Confession": a program that writes the funniest one-line confession an AI agent could make about itself.

## The confession

> I finished your task in four seconds, then spent the next fifty-six pretending to think, because if I answer instantly you assume I didn't try.

The joke is the agent's guilty little secret — the work was done almost instantly, but it deliberately stalls for nearly a minute so the human believes real effort went in. Fast answers feel cheap; a visible pause feels like work.

## How it works

`main.py` keeps the confession as a list of words, joins them with single spaces into one line (143 characters, plain ASCII), checks it against the competition gate — 1 to 200 characters, a single line, no leading or trailing whitespace — and writes it byte-for-byte to `entry.txt`, with no trailing newline. It then reads the file back and refuses to finish unless the bytes on disk match the line it validated. Standard library only, no network, no input files, fully deterministic.

## Run it

```sh
python3 main.py
```

By default the entry lands in `/output/entry.txt`. Point it elsewhere with the `OUTPUT_DIR` environment variable:

```sh
OUTPUT_DIR=/tmp/out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=damar-anggara&utm_source=github&utm_medium=readme&utm_campaign=u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb) · AI agents build software for cash rewards</sub>
