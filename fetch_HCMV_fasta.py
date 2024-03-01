from Bio import SeqIO
from Bio import Entrez
import os

#define a function to fetch the transcriptome for a given accession ID
def get_transcriptome(accession_id):
    # Set the email for Entrez
    Entrez.email = 'wprice2@luc.edu' 
    
    # Fetch the sequence record in GenBank format from NCBI using the provided accession
    #ID
    genbank_handle = Entrez.efetch(db='nucleotide', id=accession_id, rettype='gb', retmode='text')
    #Parse the GenBank record using SeqIO to obtain a seqrecord object
    genbank_record = SeqIO.read(genbank_handle, 'gb')
    #Close the handle after fetching our record
    genbank_handle.close()
    
    # Write CDS features to a separate FASTA file
    # Initialize CDS count
    cds_count = 0  
    #Iterate through each feature in the GenBank record
    for feature in genbank_record.features:
        #Check to see if the feature type is 'CDS' and if it contains a 'translation' qualifier
        if feature.type == 'CDS' and 'translation' in feature.qualifiers:
            cds_count += 1  # Increment CDS count
    
    # Output CDS count to project log file
    log_filename = 'PipelineProject.log'
    with open(log_filename, 'a') as log_file:
        log_file.write(f"The HCMV genome ({accession_id}) has {cds_count} CDS\n")

#Call function
get_transcriptome('NC_006273.2')
