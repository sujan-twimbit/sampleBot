import os
def traverse_and_process(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.html'):
                pdf_path = os.path.join(root, file)
                metadata = {
                    "path": pdf_path.replace(directory, "")
                }
                print(metadata)

traverse_and_process("/Users/sujanmidatani/Desktop/projects/“aicb”")
            
