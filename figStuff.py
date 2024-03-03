# inspired by https://jwalton.info/Embed-Publication-Matplotlib-Latex/
def setSize(width,height=0):
    """Set figure dimensions to avoid scaling in LaTeX.
       width in mm

    Returns
    -------
    fig_dim: tuple
            Dimensions of figure in inches
    """
    # Convert from pt to inches
    inches_per_mm = 1 / 25.4

    # Golden ratio to set aesthetic figure height
    # https://disq.us/p/2940ij3
    golden_ratio = (5**.5 - 1) / 2

    # Figure width in inches
    fig_width_in = width * inches_per_mm
    
    if (height!=0):
        # Figure height in inches
        fig_height_in = height * inches_per_mm
    else:
        fig_height_in = fig_width_in * golden_ratio

    fig_dim = (fig_width_in, fig_height_in)

    return fig_dim

def setTexFonts(plt,fontSize=10):
    """Set text fonts to figure
      
       fontSize in pts (default 10)
    """
    #plt.style.use('seaborn')

    tex_fonts = {
        # Use LaTeX to write all text
        "text.usetex": True,
        "font.family": "serif",
        # Use 10pt font in plots, to match 10pt font in document
        "axes.labelsize": fontSize,
        "font.size": fontSize,
        # Make the legend/label fonts a little smaller
        "legend.fontsize": 0.8*fontSize,
        "xtick.labelsize": 0.8*fontSize,
        "ytick.labelsize": 0.8*fontSize
    }

    plt.rcParams.update(tex_fonts)
