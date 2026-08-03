class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        unordered_map<int, int> refMap;

        for (int i = 0; i < n; i++) {
            int diff = target - nums[i];

            if (refMap.find(diff) != refMap.end()) {
                return {refMap[diff], i};
            }
            refMap.insert({nums[i], i});
        }
        return {};
    }
};
