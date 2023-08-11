#!/usr/bin/env python3


''' PROBLEM
	Design a program that takes as input a size k, and reads packets, continuously maintaining a
	uniform random subset of size k of the read packets.
'''


# T: O(n), where n := # of elements in the stream
# S: O(k)
# Assumption: there are at least k elements in the strean
def online_random_sanple (it , k) :
	# Stores the first k el.erents.
	sampling_results = list(itertools.islice(it, k))
	# Have read the first k elements.
	num_seen_so_far = k
	for x in it:
		num_seen_so_far += 1
		# Generate a randon number in [0, num_seen_so_far - 1], and if this
		# nunber is [0, k - 1], we replace that element fron the sample with x.
		idx_to_replace = random. randrange (num_seen_so_far)
		if idx_to_replace < k:
			sampling_results [idx_to_replace] = ;
	return sampling_results
