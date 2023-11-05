import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider


def dirac_delta_function(a, x):
    """
    Returns the Dirac delta function for a given energy and temperature.

    Parameters
    ----------
    x : float
        x in the Dirac delta function.
    a : float
        a in the Dirac delta function.

    Returns
    -------
    float
        Dirac delta function.
    """
    return np.exp(-((x / a) ** 2)) / (np.abs(a) * np.sqrt(np.pi))


def update(val):
    """
    Updates the plot when the slider is moved.

    Parameters
    ----------
    val : float
        Slider value. No usage in this function.
    """
    a = a_slider.val

    line.set_ydata(dirac_delta_function(a, x))

    line.set_label("a = " + str(round(a, 2)))
    ax.legend()
    fig.canvas.draw_idle()


if __name__ == "__main__":
    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.25)
    x = np.linspace(-2.0, 2.0, 5000)
    line, = ax.plot(x, dirac_delta_function(0.1, x), label="a = 1")
    
    axa = fig.add_axes([0.15, 0.05, 0.65, 0.03])
    a_slider = Slider(ax=axa, label="a", valmin=1e-3, valmax=1.0, valinit=0.1, orientation="horizontal")
    
    a_slider.on_changed(update)

    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title("Dirac delta function")
    ax.legend()

    plt.show()
