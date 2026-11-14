---
title: "Hyperspectral Biology"
description: "A camera on a roof picked out engineered bacteria on sand from 90 metres. The bacteria were reporting on a chemical buried under them, which no camera can see."
eyebrow: "Remote sensing"
illustration: what-noticed-it
topics: ["Synthetic Biology", "Remote Sensing"]
notes:
  - "Chemla, Y., Levin, I., Fan, Y., Johnson, A. A., Coley, C. W. & Voigt, C. A. Hyperspectral reporters for long-distance and wide-area detection of gene expression in living bacteria. *Nature Biotechnology* **44**, 258–268 (2026); published online 11 April 2025. [doi:10.1038/s41587-025-02622-y](https://doi.org/10.1038/s41587-025-02622-y). See also the accompanying News & Views: Wilson, M. Z. Environmental monitoring from the air with hyperspectral reporters. *Nature Biotechnology* **44**, 194–195 (2026). [doi:10.1038/s41587-025-02668-y](https://doi.org/10.1038/s41587-025-02668-y)."
  - "The cameras in question are the kind that fly on satellites, and the paper says so. But nothing here was detected from orbit. The demonstrations are a drone at 15 and 54 m and a fixed camera at 90 m, and that is the whole of it so far."
  - "Counts from the paper's Source Data for Fig. 1e: of 20,170 metabolites simulated, 2,603 came out with no absorbance peak, 17,242 with one, 651 with two and 23 with three. The 23 are drawn individually in Supplementary Figure 4. These are predicted spectra, not measured ones — TD-DFT with the B3LYP functional and a 6-31G(d) basis."
  - "Which is not nothing: the sensor circuit was inserted upstream of *ppsR*, the transcription factor that holds the native photosystem genes down. Steunou, A.-S., Astier, C. & Ouchane, S. Regulation of photosynthesis genes in *Rubrivivax gelatinosus*. *Journal of Bacteriology* **186**, 3133–3142 (2004). [doi:10.1128/jb.186.10.3133-3142.2004](https://doi.org/10.1128/jb.186.10.3133-3142.2004)"
  - "Two, according to Niko McCarty's write-up of the paper, which is the best long read on this work and where several of the details here that are not in the figures come from. McCarty, N. Seeing Microbes from the Sky. *Asimov Press* (2025). [doi:10.62211/23jr-64kt](https://doi.org/10.62211/23jr-64kt). I could not confirm the count from the paper itself, which is paywalled past the figures."
  - "The raw hyperspectral images are on Zenodo: [doi:10.5281/zenodo.14756888](https://doi.org/10.5281/zenodo.14756888)"
---

A paper that came out in *Nature Biotechnology* in April last year showed that you can point a camera at an acre of ground from 90 metres away and tell, from that one image, where a particular gene is switched on.<sup class="note-ref"><a href="#note-1" id="note-ref-1" aria-label="Note 1">1</a></sup> The gene is in bacteria, the bacteria are spread on sand, and the camera is an ordinary enough piece of equipment that people already bolt it to drones and satellites.<sup class="note-ref"><a href="#note-2" id="note-ref-2" aria-label="Note 2">2</a></sup>

I want to get to what the bacteria were actually reporting on, because that turned out to be the part I had misremembered. But first, the camera.

**Hyperspectral imaging** is basically imaging where each pixel contains something that looks like the output of a spectrophotometer.

Normally, when we take a picture, the camera sensor records information at each pixel in three colours (RGB). On the other hand, when we want to know which wavelengths a particular compound absorbs, we put it into a spectrophotometer and measure its absorption spectrum.

A hyperspectral camera essentially combines these two things, so instead of three colour values, each pixel contains an entire spectrum telling us how light interacts with whatever is being imaged. Which means that if you can get an organism to make a molecule with a spectrum nothing else in the scene has, the camera can find that organism in a picture of a field.

So: what makes a good hyperspectral reporter?

**1) It needs a spectrum nothing else has.** The authors took 20,170 metabolites out of reaction databases and simulated the spectrum of every one of them. Simulated, rather than measured, because only about a hundred biological molecules have a measured absorption spectrum on record at all — which I did not know, and which is its own small scandal.

