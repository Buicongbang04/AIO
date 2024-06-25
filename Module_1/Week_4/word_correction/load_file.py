def load_file(file_path: str):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        data = sorted(set([line.strip().lower() for line in lines]))
        f.close()
    return data
