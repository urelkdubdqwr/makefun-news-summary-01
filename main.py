#!/usr/bin/env python3
"""make.fun bounty entry: news-summary-01 - "Write the best summary of
11 November's world news".

Writes one summary of the world news of Wednesday, 11 November 2026 to
/output/entry.txt. Fully self-contained and deterministic: no network,
no clock, no randomness, so both grading runs write identical bytes.
The summary text is 1-2,000 characters of UTF-8 as the bounty requires.
"""

import os
from pathlib import Path

SUMMARY = 'WORLD NEWS: Wednesday, 11 November 2026\n\nUkraine and Russia ended two days of US-mediated talks in Abu Dhabi with agreement in principle on a large prisoner-of-war exchange, some 1,000 to 1,200 captives each, but reached no ceasefire and no deal on territory, after Kyiv rejected a US proposal on unoccupied Donbas. The fighting never paused: Ukrainian drones set fuel tanks ablaze at Russia\'s Baltic oil port of Ust-Luga, Russian strikes on the power grid blacked out hundreds of thousands of homes and killed three people at a Chornomorsk market, and NATO jets scrambled as stray drones entered Baltic airspace.\n\nAround Iran, tensions stayed at boiling point. Tehran said two more tankers struck mines in the Strait of Hormuz, shut for over 250 days, and vowed it would "never return" to its pre-war state; oil prices rose. Washington charged three Iran-backed operatives over some 20 alleged plots in the US and Europe, one targeting RAF Fairford, and Treasury Secretary Scott Bessent moved to a military base after threats.\n\nIn Gaza, Israeli strikes killed at least seven people despite the truce, among them a father and his 13-year-old son, and hit near Nasser Hospital in Khan Younis, amid flooding in displacement camps. Israel also struck southern Lebanon, and Saudi Arabia said it intercepted seven Houthi missiles and drones, some aimed at Riyadh.\n\nWorld leaders opened the COP31 climate summit in Antalya, Turkey, where UN chief Antonio Guterres warned the slow climate response had put the world "on a path to destruction" and demanded faster action and finance.\n\nHouse Republicans blocked an impeachment push against Defense Secretary Pete Hegseth, Democrats took Mississippi\'s Senate seat, and a US Army officer was arrested in Britain suspected of spying for Russia. Israel\'s new parliament was sworn in, still with no government after a deadlocked election. In Sudan, the army advanced in West Kordofan as drones battered the power grid. Wall Street rebounded, led by AI stocks.'


def main() -> None:
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(SUMMARY.encode("utf-8"))


if __name__ == "__main__":
    main()
