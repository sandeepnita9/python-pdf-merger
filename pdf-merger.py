import PyPDF2

def mergePDF(pdfs, mergedpdf):

    #Create PDF merging class object
    mergeMyPDF = PyPDF2.PdfFileMerger() 
    
    #read input pdf files path and merge them
    for fileToMerge in pdfs:
        input_pdf_file = open(fileToMerge, "rb")
        mergeMyPDF.append(input_pdf_file)
    
    #Create blank pdf file object
    merged_file_object = open(mergedpdf, "wb")
    
    #write merged pdf file
    mergeMyPDF.write(merged_file_object)
    
    # closing the input pdf file object 
    mergeMyPDF.close() 
      
    # closing the merged pdf file object 
    mergeMyPDF.close()

def main():
    #read input file
    with open("D:\py-scripts\pdf-merge\input.txt") as input_file:
        pdfs_to_merge = input_file.read().splitlines()
        
        #name of merged file
        merged_pdf_name = "D:\py-scripts\pdf-merge\mergedpdf.pdf"
        
        #call to main pdf merger function.
        mergePDF(pdfs_to_merge, merged_pdf_name)

if __name__ == "__main__": 
    # calling the main function 
    main()
