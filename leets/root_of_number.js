function root(x, n) {
  if(x === 0) return 0;
  
  let lower = 0;
  let higher = Math.max(1, x);
  let approx = (higher + lower)/2;
  
  while(approx - lower >= 0.001) {
    if(Math.pow(approx, n) > x) {
      higher = approx;
    } else if (Math.pow(approx, n) < x) {
      lower = approx;
    } else break;
    
    approx = (higher + lower)/2;
  }
  
  return approx;
}