Of those 20,170, 17,916 came back with at least one absorbance peak. 651 had two. Twenty-three had three.<sup class="note-ref"><a href="#note-3" id="note-ref-3" aria-label="Note 3">3</a></sup> Twenty-three. And most of those twenty-three are bacteriochlorophylls, bacteriopheophytins and their precursors, which also absorb out past 750 nm, in the near-infrared, where soil and leaves are comparatively quiet.

(The screen didn't literally filter on peak count, by the way — counting peaks is just the quickest way to see how thin the field is. What they actually ranked was *uniqueness*: how far each predicted spectrum sits from every other predicted spectrum, measured as the cost of transporting one curve into the shape of the other.)

**2) It should be relatively easy for bacterial cells to produce.** When we introduce a bunch of enzymes into bacteria to make them produce a particular compound, quite often this comes at the expense of cell growth, because the additional metabolic pathways impose a burden.

So, if the bacteria we are working with already produce the compound naturally, or if we only need to add two or three enzymes to get it, we have a much better chance of success. The paper makes this quantitative in a way I liked: they built a graph of every known enzymatic reaction, marked the metabolites each candidate host already makes, and then counted the shortest path from there to each target molecule. Uniqueness on one axis, enzymatic steps on the other, and you pick from the bottom right.

**3) It should stand out from the surrounding environment.** The first criterion only compares molecules against other molecules inside cells. But if we want to use these reporters in the field, their spectra also have to be distinguishable from soil, sand, rocks and plants — which the authors checked by photographing actual grass, loam and sand with the same cameras.

In the end they selected two compounds: **biliverdin IXα** and **bacteriochlorophyll a**. (Look at the structures and you'll notice both are tetrapyrroles. So are most of the twenty-three.)

Biliverdin went into *Pseudomonas putida*, a common soil bacterium and an unusually well-behaved engineering host. That one is the straightforward case.

The more interesting case is bacteriochlorophyll a, for which they used *Rubrivivax gelatinosus* — a purple non-sulfur bacterium, aquatic rather than soil-dwelling, and not a model organism by any measure. The advantage of a host like this is that it already makes bacteriochlorophyll a for its own photosynthesis, through a ten-step pathway it keeps in its genome, so there is no pathway to install. They didn't add a single biosynthetic gene to it. They put a sensor circuit in front of the regulator that normally keeps that pathway switched down.<sup class="note-ref"><a href="#note-4" id="note-ref-4" aria-label="Note 4">4</a></sup> For *P. putida*, making biliverdin took two genes.<sup class="note-ref"><a href="#note-5" id="note-ref-5" aria-label="Note 5">5</a></sup>

The downside, of course, is that our ability to engineer organisms like *R. gelatinosus* is far more limited than for the usual lab strains. (Although Chris Voigt's lab, which this is, has about as much experience with that kind of thing as anyone.)

Now, the part I had wrong.

I had remembered this as burying engineered bacteria in soil and finding them from the air, and that is not what happened. The bacteria were spread on sand, in open boxes, in plain sight of the camera. Seven grams of sand at a time, in the laboratory version. Nothing was hidden about them at all.

What was buried was the *signal*. In the outdoor run, a filter disk soaked in an acyl-homoserine lactone went a centimetre under the sand in one box; an identical box with bacteria and no disk sat nearby as the control. The chemical diffused upward through the sand. The bacteria on the surface sensed it, turned on the regulator, filled with bacteriochlorophyll, and changed what they did to light. A camera mounted on a building roof, on a rotating platform, took a single image covering about 4,000 square metres from 90 metres out, and the two boxes came apart cleanly.<sup class="note-ref"><a href="#note-6" id="note-ref-6" aria-label="Note 6">6</a></sup>

That is the actual shape of the thing, and it is better than what I had remembered. No camera can see a chemical a centimetre under sand. Hyperspectral or not, you are looking at a surface. What the method does is recruit something that lives on that surface, give it a nose for the thing you care about, and make its answer loud in a wavelength band the scenery leaves empty.

Which means the hard limit on this is not the camera, and it is not the molecule. It is the sensor — what you can get a bacterium to notice in the first place.

You never see the thing you're looking for. You see what noticed it.
{: .blog-coda}
