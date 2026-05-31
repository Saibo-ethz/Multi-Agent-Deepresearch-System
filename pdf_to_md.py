import pymupdf4llm
from pathlib import Path

INPUT_DIR = Path("C:/Users/Lenovo/Desktop/Building Automation")
OUTPUT_DIR = INPUT_DIR / "md_output"
OUTPUT_DIR.mkdir(exist_ok=True)

pdf_files = list(INPUT_DIR.rglob("*.pdf"))
print(f"found {len(pdf_files)} PDF files")

for i, pdf_path in enumerate(pdf_files, 1):
    try:
        print(f"[{i}/{len(pdf_files)}] converting: {pdf_path.name}")
        md_text = pymupdf4llm.to_markdown(str(pdf_path))
        output_path = OUTPUT_DIR / (pdf_path.stem + ".md")
        output_path.write_text(md_text, encoding="utf-8")
        print(f"  done: {output_path.name}")
    except Exception as e:
        print(f"  failed: {pdf_path.name} | {e}")

print("finished")
