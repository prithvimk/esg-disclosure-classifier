from pathlib import Path

# Base project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Data directories
DATA_DIR = BASE_DIR / "data"
UPLOADS = DATA_DIR / "uploads"

# Metadata files
METADATA_FILE = DATA_DIR / "metadata-sample.xlsx"
EXTRACTION_LOG = DATA_DIR / "extraction_log.log"

# Output (graph DB exports, embeddings, etc.)
GRAPH_EXPORTS_DIR = DATA_DIR / "graph_exports"
EMBEDDINGS_DIR = DATA_DIR / "embeddings"

# Config files
CONFIG_DIR = BASE_DIR / "config"