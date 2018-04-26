import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import POSTPROCv16 as PP
import SPECGENv15 as SG


def extract_spectrum(realspec, fakespec):
    """returns 2d array with columns [wavelength, realflux, fakeflux, residuals]"""
    real_spec = np.loadtxt(realspec)
    fake_spec = np.loadtxt(fakespec)
    wavelengths = real_spec[:, 0]
    realflux = real_spec[:, 1]
    fakeflux = fake_spec[:, 1]
    output_array = np.zeros((np.size(wavelengths), 4))
    output_array[:, 0] = wavelengths
    output_array[:, 1] = realflux
    output_array[:, 2] = fakeflux
    output_array[:, 3] = realflux - fakeflux
    return output_array

def plot_results(array, waverange, fluxrange):
    gs = gridspec.GridSpec(2, 1, height_ratios=[2, 1])
    fig = plt.figure(figsize=(22,15))
    plt.subplots_adjust(hspace=0.0001)
    spectra = plt.subplot(gs[0])
    spectra.plot(array[:, 0], array[:, 1], color='Black', linewidth=3, label='real')
    spectra.plot(array[:, 0], array[:, 2], color='FireBrick', linewidth=3, label='synthetic')
    plt.yticks(np.arange(fluxrange[0], fluxrange[1], step=(fluxrange[1]-fluxrange[0])/10))
    plt.ylim(fluxrange[0], fluxrange[1])

    residuals = plt.subplot(gs[1], sharex=spectra)
    residuals.plot(array[:, 0], array[:, 3], color='SeaGreen', linewidth=3)
    plt.yticks=(np.arange(np.min(array[:, 3]), np.max(array[:, 3]),
                          (np.max(array[:, 3])-np.min(array[:, 3]))/10))
    plt.ylim(np.min(array[:, 3])*1.1, np.max(array[:, 3])*0.9)

    spectra.set_xticks(np.arange(waverange[0], waverange[1], (waverange[1]-waverange[0])/10))
    spectra.set_xlim(waverange[0], waverange[1])

    residuals.plot([array[0, 0], array[-1, 0]], [0.025, 0.025], color='Grey', linestyle='--', linewidth=1.5)
    residuals.plot([array[0, 0], array[-1, 0]], [-0.025, -0.025], color='Grey', linestyle='--', linewidth=1.5)

    spectra.legend()
    plt.setp(spectra.get_xticklabels(), visible=False)
    plt.show()


if __name__ == "__main__":
    SG.Main('generate.param')
    PP.Main('postproc.param')
    realspec = "/home/donald/Desktop/PYTHON/ANNA_CNN/linelist_tune/vald_tune/median_solar_spec"
    fakespec = "/home/donald/Desktop/PYTHON/ANNA_CNN/linelist_tune/vald_tune/0.0001.vsn.spec"
    extracted_array = extract_spectrum(realspec, fakespec)
    plot_results(extracted_array, (6730.0, 6785.0), (0.75, 1.04))
