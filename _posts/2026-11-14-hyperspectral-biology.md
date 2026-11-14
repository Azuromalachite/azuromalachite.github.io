---
title: "Hyperspectral Biology"
description: "A camera on a roof picked out engineered bacteria on sand from 90 metres. The bacteria were reporting on a chemical buried under them, which no camera can see."
eyebrow: "Remote sensing"
illustration: what-noticed-it
topics: ["Synthetic Biology", "Remote Sensing"]
notes:
  - "Chemla, Y., Levin, I., Fan, Y., Johnson, A. A., Coley, C. W. & Voigt, C. A. Hyperspectral reporters for long-distance and wide-area detection of gene expression in living bacteria. *Nature Biotechnology* **44**, 258–268 (2026); published online 11 April 2025. [doi:10.1038/s41587-025-02622-y](https://doi.org/10.1038/s41587-025-02622-y). See also the accompanying News & Views: Wilson, M. Z. Environmental monitoring from the air with hyperspectral reporters. *Nature Biotechnology* **44**, 194–195 (2026). [doi:10.1038/s41587-025-02668-y](https://doi.org/10.1038/s41587-025-02668-y)."
  - "The cameras are the kind that fly on satellites, and the paper says so. But nothing in the published record was detected from orbit: the demonstrations are a drone at 24 and 54 m and a fixed camera at 90 m."
  - "If you want the imaging side properly: Hong, D. et al. Hyperspectral imaging. *Nature Reviews Methods Primers* **6**, 19 (2026). [doi:10.1038/s43586-026-00470-x](https://doi.org/10.1038/s43586-026-00470-x)"
  - "Source Data for Fig. 1e: of the metabolites simulated, 2,603 came out with no absorbance peak, 17,242 with one, 651 with two and 23 with three, and Supplementary Figure 4 draws all 23. The paper gives these as 4% and 0.2%; against the 17,916 in that figure they are 3.6% and 0.13%, so the 0.2% looks to be taken against the smaller intensity-filtered set of 12,329. The counts aren't ambiguous, so I've used those. All of it is predicted — TD-DFT, B3LYP functional, 6-31G(d) basis set — not measured."
  - "`bphO`, a heme oxygenase from *Pseudomonas aeruginosa*, plus `smURFP`. The paper notes that expressing the oxygenase on its own in *E. coli* or *P. putida* gave nothing detectable. For a longer and very good read on this work, see McCarty, N. Seeing Microbes from the Sky. *Asimov Press* (2025). [doi:10.62211/23jr-64kt](https://doi.org/10.62211/23jr-64kt)"
  - "The sensor drives LacI, which represses *ppsR*, which is itself the repressor of the pigment genes — a double negative, which is how you get a signal to *increase* pigment. Background on the regulator: Steunou, A.-S., Astier, C. & Ouchane, S. Regulation of photosynthesis genes in *Rubrivivax gelatinosus*. *Journal of Bacteriology* **186**, 3133–3142 (2004). [doi:10.1128/jb.186.10.3133-3142.2004](https://doi.org/10.1128/jb.186.10.3133-3142.2004)"
  - "The raw hyperspectral images are on Zenodo: [doi:10.5281/zenodo.14756888](https://doi.org/10.5281/zenodo.14756888)"
---

A paper that came out in *Nature Biotechnology* in April last year showed that you can point a camera at an acre of ground from 90 metres away and tell, from that one image, where a particular gene is switched on.<sup class="note-ref"><a href="#note-1" id="note-ref-1" aria-label="Note 1">1</a></sup> The gene is in bacteria, the bacteria are sitting on sand, and the camera is an ordinary enough piece of equipment that people already bolt it to drones and satellites.<sup class="note-ref"><a href="#note-2" id="note-ref-2" aria-label="Note 2">2</a></sup>

I want to get to what those bacteria were actually reporting on, because that turned out to be the part I had only half remembered. But first, the camera.

**Hyperspectral imaging** is basically imaging where each pixel contains something that looks like the output of a spectrophotometer.

Normally, when we take a picture, the camera sensor records information at each pixel in three colours (RGB). On the other hand, when we want to know which wavelengths a particular compound absorbs, we put it into a spectrophotometer and measure its absorption spectrum.

A hyperspectral camera essentially combines these two things, so instead of three colour values, each pixel contains an entire spectrum telling us how light interacts with whatever is being imaged.<sup class="note-ref"><a href="#note-3" id="note-ref-3" aria-label="Note 3">3</a></sup> The benchtop camera in this paper collects 371 bands between 400 and 1,000 nm, roughly one every 2 nm; the one they flew reaches out to 2,500. Which means that if you can get an organism to make a molecule with a spectrum nothing else in the scene has, the camera can find that organism in a picture of a field.

So: what makes a good hyperspectral reporter?

**1) It needs a spectrum nothing else has.** The authors pulled 20,177 metabolites out of three reaction databases and simulated the spectrum of every one of them — simulated, rather than measured, because fewer than a hundred biological molecules have a measured absorption spectrum on record at all. (That took 25,000 CPU-days, which I enjoyed more than I should have.)

