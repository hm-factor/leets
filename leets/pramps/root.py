def root(x, n):
  if x == 0:
    return 0

  low = 0
  high = max(1, x)
  approx = (low + high)/2

  while ((approx - low) >= 0.001):
    temp = pow(approx, n)
    if temp > x:
      high = approx
    elif temp < x:
      low = approx
    else:
      break

    approx = (low + high)/2

  return approx
