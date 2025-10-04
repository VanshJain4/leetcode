class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int count = numBottles;
        int empty = numBottles;
        while (empty >= numExchange) {
            numBottles = empty / numExchange;
            count += numBottles;
            empty = empty % numExchange + numBottles;
        }

        return count;
    }
};