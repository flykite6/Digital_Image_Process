import cv2
from numpy import zeros,median,uint8,float

def median_filter(img, K_size=3):
    H, W, C = img.shape
    if img.shape[2] == 4:
        img = cv2.cvtColor(img,cv2.COLOR_RGBA2BGR)
    # 填充0
    pad = K_size // 2
    out = zeros((H + pad*2, W + pad*2, C), dtype=float)
    out[pad:pad+H, pad:pad+W] = img.copy().astype(float)

    tmp = out.copy()

    # filtering
    for y in range(H):
        for x in range(W):
            for c in range(C):
                out[pad+y, pad+x, c] = median(tmp[y:y+K_size, x:x+K_size, c])

    out = out[pad:pad+H, pad:pad+W].astype(uint8)

    return out