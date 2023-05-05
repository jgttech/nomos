system_base_dir = "export __SYSTEM_BASE_DIR=\".nomos\""
system_source_dir = lambda filename: f"source \"${{HOME}}/${{__SYSTEM_BASE_DIR}}/shell/{filename[1:]}.sh\""

# A list of the shell files we want to detect.
shells = [
    ".zshrc",
    ".bashrc",
]
