
def toDEG(dms: str | float) -> float:
  if type(dms) is str:
    if dms.endswith('E') or dms.endswith('N'):
      dms = dms[:-1]
    
    dms = float(dms)

  s = dms % 100
  m = round((dms / 100) % 100, 0)
  h = round(dms / 10000, 0)

  deg = h + (m / 60) + (s / 3600)

  return deg
