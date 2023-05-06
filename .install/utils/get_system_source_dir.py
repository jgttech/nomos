def get_system_source_dir(filename: str) -> str:
    return f"source \"${{HOME}}/${{__SYSTEM_BASE_DIR}}/shell/{filename[1:]}.sh\""
