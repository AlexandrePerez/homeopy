# HomeoPy Repository

Have your ever want to apply homeopathy to your books? Well, I do.
Yes, this is a pretty stupid idea. But hey! I know you love stupid and meaningless projects too.

_disclaimer_: homeopathy is just **pseudo-science bullshit** and its only effects are due to the placebo effect (until proven otherwise).

## How does this even work?

Shut up, it's quantum!

Or if you want a more detailed explanation:
* step 1, dilute : at 1CH each word (definde word) has a 1% chance of being kept during the dilution. You can choose the solvent.
* step 2, energize: (random permutations), this is **very** important. If you skip the magic doesn't happen. 
* step 3: repeat steps 1 and 2 *ch* times.
* step 4: ?
* step 5: profit. For real.

High CH may take a while. 
Also, at high CH your chance of getting a single word from the original file is so low you can expect to get only solvent.
But don't worry, *water_memory* is *True*.

## Example

Dilute your text with "~" at 1CH:

`
text = Homeo("myfile", solvent="~", ntimes=2)
text.homeify(ch=1)
`