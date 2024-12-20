""" Common formatting and print commands for ISP
These commands ensure a common layout, and reduce the code required to generate
plots in the other modules.
"""

# author: Thomas Haslwanter, date: Sept-2021

# Import standard packages
import matplotlib.pyplot as plt
import os

# additional packages
import matplotlib as mpl


def setFonts(fs: int=16) -> None:
    """Set my favorite defaulte fonts

    Parameters
    ----------
    fs : font-size
    """
    
    font = {'family' : 'sans-serif',
            'weight' : 'normal',
            'size'   : fs}

    xtick = {'direction': 'out',
             'major.size': 6,
             'labelsize': fs-2}
    
    ytick = {'direction': 'out',
             'major.size': 6,
             'labelsize': fs-2}
    
    axes = {'labelsize': fs,
            'titlesize': fs}
    
    legend = {'fontsize': fs}
    
    figure = {'autolayout': True}
    
    mpl.rc('font', **font)
    mpl.rc('xtick', **xtick)
    mpl.rc('ytick', **ytick)
    mpl.rc('axes', **axes)
    mpl.rc('legend', **legend)
    mpl.rc('figure', **figure)
    
    
def showData(out_file: str, out_dir: str='.') -> None:
    """ Save a figure with subplots to a file, and then display it

    Parameters
    ----------
    out_file : name of out-file
    out_dir  : path of out-file
    """
    
    if out_dir is not None:
        # Generate the plot
        saveTo = os.path.join(out_dir, out_file)
        if out_file[-3:].lower() == 'jpg':
            pil_kwargs = {'quality': 95}
            plt.savefig(saveTo, dpi=300, pil_kwargs=pil_kwargs)
        else:
            plt.savefig(saveTo, dpi=300)
    
        # Show the user where the file is saved to
        print('OutDir: {0}'.format(out_dir))
        print('Figure saved to {0}'.format(out_file))
    
    # Show the plot
    plt.show()
    plt.close()


if __name__ == '__main__':
    setFonts()
