import joblib

model = joblib.load("D:\Work_USA\Projects\lab-report-automation\src\ckd_model.pkl")

print("✅ Model loaded successfully!")
print("Model type:", type(model))
print("Feature importances:")
for name, imp in zip(model.feature_names_in_, model.feature_importances_):
    print(f"{name}: {imp:.4f}")
