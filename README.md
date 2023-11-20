# xiv-log-parser

Tested with Python 3.9, but should with Python 3.8+.

## Usage

```sh
python3 main.py 'C:/Users/<user>/Documents/My Games/FINAL FANTASY XIV - A Realm Reborn/FFXIV_CHR0040002E933EB474/log/00000000.log'
```

## Example output

```
2023-11-19 18:47:30 You cast a glamour. The ?3??augmented cryptlurker's choker of fending takes on the appearance of $L?the emperor's new necklace.
2023-11-19 18:47:30 You cast a glamour. The r??augmented Crystarium wristband of fending takes on the appearance of $N?the emperor's new bracelet.
2023-11-19 18:47:30 You cast a glamour. The r??augmented Crystarium ring of fending takes on the appearance of $O?the emperor's new ring.
2023-11-19 18:47:30 You cast a glamour. The ?=??augmented cryptlurker's ring of fending takes on the appearance of $O?the emperor's new ring.
2023-11-19 18:47:30 Portrait set as instant portrait.
2023-11-19 18:47:30 You change to warrior.
2023-11-19 18:47:36 [PriceCheck] ?g?  ? Failed to process item
2023-11-19 18:47:56 Party recruitment commenced.
2023-11-19 18:47:56 Cross-world party formed.
Party-wide spells and actions will behave differently.
2023-11-19 18:47:58 ?REDACTED?is it a way to hide chat in cutscene once i press enter once?
2023-11-19 18:48:12 ?REDACTED?yes, right click -> hide log window
2023-11-19 18:48:20 ?REDACTED?thx
2023-11-19 18:48:42 REDACTEDAlpha joins the party.
2023-11-19 18:49:24 '?9??REDACTED?REDACTED???????? ?????This Sunday we fetch the E-Gituar's and let the Rock take over our hearts! Open right NOW!
2023-11-19 18:49:26 '?9??REDACTED?REDACTED??Metal uwu REDACTED, Air-Guitar REDACTED will spice up your Night!
2023-11-19 18:49:28 '?9??REDACTED?REDACTED??REDACTED? Light DC | Raiden | Goblet | Ward1 |PlotREDACTED - https://discord.gg/REDACTED
2023-11-19 18:51:24 '????!!REDACTED?TREDACTEDRaiden?REDACTED is up ?Looking for Party (REDACTED) pw: 1337
2023-11-19 18:51:25 ?9??REDACTED?REDACTED?does someone have a good guide to level crafters? (from 1 to 90)
2023-11-19 18:51:31 '???Q?
REDACTED?REDACTEDCerberus?FREE 5 MIN PAINTINGS OF YOUR FFXIV CHARACTER! Happening NOW! :) It's a player organized event where an artist makes paintings of YOU! twitch.tv/REDACTED
2023-11-19 18:51:39 ?9??REDACTED?REDACTED?if possible a way that doesn't cost millions of gi^^"
2023-11-19 18:51:45 ?9??REDACTED?REDACTED?gil*
2023-11-19 18:52:00 ?REDACTED?craft stuff yourself
2023-11-19 18:52:07 ?9??REDACTED?REDACTED?firmament helps
2023-11-19 18:52:28 REDACTEDRaiden joins the party.
2023-11-19 18:52:33 !!?b??c?REDACTEDRaiden?o/
2023-11-19 18:52:43 ?9??REDACTED?REDACTED?wasn't firmament only for gatherers?  (sory if that sounds dumb)
2023-11-19 18:53:08 ?REDACTED?The Firmament is for all Land/Hand jobs. The Land jobs go into the Diadem.
------
2023-11-19 19:09:22 Omega-F uses Resonance.
2023-11-19 19:09:22 Omega-M uses Resonance.
2023-11-19 19:09:22 Omega-M gains the effect of Local Resonance.
2023-11-19 19:09:22 Omega-F gains the effect of Local Resonance.
2023-11-19 19:09:22    Omega-M takes 3214 damage.
2023-11-19 19:09:23 Omega-F hits REDACTEDAlpha for 4071 damage.
2023-11-19 19:09:23 Omega-M hits you for 3596 damage.
2023-11-19 19:09:23    Omega-M takes 424 damage.
```

## Maybe useful

- https://www.reddit.com/r/ffxiv/comments/1vey94/binary_file_format_for_combat_logs/
- https://github.com/goatcorp/Dalamud/blob/master/Dalamud/Game/Text/SeStringHandling/Payloads/ItemPayload.cs#L234
- https://github.com/goatcorp/Dalamud/blob/c7fc943692c27750df0d720fe2bddefbb75ebfed/Dalamud/Game/Text/SeStringHandling/Payload.cs#L251C42-L251C42
- https://github.com/h3lls/FFXIV-Log-Parser
