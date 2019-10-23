#!/usr/bin/env python

from PyPDF2 import PdfFileReader, PdfFileWriter


def main():
    filename = "D://Users//Benjamin//Downloads//SCN_0001.pdf"
    with open(filename, 'rb') as infile:
        reader = PdfFileReader(infile)
        writer = PdfFileWriter()
        #for x in range(5, reader.getNumPages()):
        x = 0
        writer.addPage(reader.getPage(x))
        with open('output' + str(x) + '.pdf', 'wb') as outfile:
            writer.write(outfile)


if __name__ == "__main__":
    main()
