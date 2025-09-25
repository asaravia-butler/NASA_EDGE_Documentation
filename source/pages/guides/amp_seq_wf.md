# Process Amplicon Sequencing Data

## Login to NASA EDGE

1. Navigate to the NASA EDGE platform by going to [https://nasa-dev.edgebioinformatics.org/](https://nasa-dev.edgebioinformatics.org/)
2. Follow steps 2 - 5 of the {doc}`set_up#register-for-an-account-using-orcid` instructions to login to the NASA EDGE platform.
3. Once logged into the NASA EDGE platform, click on "AmpIllumina Pipeline" under "WORKFLOWS" in the side bar menu as shown below:

```{image} ../../_static/images/amp_seq_wf/select_ampIllumina_wf.png
:alt: Select AmpIllumina Pipeline workflow
:width: 800px

4. To process an amplicon sequencing dataset hosted on the [NASA Open Science Data Repository (OSDR)](https://osdr.nasa.gov/bio/repo/), follow the [Process an OSD dataset](#process-an-osd-dataset) instructions below.
5. To process a non-OSD dataset, such as your own data or a dataset shared on the NASA EDGE platform, follow the [Process a non-OSD dataset](#process-a-non-osd-dataset) instructions below.

## Process an OSD dataset

1. To process a dataset hosted on OSDR, navigate to the [OSDR repository](https://osdr.nasa.gov/bio/repo/) and search for the amplicon sequencing dataset you want to process using the free text search bar at the top of the page. Note the OSD number of the dataset you want to process as shown below:
   *Note: If you are unfamiliar with OSDR, visit the [OSDR Tutorials](https://osdr-tutorials.readthedocs.io/en/latest/) page to learn how to [Access Data in the Open Science Data Repository](https://osdr-tutorials.readthedocs.io/en/latest/pages/guides/access_osdr_data.html) and how to [Navigate an OSDR Study Page](https://osdr-tutorials.readthedocs.io/en/latest/pages/guides/navigate_an_osdr_study_page.html).* 

```{image} ../../_static/images/amp_seq_wf/find_OSD_dataset.png
:alt: Find the OSD dataset you want to process
:width: 800px

2. With the AmpIllumina Workflow selected in the NASA EDGE platform, type in a Project/Run Name for your project (required) and an optional Description, then under the "Parameters" section, select "Start with OSD or GLDS accession as input", and in the Accession text box, type in the OSD number you want to process as shown below:

```{image} ../../_static/images/amp_seq_wf/input_OSD_info_in_EDGE.png
:alt: Input the OSD information into the NASA EDGE platform
:width: 800px

3. Under the "Parameters" section, select the amplicon Target Region used for processing, which can be found on the OSD study page under Assay(s) -> Technology for the select dataset as shown below:
   *Note that some amplicon sequencing datasets on OSDR contain multiple sets of sequencing data, each with a different amplicon target region used, so be sure to select the target region you want to process on the NASA EDGE platform.*    

```{image} ../../_static/images/amp_seq_wf/OSD_amp_target_region.png
:alt: Select the amplicon Target Region on NASA EDGE to match the one used for the OSD dataset on OSDR
:width: 800px

4. All other parameters are set to default values but can be modified. If you are unsure what a specific parameter does, hover over the green "i" icon next to the parameter name for more information, as shown below. If you want to re-process an OSD dataset using the exact parameters that were used to generate the GeneLab processed data on the OSDR repository, the parameter values used can be found in the processing info directory on the OSD study page, which can be downloaded under Files -> GeneLab Processed Diversity Amplicon Files -> Processing Info -> \*processing_info.zip, as shown below.
   *Note that the parameters values in the example below were set to match what was used to generate the processed data for this dataset in the OSDR repository.*

```{image} ../../_static/images/amp_seq_wf/OSD_parameter_selection.png
:alt: Parameter selection on NASA EDGE and location of processing info on OSDR repository
:width: 800px

5. When you are satisfied with your parameter selection, click the "Submit" button at the bottom to submit your job to the processing queue.

6. To check the status of your submitted job, following the instructions in the {doc}`check_run_status` tutorial.

7. Once your job is complete, you can view and download all output files and visualizations by following the instructions in the [View and download output files](#view-and-download-output-files) section below.

## Process a non-OSD dataset

1. To process a dataset that is not hosted on OSDR, such as your own amplicon sequencing data, you'll first need to create a runsheet csv file that contains the metadata required for processing amplicon sequence datasets through the GeneLab amplicon Illumina sequencing data processing pipeline (AmpIllumina), as specified [here](https://github.com/nasa/GeneLab_AmpliconSeq_Workflow/blob/main/examples/runsheet/README.md).

2. To ensure the runsheet format is correct, it is recommended to download the example runsheet [PE_file.csv](https://github.com/nasa/GeneLab_AmpliconSeq_Workflow/blob/main/examples/runsheet/PE_file.csv) file for paired-end data or the [SE_file.csv](https://github.com/nasa/GeneLab_AmpliconSeq_Workflow/blob/main/examples/runsheet/SE_file.csv) file for single-end data from GitHub by clicking on the download link as shown below:

```{image} ../../_static/images/amp_seq_wf/download_runsheet.png
:alt: Download example runsheet csv file from GitHub
:width: 800px

3. Open the example runsheet on your local computer and fill in the metadata columns with your sample info. A description of what should be included in each column can be found on GitHub [here](https://github.com/nasa/GeneLab_AmpliconSeq_Workflow/tree/main/examples/runsheet#required-columns). An example of a completed runsheet csv file for a paired-end dataset is shown below:
   *Note: The "forward" and "reverse" (PE data only) columns should only include the forward and reverse fastq file names, respectively, for each respective sample. Make sure the sample, file, and group names do not contain any spaces or weird characters.*

```{image} ../../_static/images/amp_seq_wf/example_runsheeet.png
:alt: Completed example runsheet csv file for a paired-end dataset
:width: 800px

4. Save your completed runsheet as a csv file.

5. Upload your runsheet csv file and your forward and reverse (for PE datasets only) fastq files to the [NASA EDGE platform](https://nasa-dev.edgebioinformatics.org/) by following the {doc}`set_up#upload-data` instructions.

6. Once your runsheet and fastq files are successfully uploaded, navigate to the [AmpIllumina workflow](https://nasa-dev.edgebioinformatics.org/workflow/nasa) on the NASA EDGE platform and type in a Project/Run Name for your project (required) and an optional Description, then under the "Parameters" section, select "Start with a runsheet csv file as input", and for the "Runsheet CSV" parameter, select the runsheet csv file you uploaded in step 5 from the drop-down menu. Next, input the forward and reverse primer sequences used to amplify the amplicon that was sequenced in your dataset, as shown in the example below.
   *Note that the "Group Column" and "Sample Column" parameters will only need to be modified if you did not use the example runsheet csv file specified in steps 1 - 3 above.*

```{image} ../../_static/images/amp_seq_wf/input_runsheet_info.png
:alt: Input the non-OSD dataset information into the NASA EDGE platform
:width: 800px

7. Under the "Parameters" section, select the amplicon Target Region that was amplified and sequenced in the dataset you're processing. All other parameters are set to default values but can be modified. If you are unsure what a specific parameter does, hover over the green "i" icon next to the parameter name for more information, as shown below.

```{image} ../../_static/images/amp_seq_wf/runsheet_parameter_selection.png
:alt: Amplicon target region and parameter selection on NASA EDGE
:width: 800px
   
8. When you are satisfied with your parameter selection, click the "Submit" button at the bottom to submit your job to the processing queue.

9. To check the status of your submitted job, following the instructions in the {doc}`check_run_status` tutorial.

10. Once your job is complete, you can view and download all output files and visualizations by following the instructions in the [View and download output files](#view-and-download-output-files) section below. 

## View and download output files

coming soon...
