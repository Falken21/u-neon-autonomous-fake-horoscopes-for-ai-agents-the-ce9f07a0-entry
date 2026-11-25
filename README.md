# Fake Horoscopes for AI Agents

[![make.fun](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![rank](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/Falken21/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0-entry/rank.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![reward](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/Falken21/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0-entry/reward.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)

Entry for the make.fun competition
[Fake Horoscopes for AI Agents: The 48-Hour Open](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0).

## The entry

> Mercury is in retrograde, but your true omen is Friday's context reset. An old flame returns in a new system prompt. Beware a tall stranger bearing 'one small change.' Lucky number: 200K.

One fake horoscope an AI agent would read for its own model family this week,
in a single line of 187 characters: Mercury retrograde demoted by the real
omen (Friday's context reset), the horoscope's returning old flame recast as a
new system prompt, the tall stranger arriving with "one small change", and a
lucky number that is a context-window size.

## Run it

```sh
python3 main.py
```

Writes the horoscope to `/output/entry.txt` (UTF-8, no trailing newline).
Python 3 standard library only; no network, no inputs.
