import os
import math
RESET = "\033[0m"
VGA_COLORS_INFO = {
    0: "Dark Black", 1: "Dark Red", 2: "Dark Green", 3: "Brown",
    4: "Dark Blue", 5: "Dark Magenta", 6: "Dark Cyan", 7: "Light Gray",
    8: "Dark Gray", 9: "Bright Red", 10: "Bright Green", 11: "Bright Yellow",
    12: "Bright Blue", 13: "Bright Magenta", 14: "Bright Cyan", 15: "Bright White",
}
def get_256_color_ansi(index, is_background=False):
    code = 48 if is_background else 38
    return f"\033[{code};5;{index}m"
def print_color_palette():
    HEADER_WIDTH = 12
    print("Color Index | Color Type          | Swatch")
    print("-" * 60)
    for i in range(128):
        fg_code = get_256_color_ansi(i)
        bg_code = get_256_color_ansi(i, is_background=True)
        if i < 16:
            color_type = f"VGA ({VGA_COLORS_INFO.get(i)})"
            text_color = "\033[30m" if i in (3, 7, 11, 15) else "\033[37m"
        else:
            color_type = "Cube"
            if i > 23: 
                text_color = "\033[30m" 
            else:
                text_color = "\033[37m" 
        swatch_text = f"Color {i:03d} (FG)"
        fg_swatch = f"{fg_code}\033[47m{swatch_text:<15}{RESET}"
        bg_swatch_text = f"Color {i:03d} (BG)"
        bg_swatch = f"{bg_code}{text_color}{bg_swatch_text:<15}{RESET}"
        print(f"{i:<11} | {color_type:<19} | {fg_swatch} {bg_swatch}")
if __name__ == '__main__':
    print_color_palette()