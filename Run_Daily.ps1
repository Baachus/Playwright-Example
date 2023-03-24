# Set the path to the virtual environment activate script
$activateScript = "c:/Users/Baachus/Desktop/Files/Automation/Playwright - Example/sandbox-env/Scripts/Activate.ps1"

# Activate the virtual environment
& $activateScript

# Run pytest
pytest -k "bing"