Of those, 17,916 came back with at least one absorbance peak. 651 had two. Twenty-three had three.<sup class="note-ref"><a href="#note-4" id="note-ref-4" aria-label="Note 4">4</a></sup> Twenty-three. And most of those twenty-three are bacteriochlorophylls, bacteriopheophytins and their precursors, which also absorb out past 750 nm, in the near-infrared, where soil and leaves are comparatively quiet.

(The screen didn't rank molecules by counting peaks, by the way. What it scored was *uniqueness* — how far each predicted spectrum sits from every other predicted spectrum, measured as the cost of transporting one curve into the shape of the other. Having several peaks is a property of the molecules that scored well, not the filter itself.)

**2) It should be relatively easy for bacterial cells to produce.** When we introduce a bunch of enzymes into bacteria to make them produce a particular compound, quite often this comes at the expense of cell growth, because the additional metabolic pathways impose a burden.

So, if the bacteria we are working with already produce the compound naturally, or if we only need to add two or three enzymes to get it, we have a much better chance of success. The paper makes this quantitative in a way I liked: they built a graph of every known enzymatic reaction, marked the metabolites each candidate host already makes, and then counted the shortest path from there to each target molecule. Uniqueness on one axis, enzymatic steps on the other, and you pick from the bottom right.

**3) It should stand out from the surrounding environment.** The first criterion only compares molecules against other molecules inside cells. But if we want to use these reporters in the field, their spectra also have to be distinguishable from soil, sand, rocks and plants — which the authors checked by photographing actual grass, loam and sand with the same cameras, along with denim, red-painted metal and LB agar, for reasons I would like to have heard discussed.

In the end they selected two compounds: **biliverdin IXα** and **bacteriochlorophyll a**. (Look at the structures and you'll notice both are tetrapyrroles. So are most of the twenty-three.)

Biliverdin went into *Pseudomonas putida*, a common soil bacterium and an unusually well-behaved engineering host. On paper this is the easy case — a heme oxygenase turns heme into biliverdin, one enzyme, exactly the kind of answer the shortest-path search was built to find. In practice they expressed the oxygenase and could not detect the product at all. Free tetrapyrroles don't accumulate. So they added a second gene, a protein called SmURFP that binds biliverdin and holds onto it, and the pigment stayed put.<sup class="note-ref"><a href="#note-5" id="note-ref-5" aria-label="Note 5">5</a></sup> One enzyme in the model, two genes in the organism, which is roughly the exchange rate I have come to expect.

The more interesting case is bacteriochlorophyll a, for which they used *Rubrivivax gelatinosus* — a purple non-sulfur bacterium, aquatic rather than soil-dwelling, and not a model organism by any measure. The advantage of a host like this is that it already makes bacteriochlorophyll a for its own photosynthesis, through a ten-step pathway sitting in its genome. Building that pathway in *P. putida* instead would have meant at least eleven enzymes and 19 kb of DNA. So they added no biosynthetic genes at all. They put a sensor circuit in front of *ppsR*, the repressor that normally keeps the pigment pathway turned down, and let the cell's own machinery do the rest.<sup class="note-ref"><a href="#note-6" id="note-ref-6" aria-label="Note 6">6</a></sup>

It helps that *R. gelatinosus* is a facultative phototroph, so the pigment isn't essential and you can push it around without killing the cell. The downside, of course, is that our ability to engineer organisms like this is far more limited than for the usual lab strains. (Although Chris Voigt's lab, which this is, has about as much experience with that kind of thing as anyone.)

Now, the part I had half wrong.

I had remembered this as burying engineered bacteria in soil and finding them from the air. The containers I remembered are real and they are in the paper — closed plastic boxes, 30 × 30 cm, whose lids were opened only for the few minutes of imaging and sealed again afterwards. But that is containment, not concealment. These are engineered organisms sitting outdoors in a field, and the lid belongs to the regulatory story rather than the optical one. The bacteria themselves were never buried. They were poured over the top of a kilogram of sand and left in the sun.

What was buried was the *signal*. A filter disk soaked in an acyl-homoserine lactone went a centimetre down into the sand in one container; an identical container with bacteria and a blank disk sat beside it as the control. The chemical diffused upward. The bacteria on the surface sensed it, released the brake on their own pigment pathway, and turned the colour of a purple bacterium. A hyperspectral camera on a rotating stage, at a window on the roof of a nine-storey building in Rehovot, took a single image covering an acre from 90 metres out, in thirty seconds.<sup class="note-ref"><a href="#note-7" id="note-ref-7" aria-label="Note 7">7</a></sup> The two containers came apart cleanly: 0.99 by area under the ROC curve. Pick the single most informative wavelength instead of using the whole spectrum and that falls to 0.23, which is worse than guessing.

That is the actual shape of the thing, and it is better than what I had remembered. No camera can see a chemical a centimetre under sand. Hyperspectral or not, you are looking at a surface. What the method does is recruit something that lives on that surface, give it a nose for the thing you care about, and make its answer loud in a band the scenery leaves empty.

Which means the hard limit on this is not the camera, and it is not the molecule. It is the sensor — what you can get a bacterium to notice in the first place.

You never see the thing you're looking for. You see what noticed it.
{: .blog-coda}
