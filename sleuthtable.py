import pandas as pd

# Define samples, conditions, and the base path to Kallisto outputs
samples = ['SRR5660030', 'SRR5660033', 'SRR5660044', 'SRR5660045']
conditions = ['2dpi', '6dpi', '2dpi', '6dpi']  
base_path = "/home/wprice2/myrepo/"  

# Create a DataFrame with the necessary information
metadata = pd.DataFrame({
    'sample': samples,
    'condition': conditions,
    'path': [f"{base_path}/{sample}_results" for sample in samples]  
})

# Save the DataFrame to a CSV file
metadata.to_csv('metadata_for_sleuth.csv', index=False, sep='\t')

print("metadata_for_sleuth.csv has been created.")
