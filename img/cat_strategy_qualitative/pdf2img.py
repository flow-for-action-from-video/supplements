import pdf2image

for i in range(1, 7):
    pages = pdf2image.convert_from_path(f"{i}.pdf")
    for page in pages:
        page.save(f"{i}.png", "png")