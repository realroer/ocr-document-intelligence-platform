from batch_processor import process_new_json_files


def main() -> None:
    """Run the OCR Document Intelligence batch pipeline."""
    process_new_json_files()


if __name__ == "__main__":
    main()
