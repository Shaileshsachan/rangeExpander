import unittest
from src.expand_ranges import expand_ranges

class TestRangeExpander(unittest.TestCase):

    def test_single_range(self):
        self.assertEqual(expand_ranges("1-3"), [1, 2, 3])
    
    def test_single_number(self):
        self.assertEqual(expand_ranges("5"), [5])

    def test_mixed_range_and_number(self):
        self.assertEqual(expand_ranges("1-2,4"), [1, 2, 4])
    
    def test_complex_case(self):
        self.assertEqual(expand_ranges("1-3,5,7-9"), [1, 2, 3, 5, 7, 8, 9])

    # Stage 2 tests
    def test_repeated_range(self):
        self.assertEqual(expand_ranges("1-2*3"), [1, 2, 1, 2, 1, 2])

    def test_repeated_single_number(self):
        self.assertEqual(expand_ranges("5*2"), [5, 5])

    def test_mixed_repeated_and_normal(self):
        self.assertEqual(expand_ranges("1-3*2,4"), [1, 2, 3, 1, 2, 3, 4])

    def test_multiple_repeats(self):
        self.assertEqual(expand_ranges("1-2,3-4*2"), [1, 2, 3, 4, 3, 4])

    def test_single_number_repeat(self):
        self.assertEqual(expand_ranges("1*4"), [1, 1, 1, 1])

    # Stage 3 tests
    def test_descending_range(self):
        self.assertEqual(expand_ranges("5-2"), [5, 4, 3, 2])

    def test_mixed_ascending_and_descending(self):
        self.assertEqual(expand_ranges("1-3,5-2"), [1, 2, 3, 5, 4, 3, 2])

    def test_same_start_and_end(self):
        self.assertEqual(expand_ranges("3-3"), [3])

    def test_repeated_descending_range(self):
        self.assertEqual(expand_ranges("5-3*2"), [5, 4, 3, 5, 4, 3])

    def test_combined_repeat_and_reverse(self):
        self.assertEqual(expand_ranges("1-2*2,5-3*2"), [1, 2, 1, 2, 5, 4, 3, 5, 4, 3])

    # Stage 4 tests
    def test_flatten_and_sort(self):
        self.assertEqual(
            expand_ranges("1,3-5,7-2,10", unique_sorted_output=True),
            [1, 2, 3, 4, 5, 6, 7, 10]
        )

    def test_overlapping_ranges(self):
        self.assertEqual(expand_ranges("1-3,2-4", unique_sorted_output=True), [1, 2, 3, 4])

    def test_duplicate_numbers(self):
        self.assertEqual(expand_ranges("5,3,5,3", unique_sorted_output=True), [3, 5])

    def test_repeat_with_overlap(self):
        self.assertEqual(expand_ranges("1-2*2,2-1*2", unique_sorted_output=True), [1, 2])

    #stage5
    def test_step_values_ascending(self):
        self.assertEqual(expand_ranges("1-10:2"), [1, 3, 5, 7, 9])

    def test_step_values_descending(self):
        self.assertEqual(expand_ranges("10-1:3"), [10, 7, 4, 1])

    def test_step_with_custom_delimiters(self):
        self.assertEqual(expand_ranges("1..5:2", range_delimiters=[".."]), [1, 3, 5])

    def test_overlapping_ranges_deduplicated(self):
        self.assertEqual(
            expand_ranges("1-3,2-5", unique_sorted_output=True),
            [1, 2, 3, 4, 5]
        )

    def test_duplicate_numbers_merged(self):
        self.assertEqual(
            expand_ranges("2,2,2-2", unique_sorted_output=True),
            [2]
        )

    def test_overlapping_range_edges(self):
        self.assertEqual(
            expand_ranges("1-2,2-3", unique_sorted_output=True),
            [1, 2, 3]
        )

    #stage 7
    def test_output_as_list(self):
        self.assertEqual(
            expand_ranges("1-3", output_format="list"),
            [1, 2, 3]
        )

    def test_output_as_csv(self):
        self.assertEqual(
            expand_ranges("1-3", output_format="csv"),
            "1,2,3"
        )

    def test_output_as_set(self):
        self.assertEqual(
            expand_ranges("1-3", output_format="set"),
            {1, 2, 3}
        )

    def test_invalid_output_format(self):
        with self.assertRaises(ValueError):
            expand_ranges("1-3", output_format="html")


if __name__ == "__main__":
    unittest.main()
