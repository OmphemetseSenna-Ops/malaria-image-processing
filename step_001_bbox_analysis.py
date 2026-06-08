import os
from statistics import mean
from config import DATASETS

def analyze_bounding_boxes(dataset_name):
    if dataset_name not in DATASETS:
        print(f"Unknown dataset: {dataset_name}")
        return

    label_dir = DATASETS[dataset_name]["labels"]

    print(f"\nBounding Box Analysis - {dataset_name}")
    print("=" * 60)

    if not os.path.isdir(label_dir):
        print(f"Labels directory does not exist: {label_dir}")
        return

    widths, heights, areas, objects_per_image = [], [], [], []
    tiny, medium, large = 0, 0, 0
    invalid_entries = 0
    files_with_invalid = set()

    label_files = [f for f in os.listdir(label_dir) if f.endswith(".txt")]
    if not label_files:
        print(f"No label files found in {label_dir}")
        return

    for file in label_files:
        path = os.path.join(label_dir, file)
        with open(path, "r") as f:
            lines = f.readlines()

        count = 0
        for line in lines:
            parts = line.strip().split()
            if len(parts) != 5:
                continue

            w, h = float(parts[3]), float(parts[4])
            
            # Skip invalid boxes - zero or negative dimensions
            if w <= 0 or h <= 0:
                invalid_entries += 1
                files_with_invalid.add(file)
                continue
            
            a = w * h
            widths.append(w); heights.append(h); areas.append(a)
            count += 1

            if a < 0.001: tiny += 1
            elif a < 0.01: medium += 1
            else: large += 1

        objects_per_image.append(count)

    total = len(areas)

    # Data quality report
    print(f"\nData Quality")
    print(f"Valid objects: {total:,}")
    print(f"Invalid objects (zero/negative dims): {invalid_entries:,}")
    print(f"Files with invalid entries: {len(files_with_invalid):,}")
    if invalid_entries > 0:
        invalid_pct = (invalid_entries / (total + invalid_entries)) * 100
        print(f"Invalid %: {invalid_pct:.2f}%")

    # Stats
    if not widths:
        print("\nNo valid bounding box data found after filtering.")
        return

    print("\nWidth Stats")
    print(f"Min: {min(widths):.5f}, Max: {max(widths):.5f}, Avg: {mean(widths):.5f}")
    print("\nHeight Stats")
    print(f"Min: {min(heights):.5f}, Max: {max(heights):.5f}, Avg: {mean(heights):.5f}")
    print("\nArea Stats")
    print(f"Min: {min(areas):.6f}, Max: {max(areas):.6f}, Avg: {mean(areas):.6f}")

    # Size distribution
    print("\nBounding Box Sizes")
    print(f"Tiny: {tiny:,}, Medium: {medium:,}, Large: {large:,}")

    # Object density
    print("\nObjects Per Image (excluding empty files)")
    valid_images = [c for c in objects_per_image if c > 0]
    if valid_images:
        print(f"Min: {min(valid_images)}, Max: {max(valid_images)}, Avg: {mean(valid_images):.2f}")
    else:
        print("No images with valid objects")

    # Recommendation
    tiny_pct = (tiny / total) * 100 if total else 0
    print("\nRecommendation")
    if tiny_pct > 50:
        recs = [
            "Majority tiny objects detected",
            "Use high resolution (1024–1280)",
            "Cropping/Tiling recommended",
            "Small-object YOLO settings"
        ]
    else:
        recs = ["Standard object training possible"]

    for r in recs:
        print("-", r)

    print("\nAnalysis complete")

def run():
    analyze_bounding_boxes("thick_clean")
    analyze_bounding_boxes("thin_clean")

if __name__ == "__main__":
    run()
