import math

def estimator(data):
  """
  - Opening rates: 12%
  - Paint loss: 5%
  - 1L paint cover 10m2
  """
  area = data["number_of_buildings"] * data["avg_area"] * data["avg_floors"] * (1-0.12)
  total_paint = (area * data["number_of_coats"] * (1+0.05)) / 10
  buckets = math.ceil(total_paint / 10)
  return f"You will need approximately **{buckets} buckets** (10L each) to paint the entire city."
