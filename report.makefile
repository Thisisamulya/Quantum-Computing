ALL_FIGURE_NAMES=$(shell cat report.figlist)
ALL_FIGURES=$(ALL_FIGURE_NAMES:%=%.pdf)

allimages: $(ALL_FIGURES)
	@echo All images exist now. Use make -B to re-generate them.

FORCEREMAKE:

-include $(ALL_FIGURE_NAMES:%=%.dep)

%.dep:
	mkdir -p "$(dir $@)"
	touch "$@" # will be filled later.

report-figure0.pdf: 
	pdflatex -halt-on-error -interaction=batchmode -jobname "report-figure0" "\def\tikzexternalrealjob{report}\input{report}"; magick convert -density 300 -transparent white "report-figure0.pdf" "report-figure0.png"

report-figure0.pdf: report-figure0.md5
report-figure1.pdf: 
	pdflatex -halt-on-error -interaction=batchmode -jobname "report-figure1" "\def\tikzexternalrealjob{report}\input{report}"

report-figure1.pdf: report-figure1.md5
report-figure2.pdf: 
	pdflatex -halt-on-error -interaction=batchmode -jobname "report-figure2" "\def\tikzexternalrealjob{report}\input{report}"

report-figure2.pdf: report-figure2.md5
report-figure3.pdf: 
	pdflatex -halt-on-error -interaction=batchmode -jobname "report-figure3" "\def\tikzexternalrealjob{report}\input{report}"

report-figure3.pdf: report-figure3.md5
report-figure4.pdf: 
	pdflatex -halt-on-error -interaction=batchmode -jobname "report-figure4" "\def\tikzexternalrealjob{report}\input{report}"

report-figure4.pdf: report-figure4.md5
report-figure5.pdf: 
	pdflatex -halt-on-error -interaction=batchmode -jobname "report-figure5" "\def\tikzexternalrealjob{report}\input{report}"

report-figure5.pdf: report-figure5.md5
report-figure6.pdf: 
	pdflatex -halt-on-error -interaction=batchmode -jobname "report-figure6" "\def\tikzexternalrealjob{report}\input{report}"

report-figure6.pdf: report-figure6.md5
report-figure7.pdf: 
	pdflatex -halt-on-error -interaction=batchmode -jobname "report-figure7" "\def\tikzexternalrealjob{report}\input{report}"

report-figure7.pdf: report-figure7.md5
