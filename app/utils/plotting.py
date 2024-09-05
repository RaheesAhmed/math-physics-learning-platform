import io
import base64
import matplotlib.pyplot as plt


def plot_to_base64(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    plot_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    plt.close(fig)
    return plot_base64
