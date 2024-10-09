#!/bin/bash

# Create the necessary directories within the existing backend folder
mkdir -p app/routers
mkdir -p alembic/versions

# Create empty Python files in the appropriate locations
touch app/__init__.py
touch app/main.py
touch app/models.py
touch app/database.py
touch app/schemas.py
touch app/crud.py
touch app/utils.py

# Create the router files
touch app/routers/enquiry.py
touch app/routers/designer.py
touch app/routers/order.py
touch app/routers/raw_material.py
touch app/routers/process.py

# Create Alembic versions directory for migrations (optional)
touch alembic/versions/.gitkeep  # .gitkeep is a placeholder to ensure the folder is tracked

# Create the requirements.txt file for dependencies
touch requirements.txt

# Output the directory structure to confirm
echo "Directory structure created successfully!"
tree .