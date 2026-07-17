import sys

x_offset = 78
y_start = 90.00
line_height = 6.65

lines = sys.stdin.read().splitlines()

# Hapus baris statistik
clean_lines = [l for l in lines if not l.startswith("Resized:")]

for i, line in enumerate(clean_lines):
    y = y_start + i * line_height
    # Escape XML
    escaped = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
    print(f'<tspan x="{x_offset}" y="{y:.2f}" xml:space="preserve">{escaped}</tspan>')
