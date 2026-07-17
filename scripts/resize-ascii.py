import sys

# Baca input
lines = sys.stdin.read().splitlines()

# Hapus baris kosong di awal/akhir
while lines and not lines[0].strip():
    lines.pop(0)
while lines and not lines[-1].strip():
    lines.pop()

original_height = len(lines)
original_width = max(len(line) for line in lines)

# Target ukuran untuk desktop (max 64 baris, 96 kolom)
target_height = 62
target_width = 94

# Hitung skala
scale_y = min(1.0, target_height / original_height)
scale_x = min(1.0, target_width / original_width)
scale = min(scale_x, scale_y)

new_height = int(original_height * scale)
new_width = int(original_width * scale)

# Resize dengan sampling
result = []
for y in range(new_height):
    row = []
    for x in range(new_width):
        src_y = min(int(y / scale), original_height - 1)
        src_x = min(int(x / scale), len(lines[src_y]) - 1) if lines[src_y] else 0
        row.append(lines[src_y][src_x] if src_x < len(lines[src_y]) else ' ')
    result.append(''.join(row))

# Output
for line in result:
    print(line)

# Print stats to stderr
print(f"\nResized: {original_width}x{original_height} → {new_width}x{new_height}", file=sys.stderr)
