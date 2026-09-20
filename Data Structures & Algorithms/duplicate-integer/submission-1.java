class Solution {
    public boolean hasDuplicate(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            int pivote = nums[i]; // Declaración y asignación
            for (int j = i + 1; j < nums.length; j++) { // Evita comparar el mismo elemento
                if (pivote == nums[j]) {
                    return true;
                }
            }
        }
        return false;
    }
}

