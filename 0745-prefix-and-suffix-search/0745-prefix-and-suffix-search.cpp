
class TrieNode {
public:
    std::vector<TrieNode*> children;
    int index;

    TrieNode() : children(27, nullptr), index(-1) {}
};

class Trie {
public:
    TrieNode* root;

    Trie() {
        root = new TrieNode();
    }

    void insertWord(const std::string& word, int index) {
        for (int i = 0; i < word.length(); ++i) {
            std::string toBeInserted = word.substr(i) + "{" + word;
            TrieNode* current = root;

            for (int j = 0; j < toBeInserted.length(); ++j) {
                int diff = toBeInserted[j] - 'a';

                if (!current->children[diff]) {
                    current->children[diff] = new TrieNode();
                }

                current->children[diff]->index = std::max(current->children[diff]->index, index);
                current = current->children[diff];
            }
        }
    }

    int findIfPrefixAndSuffixExists(const std::string& prefix, const std::string& suffix) {
        std::string stringVer = suffix + "{" + prefix;
        TrieNode* current = root;

        for (int i = 0; i < stringVer.length(); ++i) {
            if (!current) {
                return -1;
            }

            int diff = stringVer[i] - 'a';
            current = current->children[diff];
        }

        if (!current) {
            return -1;
        }

        return current->index;
    }
};

class WordFilter {
public:
    Trie trie;

    WordFilter(std::vector<std::string>& words) {
        for (int i = 0; i < words.size(); ++i) {
            trie.insertWord(words[i], i);
        }
    }

    int f(const std::string& pref, const std::string& suff) {
        return trie.findIfPrefixAndSuffixExists(pref, suff);
    }
};
