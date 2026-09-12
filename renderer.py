import tempfile

import matplotlib

# Use non-GUI backend
matplotlib.use("Agg")

import matplotlib.pyplot as plt


def render_latex(expr: str) -> str:
    """
    Renders a LaTeX equation to a PNG using Matplotlib.
    Returns the path to the generated image.
    """

    # Create a tiny figure (it will resize automatically)
    fig = plt.figure(figsize=(0.01, 0.01))

    # Draw the equation with a border around it
    text = fig.text(
        0,
        0,
        f"${expr}$",
        fontsize=30,
        bbox=dict(
            boxstyle="square,pad=0.4",
            facecolor="white",
            edgecolor="black",
            linewidth=1.5,
        ),
    )

    # Render once so we can calculate the size
    fig.canvas.draw()

    # Calculate the size of the rendered equation
    bbox = text.get_window_extent()

    dpi = 900

    width = bbox.width / dpi
    height = bbox.height / dpi

    # Resize the figure to fit the equation nicely
    fig.set_size_inches(width + 0.4, height + 0.4)

    # Add a small margin inside the figure
    text.set_position((0.05, 0.05))

    # Create temporary output file
    tmp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".png"
    )

    # Save the figure
    fig.savefig(
        tmp.name,
        dpi=dpi,
        bbox_inches="tight",
        pad_inches=0.4,
        facecolor="white",
        transparent=False,
    )

    plt.close(fig)

    return tmp.name