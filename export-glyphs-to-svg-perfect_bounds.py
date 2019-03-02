import os 

# grab current font
f = CurrentFont()
# set up canvas size
# W,H = 1000,1000

# # for each glyph in the current font...
# for g in f:
    
# # for each selected glyph in font...
for glyphName in f.selectedGlyphNames:
    g = f[glyphName]
    # check that there is a drawing 
    if g.box != None:
        # get drawing size
        # print(g.box)
        # get drawing bounds with g.box, then calculate its width and height
        W = g.box[2] - g.box[0]
        H = g.box[3] - g.box[1]
        # make a new page
        newPage(W,H)
        # calculate what margin will put the given glyph in the middle
        # evenMargin = (W - g.width) / 2
        # print(g.box)
    
        # calculate total height of 
    
        # translate the given glyph so it's in the middle
        translate(-abs(g.box[0]),abs(g.box[1]))
        # draw the glyph
        drawGlyph(g)
        # create the file name
        fileName = f.info.familyName + "-" + f.info.styleName + "-" + g.name + ".svg"
        
        
        #get folder of UFO
        
        head,tail = os.path.split(f.path)
        
        print(fileName + " saved to " + head)
        
        # save with folder (make sure folder exists)
        saveImage(head + "/" + fileName)