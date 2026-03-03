import scipy as sp

def plg_lowpass(y, samprate, cutoff, order=2):
    w = cutoff / (samprate / 2) # Normalize the cutoff frequency
    b, a = sp.signal.butter(N=order, Wn=w, btype='lowpass') # get the filter coefficients
    yf = sp.signal.filtfilt(b, a, y) # perform the filtering
    return yf

def plg_highpass(y, samprate, cutoff, order=2):
    w = cutoff / (samprate / 2) # Normalize the cutoff frequency
    b, a = sp.signal.butter(N=order, Wn=w, btype='highpass') # get the filter coefficients
    yf = sp.signal.filtfilt(b, a, y) # perform the filtering
    return yf

def plg_bandpass(y, samprate, cutoffs, order=2):
    cutoffs = np.array(cutoffs)
    w = cutoffs / (samprate / 2) # Normalize the cutoff frequencies
    b, a = sp.signal.butter(N=order, Wn=w, btype='bandpass') # get the filter coefficients
    yf = sp.signal.filtfilt(b, a, y) # perform the filtering
    return yf

def plg_bandstop(y, samprate, cutoffs, order=2):
    cutoffs = np.array(cutoffs)
    w = cutoffs / (samprate / 2) # Normalize the cutoff frequencies
    b, a = sp.signal.butter(N=order, Wn=w, btype='bandstop') # get the filter coefficients
    yf = sp.signal.filtfilt(b, a, y) # perform the filtering
    return yf
