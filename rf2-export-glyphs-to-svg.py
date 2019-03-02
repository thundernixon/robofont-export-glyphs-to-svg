# grab current font
f = CurrentFont()
# set up canvas size
W,H = 1000,1000

# for each glyph in the current font...
for g in f:
    # make a new page
    newPage(W,H)
    # calculate what margin will put the given glyph in the middle
    evenMargin = (W - g.width) / 2
    # translate the given glyph so it's in the middle
    translate(evenMargin,-f.info.descender)
    # draw the glyph
    drawGlyph(g)
    # create the file name
    fileName = f.info.familyName + "-" + f.info.styleName + "-" + g.name + ".svg"
    # save with folder (make sure folder exists)
    saveImage("rf2-exports/" + fileName)