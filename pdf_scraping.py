# Working on text scrpaing from pdf
import os
import PyPDF2
from collections import Counter
from pathlib import Path

# Define the file path with Unicode characters
# Define the file path with Unicode characters
file_path = r'C:\Users\shres\Desktop\r_direct\sem_6_syllabus.pdf'

# Open the PDF file in read-binary mode
with open(file_path, 'rb') as file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(file)
    
    # Iterate over each page in the PDF
    ''' The code velow gave error '''
    # for page_num in range(pdf_reader.numPages):
    #     # Extract the text from the current page
    #     page = pdf_reader.getPage(page_num)
    #     text = page.extractText()

    '''This code worked and gives all the text from the pdf.'''
    for page_num in range(len(pdf_reader.pages)):
        # Extract the text from the current page
        page = pdf_reader.pages[page_num]
        text = page.extract_text()



        # Process and print the extracted text
        print("Page", page_num + 1)
        print(text)
        print("-" * 40)





'''Now i want to work on manipulation of these strings. I want count of unique letters from here.'''    
'''Here's the Code to get count of words'''

'''with open(r'C:\Users\shres\Desktop\r_direct\Sem 6 DU SYLLABUS .pdf', 'rb') as file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(file)
    extracted_text = ""
    for page in pdf_reader.pages:
        extracted_text += page.extract_text()
# Convert the extracted text to lowercase
lowercase_text = extracted_text.lower()
# Split the text into words
words = lowercase_text.split()
# Count the occurrences of each word
word_counts = Counter(words)
ordered_words = word_counts.most_common()
college_count = word_counts["college"]
print(college_count)'''