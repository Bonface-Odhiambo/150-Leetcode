class Solution {
    merge(nums1, m, nums2, n) {
        // Initialize pointers
        let p1 = m - 1; // Last valid element in nums1
        let p2 = n - 1; // Last element in nums2
        let p = m + n - 1; // Last position in nums1

        // Merge nums1 and nums2 from the back
        while (p1 >= 0 && p2 >= 0) {
            if (nums1[p1] > nums2[p2]) {
                nums1[p] = nums1[p1];
                p1--;
            } else {
                nums1[p] = nums2[p2];
                p2--;
            }
            p--;
        }

        // Add remaining elements from nums2, if any
        while (p2 >= 0) {
            nums1[p] = nums2[p2];
            p2--;
            p--;
        }

        // Print the merged array
        console.log(nums1);
    }
}

// Example usage:
const nums1 = [1, 2, 3, 0, 0, 0];
const m = 3;
const nums2 = [2, 5, 6];
const n = 3;

const solution = new Solution();
solution.merge(nums1, m, nums2, n);
// Output: [1, 2, 2, 3, 5, 6]
