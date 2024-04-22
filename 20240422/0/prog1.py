def sqroots(coeffs: str) -> str:
	try:
		a, b, c = map(float, coeffs.split())
		test = b / a

		d = b ** 2 - 4 * a * c
		if d < 0:
			return ""
		if d == 0:
			return str(-b / (2 * a))

		d = d ** 0.5
		return str((-b - d) / (2 * a)) + ' ' + str((-b + d) / (2 * a))
	except Exception:
		return "Incorrect input."
