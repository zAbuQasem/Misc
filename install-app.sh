#!/bin/bash

# Written by zAbuQasem

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

if ! command -v desktop-file-install &> /dev/null; then
    echo -e "${RED}Error: desktop-file-install not found. Please install desktop-file-utils.${NC}"
    exit 1
fi

display_help() {
    echo -e "${YELLOW}Usage:${NC} $0 ${GREEN}-n|--name <app_name> -e|--exec <exec_path> [-i|--icon <icon_path>]${NC}"
    echo "Options:"
    echo "  -n, --name     : Application name (required)"
    echo "  -e, --exec     : Executable path (required)"
    echo "  -i, --icon     : Icon path (optional)"
    echo "  -h, --help     : Display this help menu"
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        -n|--name)
            APP_NAME="$2"
            shift 2
            ;;
        -e|--exec)
            EXEC_PATH="$2"
            shift 2
            ;;
        -i|--icon)
            ICON_PATH="$2"
            shift 2
            ;;
        -h|--help)
            display_help
            exit 0
            ;;
        *)
            echo -e "${RED}Unknown option: $1${NC}"
            display_help
            exit 1
            ;;
    esac
done

if [ -z "$APP_NAME" ] || [ -z "$EXEC_PATH" ]; then
    echo -e "${RED}Error: Application name and executable path are required.${NC}"
    display_help
    exit 1
fi

if [ -z "$ICON_PATH" ]; then
    ICON_PATH=""
fi

DESKTOP_ENTRY_FILE="$HOME/.local/share/applications/$APP_NAME.desktop"

echo -e "[Desktop Entry]" > "$DESKTOP_ENTRY_FILE"
echo -e "Name=$APP_NAME" >> "$DESKTOP_ENTRY_FILE"
echo -e "Exec=$EXEC_PATH" >> "$DESKTOP_ENTRY_FILE"
echo -e "Icon=$ICON_PATH" >> "$DESKTOP_ENTRY_FILE"
echo -e "Type=Application" >> "$DESKTOP_ENTRY_FILE"
echo -e "Categories=Utility;" >> "$DESKTOP_ENTRY_FILE"

desktop-file-install --dir="$HOME/.local/share/applications" "$DESKTOP_ENTRY_FILE"

echo -e "${GREEN}${APP_NAME} added to the application menu.${NC}"
