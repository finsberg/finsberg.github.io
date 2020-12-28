PY=python
PANDOC=pandoc


help:
	@echo ' 																	  '
	@echo 'Makefile for the Markdown CV                                       '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make html                        (re)generate the web site          '
	@echo '   make pdf                         generate a PDF file  			  '
	@echo '   make docx	                   generate a Docx file 			  '
	@echo '   make tex	                   generate a tex file 			  '
	@echo '                                                                       '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html'
	@echo ' 																	  '
	@echo 'pandoc test.md -o test.pdf --bibliography=test_ref.bib --csl=plos.csl  '
	@echo ' 																	  '
	@echo 'get templates from: https://github.com/jgm/pandoc-templates			  '

pdf:
	pandoc -s -f markdown-auto_identifiers \
	../_index.md \
	-o "cv.pdf" \
	--template="template.tex" \
	--pdf-engine=xelatex

tex:
	pandoc -s \
	../_index.md \
	-o "cv.tex" \
	--template="template.tex" \
	--pdf-engine=xelatex

docx:
	pandoc ../_index.md \
	-o "cv.docx" \

html:
	pandoc ../_index.md \
	-o "cv.html"

clean:
	rm -f cv*

.PHONY: help pdf docx html tex
