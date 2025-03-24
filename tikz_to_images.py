import subprocess
# from pypdf import PdfReader
from pathlib import Path

def extract_tikz_to_images(latex_file, output_dir, image_format="png"):
    """
    Extracts tikzpicture environments from a LaTeX file and converts them to images.

    Args:
        latex_file (str): Path to the LaTeX file.
        output_dir (str): Directory to save the extracted images.
        image_format (str): Desired image format (e.g., 'png', 'svg', 'jpg').
    """
    if image_format not in {"png", "svg", "jpg"}:
        raise ValueError("Unsupported image format. Use 'png', 'svg', or 'jpg'.")

    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    with open(latex_file, "r") as file:
        content = file.read()

    # Extract tikzpicture environments
    tikz_blocks = []
    start_tag = "\\begin{tikzpicture}"
    end_tag = "\\end{tikzpicture}"
    start = 0

    while True:
        start = content.find(start_tag, start)
        if start == -1:
            break
        end = content.find(end_tag, start) + len(end_tag)
        tikz_blocks.append(content[start:end])
        start = end

    if not tikz_blocks:
        print("No tikzpicture environments found.")
        return

    # Process each tikzpicture block
    for i, tikz in enumerate(tikz_blocks):
        standalone_latex = f"""
\\documentclass[tikz,border=2mm]{{standalone}}
\\usepackage{{tikz}}
\\usetikzlibrary{{external, shapes.geometric, arrows, arrows.meta}}
\\begin{{document}}
    {tikz}
\\end{{document}}
        """
        temp_tex_file = Path(output_dir) / f"tikz_temp_{i}.tex"
        temp_pdf_file = temp_tex_file.with_suffix(".pdf")
        temp_image_file = temp_tex_file.with_suffix(f".{image_format}")
        # temp_image_file is not used, so it has been removed
        # Write standalone LaTeX file
        with open(temp_tex_file, "w") as file:
            file.write(standalone_latex)

        # Compile LaTeX to PDF
        try:
            subprocess.run(
            ["pdflatex", "-output-directory", output_dir, str(temp_tex_file)],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            )
        except subprocess.CalledProcessError as e:
            print(f"Error compiling {temp_tex_file}: {e}")
            continue

        # Convert PDF to SVG using pdftocairo
        try:
            svg_output = temp_tex_file.with_suffix(".svg")
            subprocess.run(
            ["pdftocairo", "-svg", str(temp_pdf_file), str(svg_output)],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            )
            print(f"Generated {svg_output}")
        except subprocess.CalledProcessError as e:
            print(f"Error converting {temp_pdf_file} to SVG: {e}")
            continue

        # Convert PDF to PNG using pdftocairo
        try:
            png_output = temp_tex_file.with_suffix(".png")
            subprocess.run(
            ["pdftocairo", "-png", str(temp_pdf_file), str(png_output)],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            )
            print(f"Generated {png_output}")
        except subprocess.CalledProcessError as e:
            print(f"Error converting {temp_pdf_file} to PNG: {e}")
            continue

        # Clean up temporary files
        temp_tex_file.unlink(missing_ok=True)
        temp_pdf_file.unlink(missing_ok=True)
        aux_file = temp_tex_file.with_suffix(".aux")
        log_file = temp_tex_file.with_suffix(".log")
        aux_file.unlink(missing_ok=True)
        log_file.unlink(missing_ok=True)

if __name__ == "__main__":
    # Example usage
    latex_file_path = "pic.tex"  # Replace with your LaTeX file path
    output_directory = "output_images"
    image_formats = "png"  # Change to 'svg' or 'jpg' if needed

    extract_tikz_to_images(latex_file_path, output_directory, image_formats)