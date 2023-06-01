import decimal as decimal


def solve(coefficients, interval, resolution=10e-2, tolerance=10e-6, threshold=10e-3):
    def polynomial(x):
        total = 0
        for i in range(len(coefficients)):
            total += coefficients[i] * x**i

        return total

    def polynomial_deriv(x):
        total = 0
        for i in range(1, len(coefficients)):
            total += i * coefficients[i] * x**(i-1)

        return total

    sign_check = lambda x: -1 if x < 0 else 1
    n_sigfigs = abs(decimal.Decimal(str(tolerance)).as_tuple().exponent)
    coefficients = [float(s) for s in coefficients.split()]
    interval = [float(s) for s in interval.split()]
    # Breaking the interval into sub-intervals
    sub_interval_edges = []
    if abs(interval[1] - interval[0]) < resolution:
        sub_interval_edges = interval
    else:
        edge = interval[0]
        sub_interval_edges.append(edge)
        while edge < interval[1]:
            edge += resolution
            sub_interval_edges.append(edge)

        sub_interval_edges.append(interval[1])

    roots = []
    # Checking for odd roots
    for i in range(len(sub_interval_edges) - 1):
        left_edge = sub_interval_edges[i]
        right_edge = sub_interval_edges[i+1]
        if sign_check(polynomial(left_edge)) == sign_check(polynomial(right_edge)):
            continue
        else:
            while True:
                x = (right_edge + left_edge)/2
                if (polynomial(right_edge)*polynomial(x)) > 0:
                    right_edge = x
                else:
                    left_edge = x

                if abs(right_edge - left_edge) < tolerance:
                    if abs(polynomial(x)) < threshold:
                        roots.append(float((f'% .{n_sigfigs+1}f' % x)[0:-1]))

                    break

    # Checking for even roots
    for i in range(len(sub_interval_edges) - 1):
        left_edge = sub_interval_edges[i]
        right_edge = sub_interval_edges[i + 1]
        if sign_check(polynomial_deriv(left_edge)) == sign_check(polynomial_deriv(right_edge)):
            continue
        else:
            while True:
                x = (right_edge + left_edge) / 2
                if (polynomial_deriv(right_edge) * polynomial_deriv(x)) > 0:
                    right_edge = x
                else:
                    left_edge = x

                if abs(right_edge - left_edge) < tolerance:
                    if abs(polynomial_deriv(x)) < threshold:
                        if abs(polynomial(x)) < threshold:
                            roots.append(float((f'% .{n_sigfigs+1}f' % x)[0:-1]))

                    break

    return roots


if __name__ == '__main__':

    done = False
    while not done:
        coefficients = input('Enter the polynomial coefficients:\n')
        interval = input('Enter the interval:\n')
        roots = solve(coefficients, interval)
        if roots:
            for root in roots:
                print(f'Root found at {root}.')
        else:
            print('No roots are found!')
        answer = input('Do you want to continue? [Y/N]\n').upper()
        if answer != 'Y':
            done = True