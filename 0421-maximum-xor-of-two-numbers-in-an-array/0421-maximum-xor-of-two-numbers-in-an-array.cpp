
class TrieNode {
public:
    TrieNode() {
        children = std::vector<TrieNode*>(2, nullptr);
    }
    std::vector<TrieNode*> children;
};

class Trie {
public:
    Trie(int max_length) {
        root = new TrieNode();
        this->max_length = max_length;
    }

    int insert(int number) {
        TrieNode* my_pointer = root;
        TrieNode* opposite_pointer = root;
        int res = 0;

        for (int i = max_length - 1; i >= 0; i--) {
            int bit = (number >> i) & 1;

            if (!my_pointer->children[bit]) {
                my_pointer->children[bit] = new TrieNode();
            }

            if (opposite_pointer->children[1 - bit]) {
                opposite_pointer = opposite_pointer->children[1 - bit];
                res += (1 << i);
            } else {
                opposite_pointer = opposite_pointer->children[bit];
            }

            my_pointer = my_pointer->children[bit];
        }

        return res;
    }

private:
    TrieNode* root;
    int max_length;
};

class Solution {
public:
    int findMaximumXOR(std::vector<int>& nums) {
        int max_length = 32; // Assuming 32-bit integers
        Trie trie(max_length);
        int n = nums.size();
        int res = 0;

        for (int i = 0; i < n; i++) {
            res = std::max(res, trie.insert(nums[i]));
        }
        return res;
    }
};

