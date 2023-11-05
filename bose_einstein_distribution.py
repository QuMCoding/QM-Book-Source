import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider

def bose_einstein_distribution(energy, temperature):
    """
    Returns the Bose-Einstein distribution function for a given energy, temperature, and chemical potential.

    Parameters
    ----------
    energy : float
        Energy of the state.
    temperature : float
        Temperature of the system.
    chemical_potential : float
        Chemical potential of the system.

    Returns
    -------
    float
        Bose-Einstein distribution function.
    """
    k = 8.617333262145e-5  # Boltzmann constant in eV/K
    A = 1.0
    return 1.0 / (A * np.exp((energy) / (temperature * k)) - 1.0)

def update(val):
    """
    Updates the plot when the slider is moved.

    Parameters
    ----------
    val : float
        Slider value.
    """
    temperature = temperature_slider.val

    line.set_ydata(bose_einstein_distribution(energy, temperature))

    line.set_label("T = " + str(round(temperature, 2)) + " K")
    ax.legend()
    fig.canvas.draw_idle()
    

if __name__ == "__main__":
    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.25)
    energy = np.linspace(0.0, 0.1, 1000)
    line, = ax.plot(energy, bose_einstein_distribution(energy, 100), label="T = 100 K")
    
    axtemp = fig.add_axes([0.25, 0.1, 0.65, 0.03])
    temperature_slider = Slider(ax=axtemp, label="Temperature (K)", valmin=0.0, valmax=10000.0, valinit=100, orientation="horizontal")
    
    temperature_slider.on_changed(update)

    ax.set_xlabel("Energy (eV)")
    ax.set_ylabel("<n>")
    ax.set_title("Bose-Einstein distribution")
    ax.legend()

    plt.show()

