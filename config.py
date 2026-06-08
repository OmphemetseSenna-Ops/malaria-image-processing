import os
from dotenv import load_dotenv

load_dotenv()

# Get the base directory for this project.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def resolve_path(env_key: str, default: str) -> str:
    # Resolve an env path to an absolute path relative to BASE_DIR.
    value = os.getenv(env_key, default)
    if not value:
        raise ValueError(f"Environment variable {env_key} is required")
    return value if os.path.isabs(value) else os.path.abspath(os.path.join(BASE_DIR, value))


# Base dataset folder for clean dataset sources.
DATASETS_BASE = resolve_path("DATASETS_BASE", "clean datasets")

# Destination paths for clean dataset outputs.
THICK_FINAL_IMAGES = resolve_path("THICK_FINAL_IMAGES", os.path.join(DATASETS_BASE, "Thick_FINAL", "images"))
THICK_FINAL_LABELS = resolve_path("THICK_FINAL_LABELS", os.path.join(DATASETS_BASE, "Thick_FINAL", "labels_yolo"))
THICK_CLEAN_IMAGES = resolve_path("THICK_CLEAN_IMAGES", os.path.join(DATASETS_BASE, "Thick_CLEAN", "images"))
THICK_CLEAN_LABELS = resolve_path("THICK_CLEAN_LABELS", os.path.join(DATASETS_BASE, "Thick_CLEAN", "labels_yolo"))
THIN_CLEAN_IMAGES = resolve_path("THIN_CLEAN_IMAGES", os.path.join(DATASETS_BASE, "Thin_Images", "images"))
THIN_CLEAN_LABELS = resolve_path("THIN_CLEAN_LABELS", os.path.join(DATASETS_BASE, "Thin_Images", "labels_yolo"))

DATASETS = {
    "thick_clean": {
        "images": THICK_CLEAN_IMAGES,
        "labels": THICK_CLEAN_LABELS,
    },
    "thin_clean": {
        "images": THIN_CLEAN_IMAGES,
        "labels": THIN_CLEAN_LABELS,
    },
    "thick_final": {
        "images": THICK_FINAL_IMAGES,
        "labels": THICK_FINAL_LABELS,
    },
}

VALIDATION_REPORT = os.getenv("VALIDATION_REPORT", "validation_report.txt")

IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png")

THIN_CLASSES = [
    "gametocyte",
    "trophozoite",
    "other stage",
    "white blood cell",
    "artefacts",
    "ring stage"
]