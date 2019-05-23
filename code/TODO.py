from os.path import isfile, join

from ._check_fastq_gzs import _check_fastq_gzs
from ._print_and_run_command import _print_and_run_command


def count_transcripts_using_kallisto_quant(
    fastq_gz_file_paths,
    fasta_gz_file_path,
    output_directory_path,
    n_bootstrap=0,
    fragment_length=180,
    fragment_length_standard_deviation=20,
    n_job=1,
    overwrite=False,
):

    _check_fastq_gzs(fastq_gz_file_paths)

    fasta_gz_kallisto_index_file_path = f"{fasta_gz_file_path}.ki"

    if not isfile(fasta_gz_kallisto_index_file_path):

        _print_and_run_command(
            f"kallisto index --index {fasta_gz_kallisto_index_file_path} {fasta_gz_file_path}"
        )

    abundance_file_path = join(output_directory_path, "abundance.tsv")

    if not overwrite and isfile(abundance_file_path):

        raise FileExistsError(abundance_file_path)

    if len(fastq_gz_file_paths) == 1:

        sample_argument = f"--single --fragment-length {fragment_length} --sd {fragment_length_standard_deviation} {fastq_gz_file_paths[0]}"

    elif len(fastq_gz_file_paths) == 2:

        sample_argument = " ".join(fastq_gz_file_paths)

    _print_and_run_command(
        f"kallisto quant --index {fasta_gz_kallisto_index_file_path} --output-dir {output_directory_path} --bootstrap-samples {n_bootstrap} --threads {n_job} {sample_argument}"
    )

    return output_directory_path
