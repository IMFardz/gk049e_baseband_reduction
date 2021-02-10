"""
Includes class objects for folding baseband data
"""
import astropy.units as u
from baseband_tasks import dm, dispersion, channelize, functions, integration, fourier
from pulsar import predictor
from baseband_tasks.io import hdf5


class Fold:
    """Folds data"""

    def __init__(self, fh, dispersion_measure, frequency,
                 sideband, polyco_file,
                 polarization, fullpol, nthreads, start):

        self.dispersion_measure = dispersion_measure
        self.frequency = frequency
        self.sideband = sideband
        self.polyco_file = polyco_file
        self.polarization = polarization
        self.fullpol = fullpol
        self.nthreads = nthreads
        self.interval = 10 * u.s  # Sub integration time interval
        self.start = start
        self.integrator = self.initialize_pipeline(fh)


    def initialize_pipeline(self, fh):
        """"Setup the dedisperser, produce intensities and return the integrator"""
        dispersion_measure = dm.DispersionMeasure(self.dispersion_measure)
        psr_polyco = predictor.Polyco(self.polyco_file)

        # Build the pipeline
        dedisperser = dispersion.Dedisperse(fh, dispersion_measure, 327*u.MHz,
                                            frequency=self.frequency, sideband=self.sideband)
        channelizer = channelize.Channelize(dedisperser, 4096, frequency=self.frequency, sideband=self.sideband)
        if self.fullpol:
            power = functions.Power(channelizer, polarization=self.polarization)
        else:
            power = functions.Square(channelizer, polarization=self.polarization)
        integrator = integration.Fold(power, n_phase=1024, phase=psr_polyco, step=self.interval, start=self.start, average=True)

        return integrator

    def integrate_and_save(self, count=1, output=None):
        """Produces and outputs sample"""
        tstart = self.integrator.time
        print('Starting at time {0}'.format(tstart.iso))

        # EXPERIMENTAL: USE hd5f file format:
        output.read(count=count, out=self.h5w)

        # ORIGINAL: USES NUMPY ARRAY AS OUTPUT
        # if output is None:
        #     print('reading out output array')
        #     output = self.integrator.read(count=count)
        # else:
        #     output = self.integrator.read(out=output)

        # Note - calculating the time doesn't currently work for the
        # integrator if you are using bins in phase.

        #return output, tstart
        return tstart
