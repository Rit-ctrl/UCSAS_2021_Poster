SOURCES=$(shell find . -name "*.Rmd")
TARGET=$(SOURCES:%.Rmd=%.pdf)

all: $(TARGET)

%.pdf : %.Rmd
	Rscript -e 'rmarkdown::render("$<", output_format = "beamer_presentation")'

clean :
	rm -rf *.pdf *.log


