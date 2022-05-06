import os
import time
from tqdm import tqdm
from PyPDF2 import PdfFileReader, PdfFileMerger

def search_pdfs():
    pdf_dir_list = []
    dir_name = os.getcwd()
    for (root, directories, files) in tqdm(os.walk(dir_name)):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.split('.')[-1]=='pdf':
                pdf_dir_list.append(file_path)
    return pdf_dir_list

if __name__ == '__main__':
    start = time.time()
    pdf_merger = PdfFileMerger(strict=False)
    pdf_dir_list = search_pdfs()
    pdf_dir_list = list(
        map(
            lambda x : x.replace(str("\\"),'/')
                                 ,pdf_dir_list)
        )

    for file_path in tqdm(pdf_dir_list[:110]):
        try:
            pdf_merger.append(PdfFileReader(open(file_path, 'rb')))
        except:
            print("Error merging {}".format(file_path))
            raise

    pdf_merger.write("Merged.pdf")
    pdf_merger.close()
    duration = time.time() - start
    print('Pdf Merging Is Done!')
    print('Work Time is %s Seconds' % (round(duration,3)))
    print('Merged Pdfs are as below')
    for x in pdf_dir_list:
        print(x)
