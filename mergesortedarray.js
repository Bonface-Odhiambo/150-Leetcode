var merge = function (nums1, m, nums2, n) {
    // Initialize pointers
    let p1 = m - 1; // Pointer for the last element in nums1's initial portion
    let p2 = n - 1; // Pointer for the last element in nums2
    let p = m + n - 1; // Pointer for the last position in nums1

    // Merge nums1 and nums2 starting from the end
    while (p1 >= 0 && p2 >= 0) {
        if (nums1[p1] > nums2[p2]) {
            nums1[p] = nums1[p1];
            p1--;
        } else {
            nums1[p] = nums2[p2];
            p2--;
        }
        p--; // Move the pointer for nums1
    }

    // If any elements remain in nums2, copy them to nums1
    while (p2 >= 0) {
        nums1[p] = nums2[p2];
        p2--;
        p--;
    }
};
