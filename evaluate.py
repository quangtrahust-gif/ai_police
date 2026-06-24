from ultralytics import YOLO

model = YOLO('best.pt')
metrics = model.val(
    data='/home/quangtra/ai_police/custom_dataset/data.yaml',
    device='cpu',
    plots=False,          # Tắt vẽ biểu đồ
    save_json=False,      # Tắt lưu JSON
    save_txt=False        # Tắt lưu file txt
)

print(f"mAP50-95: {metrics.box.map:.4f}")
print(f"mAP50: {metrics.box.map50:.4f}")