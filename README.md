# Malaria Image Processing
A comprehensive image analysis and pre-processing pipeline for malaria microscopy detection. This project processes microscopy images with bounding box annotations in YOLO format to analyze parasite detection patterns and provide insights for model training optimization.

## Project Overview
- **Purpose**: Analyze and prepare malaria microscopy datasets for object detection (YOLO)
- **Input**: Images + YOLO-format bounding box annotations
- **Output**: Dataset statistics, quality metrics, training recommendations
- **Datasets**: Thick blood smear and thin blood smear preparations

## Current Analysis Results

### Dataset Summary

#### Thick Clean Dataset
- **Total Images**: 3,043
- **Total Valid Objects**: 377,058
- **Invalid Entries**: 108 (0.03%) — automatically filtered
- **Files with Invalid Entries**: 89
- **Average Objects per Image**: 123.91 (range: 1–628)

**Bounding Box Statistics:**
- **Width**: Min 0.00024, Max 0.23912, Avg 0.01750
- **Height**: Min 0.00047, Max 0.27652, Avg 0.01491
- **Area**: Min ~0.000000, Max 0.059905, Avg 0.000310
- **Size Distribution**: Tiny 362,155 (96.0%), Medium 14,775 (3.9%), Large 128 (0.04%)

#### Thin Clean Dataset
- **Total Images**: 1,012
- **Total Valid Objects**: 43,449
- **Invalid Entries**: 10 (0.02%) — automatically filtered
- **Files with Invalid Entries**: 10
- **Average Objects per Image**: 42.98 (range: 1–271)

**Bounding Box Statistics:**
- **Width**: Min 0.00044, Max 0.17845, Avg 0.01627
- **Height**: Min 0.00033, Max 0.17318, Avg 0.01268
- **Area**: Min ~0.000000, Max 0.025939, Avg 0.000279
- **Size Distribution**: Tiny 41,904 (96.4%), Medium 1,515 (3.5%), Large 30 (0.07%)

### Data Quality Assessment

**Excellent** — < 0.03% corruption rate across both datasets
- Invalid entries are filtered automatically
- Minimal data quality issues
- Ready for training with standard preprocessing

### Training Recommendations
1. **Use High Resolution**: Train with `imgsz=1280` (default 640 may miss tiny objects)
2. **Small-Object Optimization**: Enable small-object detection settings
3. **Augmentation**: Leverage mosaic augmentation and small-object augmentation
4. **Confidence Threshold**: Lower confidence threshold (0.25) for small parasites
5. **Optional Tiling**: For advanced training, consider 640×640 patch extraction from full images


Analyzes both `thick_clean` and `thin_clean` datasets, reporting:
- Data quality metrics
- Box size statistics (width, height, area)
- Distribution of object sizes
- Training recommendations

## Dependencies

- Python 3.8+
- python-dotenv
- Statistics (stdlib)

## Installation

```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows
pip install python-dotenv
```

## Configuration

Create/update `.env` with dataset paths:
```env
DATASETS_BASE=clean datasets
THICK_FINAL_IMAGES=clean datasets/Thick_FINAL/images
THICK_FINAL_LABELS=clean datasets/Thick_FINAL/labels_yolo
THICK_CLEAN_IMAGES=clean datasets/Thick_CLEAN/images
THICK_CLEAN_LABELS=clean datasets/Thick_CLEAN/labels_yolo
THIN_CLEAN_IMAGES=clean datasets/Thin_Images/images
THIN_CLEAN_LABELS=clean datasets/Thin_Images/labels_yolo
VALIDATION_REPORT=validation_report.txt
```

## Notes
- Invalid bounding boxes (zero/negative dimensions) are automatically filtered during analysis
- Tiny objects dominate both datasets (96%+), requiring high-resolution model training
- Datasets are excluded from git via `.gitignore` to reduce repository size
