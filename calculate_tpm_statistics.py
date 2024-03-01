#Import necessary libraries
import pandas as pd
import numpy as np

#List of samples and their conditions
samples = [("SRR5660030", "2dpi"), ("SRR5660033", "6dpi"), ("SRR5660044", "2dpi"), ("SRR5660045", "6dpi")]

#bse path where Kallisto output folders are located
base_path = "/home/wprice2/myrepo"  

#prepare the log file
log_file_path = "PipelineProject.log"
with open(log_file_path, "a") as log_file:
    #Write the header for the log file
    log_file.write("sample\tcondition\tmin_tpm\tmed_tpm\tmean_tpm\tmax_tpm\n")
    
    #Iterate over each sample and its corresponding condition
    for sample, condition in samples:
        # onstruct the file path to the abundance.tsv file for the current sample
        file_path = f"{base_path}/{sample}_results/abundance.tsv"
        
        #Load the abundance.tsv file into a pandas DataFrame
        df = pd.read_csv(file_path, sep='\t')
        
        #calculate statistics for the TPM values in the DataFrame
        min_tpm = df['tpm'].min()
        med_tpm = df['tpm'].median()
        mean_tpm = df['tpm'].mean()
        max_tpm = df['tpm'].max()
        
        #Write the calculated statistics for the current sample to the log file
        log_file.write(f"{sample}\t{condition}\t{min_tpm}\t{med_tpm}\t{mean_tpm}\t{max_tpm}\n")

#Print a message indicating that TPM statistics have been calculated and appended to the log file for debugging
#purposes
print("TPM statistics calculated and appended to the log file.")
