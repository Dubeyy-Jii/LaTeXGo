import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import uuid

def render_latex(expr):
    fig=plt.figure(figsize=(0.01,0.01))
    fig.patch.set_alpha(0)
    plt.axis("off")
    plt.text(0.5,0.5,f"${expr}$",fontsize=24,ha="center",va="center")
    name=f"/tmp/{uuid.uuid4().hex}.png"
    plt.savefig(name,dpi=600,bbox_inches="tight",transparent=True,pad_inches=0.05)
    plt.close(fig)
    return name
