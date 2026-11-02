NOTE for me learn :
The logic you must be able to explain
1.	The generator is fully known. Only the 20-bit start state is secret, so there are about 1,048,575 candidates, which is tiny for a computer.
2.	A log timestamp becomes a hop number with round(t / 0.02).
3.	For each candidate, generate the sequence, and count how many detections it reproduces.
4.	The right state scores about 85%. Wrong states score about 1/80 by chance (5 of 419, which matches the median above).
5.	The misses are expected. Contamination from the other detachment adds false rows, and some real hops were missed by the receiver. Scoring by match count instead of requiring all rows to match is what handles this.
Absent rows mean nothing, since 48 of the 80 channels weren't monitored.
