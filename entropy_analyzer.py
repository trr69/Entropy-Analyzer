import argparse
import math
import os

def file_entropy(file_path):
    with open(file_path, 'rb') as f:
        byte_counts = [0] * 256
        total_bytes = 0
        for byte in f.read():
            byte_counts[byte] += 1
            total_bytes += 1
    
    entropy = 0
    for count in byte_counts:
        if count == 0:
            continue
        probability = count / total_bytes
        entropy -= probability * math.log2(probability)
    
    return entropy

def classify_entropy(entropy):
    if entropy > 7:
        return "High"
    elif entropy > 6:
        return "Moderate"
    else:
        return "Low"

def main():
    parser = argparse.ArgumentParser(description='Calculate entropy of a file')
    parser.add_argument('file_path', help='Path to the file')
    args = parser.parse_args()

    file_size = os.path.getsize(args.file_path)
    processed_bytes = 0

    print("Processing file...")

    with open(args.file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            processed_bytes += len(chunk)
            entropy = file_entropy(args.file_path)
            percent_done = (processed_bytes / file_size) * 100
            print(f'Processing: {percent_done:.2f}% complete, Entropy: {entropy:.2f} bits', end='\r')

    print("\nDone.")

    final_entropy = file_entropy(args.file_path)
    entropy_class = classify_entropy(final_entropy)
    print(f"Final entropy classification: {entropy_class}")

if __name__ == "__main__":
    main()
