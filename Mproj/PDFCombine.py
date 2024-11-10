import PyPDF2
import os

def get_pdf_list():
    pdf_list = []
    while True:
        pdf = input("Enter the name of the PDF file you want to combine: ")
        if os.path.exists(pdf):
            pdf_list.append(pdf)
        else:
            print(f"File '{pdf}' does not exist")
        if input("Do you want to add more files? (Y/N): ").lower() == 'n':
            break
    return pdf_list

def combine_pdfs(pdf_list, output_pdf):
    merger = PyPDF2.PdfMerger()

    for pdf in pdf_list:
        try:
            with open(pdf, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                if len(pdf_reader.pages) > 0:
                    merger.append(pdf)
                else:
                    print(f"{pdf} has no pages.")
        except Exception as e:
            print(f"Error reading {pdf}: {e}")
            continue
    try:
        with open(output_pdf, 'wb') as output:
            merger.write(output)
        print(f"Successfully combined PDFs into {output_pdf}")
    except Exception as e:
        print(f"Error writing output file: {e}")
    finally:
        merger.close()

if __name__ == '__main__':
    output_pdf = input("Enter the name of the output PDF file (e.g., combined.pdf): ")
    if not output_pdf.endswith('.pdf'):
        output_pdf += '.pdf'
    
    pdf_list = get_pdf_list()
    if pdf_list:
        combine_pdfs(pdf_list, output_pdf)
    else:
        print("No PDF files to combine.")