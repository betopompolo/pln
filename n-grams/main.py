from dataset_parser import load_dataset

if __name__ == '__main__':
    count = 0
    for _ in load_dataset('folha94'):
        count += 1
    print(f'dataset has {count} files')
