coeff = {
    'L': {
        'T': {
            'low': ((-200, 0), (2.76610203e-04,  6.33712901e-02,  6.37015450e-05,  1.92258094e-08,  1.55574603e-09,  1.23173389e-11,  5.87565838e-14,  1.48328819e-16, 1.49251986e-19)),
            'high': ((0, 800), (-1.40098253e-04, 6.33198398e-02, 5.99633047e-05, -7.82928338e-08, 8.83859264e-11, -1.36314288e-14, -2.79152675e-16, 4.52592512e-19, -2.14300492e-22))
        },
        'mV': {
            'low': ((-9.488, 0), (-1.12221876e-02, 1.57119487e+01, -3.99136006e-01, -1.26179615e-01, -6.19907084e-02, -1.51642779e-02, -2.14107447e-03, -1.59203047e-04, -4.96908012e-06)),
            'high': ((0, 66.466), (3.63846069e-02,  1.57370869e+01,  -2.13391881e-01,  7.63561103e-03,  -2.22074808e-04,  4.48762988e-06,  -5.36847673e-08,  3.25609022e-10, -7.08470842e-13))
        }
    },
    'K': {
        'T': {
            'low': ((-270, 0), (0, 3.9450128025e-2, 2.3622373598e-5, -3.2858906784e-7, -4.9904828777e-9, -6.7509059173e-11, -5.7410327428e-13, -3.1088872894e-15 ,-1.0451609365e-17, -1.9889266878e-20, -1.6322697486e-23)),
            'med': ((0, 500), (-0.0024829685, 0.0400866641, -1.27081008e-05, 7.99831713e-07, -1.02599237e-08, 6.08722555e-11, -1.97487299e-13, 3.6312914e-16, -3.56617383e-19, 1.45724739e-22)),
            'high': ((500, 1372), (-1.7600413686e-2, 3.8921204975e-2, 1.8558770032e-5, -9.9457592874e-8, 3.1840945719e-10, -5.6072844889e-13, 5.6075059059e-16, -3.2020720003e-19, 9.7151147152e-23, -1.2104721275e-26))
        },
        'mV': {
            'low': ((-5.891, 0), (0, 3.9450128025e-2, 2.3622373598e-5, -3.2858906784e-7, -4.9904828777e-9, -6.7509059173e-11, -5.7410327428e-13, -3.1088872894e-15 ,-1.0451609365e-17, -1.9889266878e-20, -1.6322697486e-23)),
            'high': ((0, 20.644), (0, 3.9450128025e-2, 2.3622373598e-5, -3.2858906784e-7, -4.9904828777e-9, -6.7509059173e-11, -5.7410327428e-13, -3.1088872894e-15 ,-1.0451609365e-17, -1.9889266878e-20, -1.6322697486e-23))
        }
    }
}


if __name__ == "__main__":
    # print(coeff['L']['mV']['high'][1])
    # value = -9.48
    # print(sum([k * (value) ** n for n, k in enumerate(coeff['L']['mV']['low'][1])]))
    print(coeff['K']['T'])







