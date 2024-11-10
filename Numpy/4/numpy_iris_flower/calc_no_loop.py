# coding: utf-8
import numpy as np
def calc_no_loop(new_points, points):
    # بازآرایی new_points به شکل (m, 1, f)
    new_points_reshaped = new_points[:, np.newaxis, :]
    
    # بازآرایی points به شکل (1, n, f)
    points_reshaped = points[np.newaxis, :, :]
    
    # محاسبه تفاوت‌ها، مجذورات و جمع کردن آن‌ها برای به دست آوردن فاصله‌ها
    distances = np.sum(np.square(new_points_reshaped - points_reshaped), axis=2)
    
    return distances
