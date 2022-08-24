ROOT = root
BIBTEX = $(ROOT)
PDFLATEX = pdflatex
PDFLATEX_ARGS = -file-line-error -interaction nonstopmode -recorder --src-specials

all: clean pdf

distclean: clean
	rm -f  *.pdf

check:
	chktex -n 2 -n 8 -n 6 -n 38 -n 13 -n 36 -n 24 $(ROOT)
	bibclean $(BIBTEX) > /dev/null

clean:
	rm -f *~ *.log *.aux *.toc *.dvi *.bbl *.blg *.*~* *.lof *.lot *.cb *.backup *.out *.glo *.idx *.fls *.lol *.ilg *.gls *.plog *.ind *.npc *.nps
	find . -name "*.pdftk" -delete
	-find papers-numbered -name "*.pdf*" -delete

pdf:
	-$(PDFLATEX) -draftmode $(PDFLATEX_ARGS) $(ROOT)
#	-makeindex -s confproc2.ist $(ROOT).idx
	$(PDFLATEX) -draftmode $(PDFLATEX_ARGS) $(ROOT)
	$(PDFLATEX) $(PDFLATEX_ARGS) $(ROOT)

split-pages: 
	# TODO: edit papers_split_all.sh to disconsider pages from frontmatter when setting the start and end pages
	mkdir -p papers-info papers-numbered/papers
	./exportIndividualPDFs.sh `pwd` root papers-info papers-numbered papers papers
	./fixPDFs.sh
