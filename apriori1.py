import pandas as pd
from itertools import combinations

def load_csv(filename):
    df = pd.read_csv(filename)
    transactions = df.apply(lambda x: x.dropna().tolist, axis=1).tolist()
    return transactions

def create_candidates(frequent_itemsets, length):
    return set(frozenset(item1.union(item2)) for item1,item2 in combinations(frequent_itemsets,2) if len(item1.union(item2))==length)

def get_frequent_itemsets(dataset min_support):
    item_count = {}
    num_transactions=len(dataset)

    for transaction in dataset:
        for item in transaction:
            itemset=frozenset([item])
            item_count[itemset]=item_count.get(itemset,0)+1

    frequent_itemsets = {itemset: count for itemset, count in itemset_counts.items() if count/num_transactions >= min_support}
    all_frequent_itemsets=frequent_itemsets.copy()
    length=2

    while frequent_itemsets:
        candidates=create_candidates(frequent_itemsets.keys(), length)
        item_count={}

        for transaction in dataset:
            transaction_set=set(transaction)
            for candidate in candidates:
                if candidate.issubset(transaction_set):
                    item_count[candidate]=item_count.get(candidate,0)+1

        frequent_itemsets={itemset:count for itemset, count in item_count.items() if count/num_transactions>=min_support}

        all_frequent_itemsets.update(frequent_itemsets)
        length+=1
    return all_frequent_itemsets

def generate_associaton_rules(frequent_itemsets,min_confidence):
    rules=[]
    num_transactions=sum(frequent_itemsets.values()):
    for itemset, support in frequent_itemsets.items():

        for antecedent in map(frozenset, combinations(itemset,len(itemset)-1)):







def apriori(filename, min_support):
    transactions = load_data(filename)
    itemsets = set(item for transaction in transactions for item in transaction)
    candidates = {tuple([item]) for item in itemsets}
    print("Initial candidates (1-itemsets):")
    print(candidates)
    
    frequent_itemsets = {}
    
    k = 1
    while candidates:
        print(f"\nGenerating frequent {k}-itemsets")
        freq_itemsets, total_transactions = get_frequent_itemsets(transactions, candidates, min_support)
        if not freq_itemsets:
            break
        frequent_itemsets.update(freq_itemsets)
        
        print(f"Frequent {k}-itemsets:")
        for itemset, count in freq_itemsets.items():
            support = (count / total_transactions) * 100
            print(f"{itemset}: Count={count}, Support={support:.2f}%")
        
        k += 1
        candidates = generate_candidates(freq_itemsets.keys(), k)
        print(f"\nCandidates for {k}-itemsets:")
        print(candidates)
    
    print("\nAll frequent itemsets:")
    for itemset, count in frequent_itemsets.items():
        support = (count / total_transactions) * 100
        print(f"{itemset}: Count={count}, Support={support:.2f}%")
filename = 'prog7.csv'
min_support = 2
apriori(filename, min_support)
