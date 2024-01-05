def main():
    file_path = input("Enter the file path: ")
    process_file_input(file_path)

def process_file_input(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                t, h, w = map(float, line.split())
                process_input(t, h, w)
    except FileNotFoundError:
        print("File not found. Exiting.")

def process_input(t, h, w):
    W = 0.5 * t**2 - 0.2 * h - 0.1 * w - 15
    print(W)

    if W > 300:
        print("Sunny")
    elif 200 < W <= 300:
        print("Cloudy")
    elif 100 < W <= 200:
        print("Rainy")
    else:
        print("Stormy")

if _name_ == "_main_":
    main()