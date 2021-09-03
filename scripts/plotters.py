import matplotlib.pyplot as plt

def plotMany(signal,centers):
    fig, axs = plt.subplots(3)

    axs[0].set_ylabel('Amplitude')
    axs[0].set_xlabel('Samples')
    axs[0].set_title('Complex plane')
    axs[0].plot(signal.signal)

    axs[1].set_ylabel('Im(z)')
    axs[1].set_xlabel('Re(z)')
    #axs[1].set_xlim(-3,3)
    #axs[1].set_ylim(-3,3)
    axs[1].set_title('Z-plane')
    axs[1].plot(signal.zTransform(1)[0], signal.zTransform(1)[1])

    axs[2].set_title('F-plane')
    axs[2].set_ylabel('Amplitude/2')
    axs[2].set_xlabel('Frequence')
    axs[2].plot(centers[0], centers[1])

    fig.tight_layout(pad=1)
    plt.show()
