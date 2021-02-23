import mmh3
import numpy as np
import pandas as pd
import sys


# Takes sequence_to_kmers, a dictionary mapping from an id
# to a set of shingles (or kmers), and num_hashes, number
# of hash functions for MinHash to create signature matrix.
# Returns signature matrix.
def compute_signature_matrix(sequence_to_kmers, num_hashes):
    signatures = []

    for sequence,kmers in sequence_to_kmers.items():
        signature_list = []

        for index in range(num_hashes):
            minimum = sys.maxsize
            for kmer in kmers:
                hashed = hash_kmer(kmer,index)
                if hashed < minimum:
                    minimum = hashed
            signature_list.append(minimum)

        signatures.append(signature_list)
    
    return signatures
    
# Takes sequence_to_kmers a dictionary mapping from an id
# to a set of shingles (or kmers), b the number of bands in
# the signature matrix, and r the number of rows per band.
# Returns the set of candidate pairs found and a list of b
# hash tables generated for each band.
def lsh_candidate_pairs(sequence_to_kmers, b, r, num_buckets):
    sequence_ids = list(sequence_to_kmers.keys())

    hash_tables = []
    candidate_pairs = set()

    for band in range(1, b + 1):
        hash_table = {}
        for col in range(len(sequence_ids)):
            band_sig = signatures[col][(band - 1) * r : band * r] 

            hash_value = mmh3.hash(str(band_sig), 42, signed=False) 
            bucket_num = hash_value % num_buckets        

            if bucket_num not in hash_table:
                hash_table[bucket_num] = set()

            hash_table[bucket_num].add(sequence_ids[col])

        for bucket_num, sequences in hash_table.items():
            for id1 in sequences:
                for id2 in sequences:
                    if id1 != id2:
                        candidate_pairs.add(tuple(sorted((id1, id2))))

        hash_tables.append(hash_table)
        
    return candidate_pairs, hash_tables