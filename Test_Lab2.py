import Lab2
import statistics

print("Test_Lab2")

def test_find_min_max():
    minmax_array = [12.7, 69.0, 38]
    test_array = [12.7, 69.0]
    result = Lab2.calc_min_max_temperature(minmax_array)
    assert (result == test_array)

def test_calc_average():
    average_array = [12, 69, 38]
    result = Lab2.calc_average_temperature(average_array)
    assert (result == (12+69+38)/3)

def test_calc_median_temperature():
    median_array = [12, 69, 38]
    result = Lab2.calc_median_temperature(median_array)
    assert (result == statistics.median(median_array))
