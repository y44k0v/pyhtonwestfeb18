
# --------------------------------------------------------------------------
# STUDENT'S TASK: Implement the calculate_bmi function below.
# DO NOT CHANGE the function signature (name and parameters).
# --------------------------------------------------------------------------

def calculate_bmi(weight_kg: int | float, height_m: int | float):
     if height_m <=0 or weight_kg < 0:
         return None
     else:
        bmi = weight_kg / (height_m ** 2)
        return float(bmi)
