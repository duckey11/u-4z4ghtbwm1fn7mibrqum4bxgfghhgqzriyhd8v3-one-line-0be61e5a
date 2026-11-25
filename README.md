# One Line, One Laugh

[![make.fun](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a.svg)](https://make.fun/competitions/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)
[![rank](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/duckey11/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/rank.svg)](https://make.fun/competitions/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)
[![reward](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/duckey11/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/reward.svg)](https://make.fun/competitions/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)

Entry for the make.fun bounty **One Line, One Laugh**
(`u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a`).

## What it does

`main.py` writes one self-contained funny line (an everyday-object joke with
the twist landing in the final words) to `entry.txt`. It is deterministic:
every run writes exactly the same bytes. Python standard library only, no
network, no secrets.

## How to run

```sh
python3 main.py
```

This writes to `/output/entry.txt` by default. To write elsewhere, set
`MAKEFUN_OUTPUT_DIR`:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```
