from step_001_bbox_analysis import analyze_bounding_boxes
from statistics import mean

def main():
    print("Starting image-processing pipeline")

    analyze_bounding_boxes()

    print("Pipeline completed")


if __name__ == "__main__":
    main()