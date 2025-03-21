ALL_FIGURE_NAMES=$(shell cat pic.figlist)
ALL_FIGURES=$(ALL_FIGURE_NAMES:%=%.pdf)

allimages: $(ALL_FIGURES)
	@echo All images exist now. Use make -B to re-generate them.

FORCEREMAKE:

-include $(ALL_FIGURE_NAMES:%=%.dep)

%.dep:
	mkdir -p "$(dir $@)"
	touch "$@" # will be filled later.

pic-figure0.pdf: 
	pdflatex -halt-on-error -interaction=batchmode -jobname "pic-figure0" "\def\tikzexternalrealjob{pic}\input{pic}"

pic-figure0.pdf: pic-figure0.md5
