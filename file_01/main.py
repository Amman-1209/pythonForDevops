from file_utils import check_files

def main():
    with open("check_list.txt", 'r') as file:
        paths= file.readlines()
    for path in paths:
        check_files(path.strip())
if __name__ == "__main__":
    main()
